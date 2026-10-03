def ocr_image(_: bytes) -> str:
    """OCR is optional; return an explicit safe fallback when no OCR engine is installed."""
    return ""
def transcribe_image(_content: bytes) -> str:
    return ""