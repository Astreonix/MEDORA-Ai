from pydantic import BaseModel


class BriefResponse(BaseModel):
    summary: str
    documents: list[str]
    questions: list[str]
    documented_conditions: list[str] = []
    current_medications: list[str] = []
    recent_tests: list[str] = []
    important_events: list[str] = []
    latest_available_report: str = ""
    sources: list[str] = []
    uncertain_items: list[str] = []
    disclaimer: str