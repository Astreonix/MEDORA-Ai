from io import BytesIO


def extract_text(content: bytes, content_type: str, filename: str = "") -> str:
    """Extract text without writing uploads to disk."""
    if content_type == "application/pdf" or filename.lower().endswith(".pdf"):
        try:
            import pdfplumber

            with pdfplumber.open(BytesIO(content)) as pdf:
                return "\n".join((page.extract_text() or "") for page in pdf.pages).strip()
        except Exception:
            return ""
    return content.decode("utf-8", errors="replace").strip()
import io
import pdfplumber

def extract_text(content: bytes, filename: str) -> tuple[str, bool]:
    if filename.lower().endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages).strip(), False
    return "", True