import re

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.api.deps import CurrentUser
from app.services.safety.response_guard import guard_response
from app.services.simplifier.simplifier_service import simplify_text

router = APIRouter()


class SimplifyRequest(BaseModel):
    text: str = Field(min_length=1, max_length=12000)
    language: str = Field(default="English", min_length=2, max_length=40)


class SimplifyResponse(BaseModel):
    simple_explanation: str
    roman_urdu: str = ""
    preserved_facts: dict[str, list[str]]
    disclaimer: str


@router.post("/explain", response_model=SimplifyResponse)
def simplify(payload: SimplifyRequest, _: CurrentUser) -> SimplifyResponse:
    safe_text = guard_response(simplify_text(payload.text), payload.text)
    facts = re.findall(r"\b(?:\d+(?:\.\d+)?\s*(?:mg|ml|mcg|mmHg|%)?|20\d{2})\b", payload.text, re.I)
    return SimplifyResponse(
        simple_explanation=safe_text,
        roman_urdu=safe_text if payload.language.casefold() == "roman urdu" else "Roman Urdu explanation is available after review by a qualified clinician.",
        preserved_facts={
            "dates": [fact for fact in facts if re.fullmatch(r"20\d{2}", fact)],
            "doses": [fact for fact in facts if re.search(r"(mg|ml|mcg)", fact, re.I)],
            "measurements": [fact for fact in facts if re.search(r"(mmHg|%)", fact, re.I)],
            "lab_values": [],
        },
        disclaimer="This explanation does not replace advice from a doctor.",
    )