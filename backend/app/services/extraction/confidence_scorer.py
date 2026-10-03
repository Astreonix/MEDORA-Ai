def needs_review(confidence: float, ocr_source: bool = False, value: str = "") -> bool:
    return confidence < 0.75 or (ocr_source and any(char.isdigit() for char in value)) or not value.strip()