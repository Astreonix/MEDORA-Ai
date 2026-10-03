from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.api.deps import CurrentUser, DbSession
from app.models.chat_session import ChatMessage, ChatSession
from app.schemas.chat import ChatRequest, ChatResponse, ChatSource
from app.models.document import Document
from app.services.safety.disclaimer import get_disclaimer
from app.services.safety.emergency_detector import detect_emergency, emergency_message
from app.services.safety.response_guard import guard_response

router = APIRouter()


@router.post("/ask", response_model=ChatResponse)
def chat(payload: ChatRequest, user: CurrentUser, db: DbSession) -> ChatResponse:
    session = db.scalar(select(ChatSession).where(ChatSession.id == payload.session_id, ChatSession.owner_id == user.id)) if payload.session_id else None
    if payload.session_id and not session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    if session is None:
        session = ChatSession(owner_id=user.id)
        db.add(session)
        db.flush()
    db.add(ChatMessage(session_id=session.id, role="user", content=payload.question))
    is_emergency = detect_emergency(payload.question)
    documents = list(db.scalars(select(Document).where(Document.owner_id == user.id).order_by(Document.created_at.desc()).limit(3)))
    sources = [
        ChatSource(document_id=document.id, document_name=document.filename,
                   snippet=(document.extracted_text[:240] or "No extracted text is available yet."))
        for document in documents
    ]
    not_enough_information = not documents and not is_emergency
    answer = emergency_message() if is_emergency else (
        "I could not find enough information in your uploaded records to answer that safely. Please ask your doctor."
        if not_enough_information else
        "I can help you understand what is documented in your records. Please consult a qualified clinician for diagnosis or treatment advice."
    )
    answer = guard_response(answer, payload.question)
    db.add(ChatMessage(session_id=session.id, role="assistant", content=answer))
    db.commit()
    return ChatResponse(answer=answer, session_id=session.id, language=payload.language,
                        sources=[] if is_emergency else sources, disclaimer=get_disclaimer(),
                        is_emergency=is_emergency, not_enough_information=not_enough_information)