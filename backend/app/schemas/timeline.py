from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class MedicalEventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    event_type: str
    title: str
    description: str
    event_date: date | None
    document_id: int | None
    created_at: datetime