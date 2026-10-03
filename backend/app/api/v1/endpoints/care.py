from fastapi import APIRouter, Query

from app.api.deps import CurrentUser
from app.schemas.care import CareProviderResponse, CareSearchRequest
from app.services.care.care_service import find_care

router = APIRouter()


@router.get("/search", response_model=list[CareProviderResponse])
def search_care(
    _: CurrentUser,
    specialty: str = Query("", max_length=120),
    location: str = Query("", max_length=120),
    visit_type: str = Query("", max_length=40),
    cost: str = Query("", max_length=40),
) -> list[dict[str, str]]:
    return find_care(specialty, location, visit_type, cost)