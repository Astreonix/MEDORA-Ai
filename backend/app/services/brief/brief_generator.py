from app.services.safety.disclaimer import DISCLAIMER


def generate_brief(documents: list[object]) -> dict[str, object]:
    names = [getattr(document, "title", getattr(document, "filename", "Document")) for document in documents]
    return {
        "summary": f"Doctor visit brief based on {len(documents)} document(s).",
        "documents": names,
        "questions": ["What should I ask my clinician about these records?"],
        "documented_conditions": [],
        "current_medications": [],
        "recent_tests": [],
        "important_events": [],
        "latest_available_report": names[0] if names else "",
        "sources": names,
        "uncertain_items": ["No extracted medical fields are available yet."] if not documents else [],
        "disclaimer": DISCLAIMER,
    }