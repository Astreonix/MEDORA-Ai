from fastapi import APIRouter
from sqlalchemy import select

from app.api.deps import CurrentUser, DbSession
from app.models.document import Document
from app.schemas.brief import BriefResponse
from app.services.brief.brief_generator import generate_brief

router = APIRouter()


@router.post("/generate", response_model=BriefResponse)
def doctor_brief(user: CurrentUser, db: DbSession) -> dict[str, object]:
    documents = list(db.scalars(select(Document).where(Document.owner_id == user.id).order_by(Document.created_at.desc()).limit(20)))
    return generate_brief(documents)