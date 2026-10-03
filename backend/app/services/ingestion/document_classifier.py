def classify_document(filename: str, content_type: str = "") -> str:
    name = filename.lower()
    if "lab" in name or "result" in name:
        return "lab_result"
    if "prescription" in name or "medication" in name:
        return "prescription"
    if "discharge" in name:
        return "discharge_summary"
    return "medical_document" if content_type in {"application/pdf", "text/plain"} else "image"