from pathlib import Path

ALLOWED_SIGNATURES = {".pdf": b"%PDF", ".png": b"\x89PNG", ".jpg": b"\xff\xd8\xff", ".jpeg": b"\xff\xd8\xff"}

def extension_for(filename: str) -> str:
    return Path(filename or "").suffix.lower()

def has_valid_signature(filename: str, content: bytes) -> bool:
    signature = ALLOWED_SIGNATURES.get(extension_for(filename))
    return bool(signature and content.startswith(signature))