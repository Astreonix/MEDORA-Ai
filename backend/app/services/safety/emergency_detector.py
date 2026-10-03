EMERGENCY_TERMS = (
    "chest pain", "difficulty breathing", "can't breathe", "cannot breathe",
    "severe bleeding", "unconscious", "stroke", "suicid", "overdose",
)


def detect_emergency(text: str) -> bool:
    normalized = text.casefold()
    return any(term in normalized for term in EMERGENCY_TERMS)


def emergency_message() -> str:
    return "If this may be an emergency, call your local emergency number or go to the nearest emergency department now."