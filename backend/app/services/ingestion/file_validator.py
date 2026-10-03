from dataclasses import dataclass

from app.core.config import settings


ALLOWED_TYPES = {"application/pdf", "text/plain", "text/csv", "image/png", "image/jpeg"}


@dataclass(frozen=True)
class FileValidation:
    valid: bool
    reason: str = ""


def validate_file(filename: str | None, content_type: str | None, size: int) -> FileValidation:
    if not filename or not filename.strip():
        return FileValidation(False, "A filename is required")
    if size <= 0:
        return FileValidation(False, "The file is empty")
    if size > settings.max_upload_bytes:
        return FileValidation(False, "The file exceeds the upload limit")
    if content_type and content_type.lower() not in ALLOWED_TYPES:
        return FileValidation(False, "Unsupported file type")
    return FileValidation(True)
from app.core.config import settings
from app.utils.file_helpers import has_valid_signature, extension_for

def validate_upload(filename: str, content: bytes, content_type: str = "") -> None:
    if len(content) > min(settings.max_upload_bytes, 10 * 1024 * 1024): raise ValueError("Uploaded file is larger than 10 MB.")
    if extension_for(filename) not in {".pdf", ".png", ".jpg", ".jpeg"}: raise ValueError("Only PDF, PNG, and JPG files are supported.")
    if not has_valid_signature(filename, content): raise ValueError("The uploaded file signature does not match its extension.")