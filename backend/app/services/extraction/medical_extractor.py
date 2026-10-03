import re
from .confidence_scorer import needs_review

def extract_items(text: str, ocr_source: bool = False) -> list[dict]:
    items = []
    for line in (line.strip() for line in text.splitlines() if line.strip()):
        if re.search(r"\d", line):
            items.append({"kind": "note", "name": "Documented value", "value": line, "confidence": 0.7 if ocr_source else 0.9, "needs_review": needs_review(0.7 if ocr_source else 0.9, ocr_source, line), "source_snippet": line})
    return items