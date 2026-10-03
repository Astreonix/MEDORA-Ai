from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.api.deps import CurrentUser, DbSession
from app.models.medical_event import MedicalEvent
from app.schemas.timeline import MedicalEventResponse

router = APIRouter()


@router.get("", response_model=list[MedicalEventResponse])
def timeline(user: CurrentUser, db: DbSession) -> list[MedicalEvent]:
    return list(db.scalars(select(MedicalEvent).where(MedicalEvent.owner_id == user.id).order_by(MedicalEvent.event_date.desc(), MedicalEvent.created_at.desc())))


@router.get("/{event_id}", response_model=MedicalEventResponse)
def get_event(event_id: int, user: CurrentUser, db: DbSession) -> MedicalEvent:
    event = db.scalar(select(MedicalEvent).where(MedicalEvent.id == event_id, MedicalEvent.owner_id == user.id))
    if not event:
        raise HTTPException(status_code=404, detail="Medical event not found")
    return event