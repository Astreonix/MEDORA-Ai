from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    filename: str
    content_type: str
    size_bytes: int
    title: str
    document_type: str
    processing_status: str
    processing_progress: int
    processing_error: str | None
    extracted_text: str
    created_at: datetime


class DocumentStatusResponse(BaseModel):
    document_id: int
    status: str
    progress: int
    error: str | None = None