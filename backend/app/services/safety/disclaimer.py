DISCLAIMER = "MEDORA provides general information and is not a substitute for a qualified healthcare professional."


def with_disclaimer(text: str) -> str:
    return f"{text.strip()}\n\n{DISCLAIMER}" if text.strip() else DISCLAIMER
DISCLAIMER = "MEDORA is an AI tool, not a doctor. It does not diagnose or replace professional medical advice."
def get_disclaimer() -> str:
    return DISCLAIMER