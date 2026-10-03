from fastapi import APIRouter
from app.api.deps import CurrentUser

router = APIRouter()

@router.get("")
def compare(_: CurrentUser) -> dict[str, str]:
    return {"status": "ready", "message": "Select two of your documents to compare."}