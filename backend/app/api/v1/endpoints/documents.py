from fastapi import APIRouter, File, HTTPException, UploadFile, status
from fastapi.responses import Response
from sqlalchemy import select

from app.api.deps import CurrentUser, DbSession
from app.core.config import settings
from app.core.database import SessionLocal
from app.models.document import Document
from app.schemas.document import DocumentResponse, DocumentStatusResponse
from app.services.ingestion.document_classifier import classify_document
from app.services.ingestion.file_validator import validate_file
from app.services.ingestion.text_extractor import extract_text

router = APIRouter()


@router.get("", response_model=list[DocumentResponse])
def list_documents(user: CurrentUser, db: DbSession) -> list[Document]:
    return list(db.scalars(select(Document).where(Document.owner_id == user.id).order_by(Document.created_at.desc())))


@router.post("", response_model=DocumentResponse, status_code=201)
async def upload_document(user: CurrentUser, db: DbSession, file: UploadFile = File(...)) -> Document:
    content = await file.read()
    validation = validate_file(file.filename, file.content_type, len(content))
    if not validation.valid:
        code = 413 if len(content) > settings.max_upload_bytes else 400
        raise HTTPException(status_code=code, detail=validation.reason)
    extracted_text = extract_text(content, file.content_type or "", file.filename or "")
    document = Document(owner_id=user.id, filename=file.filename or "upload", content_type=file.content_type or "application/octet-stream",
                        size_bytes=len(content), content=content, title=file.filename or "Untitled document",
                        document_type=classify_document(file.filename or "", file.content_type or ""),
                        processing_status="completed", processing_progress=100,
                        extracted_text=extracted_text)
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


@router.post("/upload", response_model=list[DocumentResponse], status_code=201)
async def upload_documents(
    user: CurrentUser,
    db: DbSession,
    files: list[UploadFile] = File(...),
) -> list[Document]:
    if not files:
        raise HTTPException(status_code=400, detail="At least one file is required")

    documents: list[Document] = []
    for file in files:
        content = await file.read()
        validation = validate_file(file.filename, file.content_type, len(content))
        if not validation.valid:
            code = 413 if len(content) > settings.max_upload_bytes else 400
            raise HTTPException(status_code=code, detail=f"{file.filename or 'upload'}: {validation.reason}")
        filename = file.filename or "upload"
        content_type = file.content_type or "application/octet-stream"
        document = Document(
            owner_id=user.id,
            filename=filename,
            content_type=content_type,
            size_bytes=len(content),
            content=content,
            title=filename,
            document_type=classify_document(filename, content_type),
            processing_status="processing",
            processing_progress=10,
            extracted_text="",
        )
        db.add(document)
        documents.append(document)

    db.commit()
    for document in documents:
        db.refresh(document)
        _process_document(document.id)
    return documents


def _process_document(document_id: int) -> None:
    db = SessionLocal()
    try:
        document = db.get(Document, document_id)
        if not document:
            return
        document.processing_progress = 40
        db.commit()
        document.extracted_text = extract_text(document.content, document.content_type, document.filename)
        document.processing_progress = 100
        document.processing_status = "completed"
        document.processing_error = None
        db.commit()
    except Exception as exc:
        db.rollback()
        document = db.get(Document, document_id)
        if document:
            document.processing_status = "failed"
            document.processing_error = str(exc)
            document.processing_progress = 0
            db.commit()
    finally:
        db.close()


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, user: CurrentUser, db: DbSession) -> Document:
    document = db.scalar(select(Document).where(Document.id == document_id, Document.owner_id == user.id))
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.get("/{document_id}/status", response_model=DocumentStatusResponse)
def get_document_status(document_id: int, user: CurrentUser, db: DbSession) -> DocumentStatusResponse:
    document = db.scalar(select(Document).where(Document.id == document_id, Document.owner_id == user.id))
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return DocumentStatusResponse(
        document_id=document.id,
        status=document.processing_status,
        progress=document.processing_progress,
        error=document.processing_error,
    )


@router.get("/{document_id}/file")
def get_document_file(document_id: int, user: CurrentUser, db: DbSession) -> Response:
    document = db.scalar(select(Document).where(Document.id == document_id, Document.owner_id == user.id))
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return Response(content=document.content, media_type=document.content_type, headers={"Content-Disposition": f'inline; filename="{document.filename}"'})


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(document_id: int, user: CurrentUser, db: DbSession) -> None:
    document = db.scalar(select(Document).where(Document.id == document_id, Document.owner_id == user.id))
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(document)
    db.commit()