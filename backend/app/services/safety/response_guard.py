import re

from app.services.safety.disclaimer import with_disclaimer
from app.services.safety.emergency_detector import detect_emergency, emergency_message


def guard_response(text: str, user_input: str = "") -> str:
    if detect_emergency(user_input):
        return f"{emergency_message()}\n\n{with_disclaimer(text)}"
    if re.search(r"\b(you have|take|increase|decrease your dose)\b", text, re.I):
        return "MEDORA cannot diagnose or prescribe. Please ask your doctor."
    return with_disclaimer(text)
