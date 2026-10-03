from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class ExtractedItem(Base):
    __tablename__ = "extracted_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id", ondelete="CASCADE"), index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    kind: Mapped[str] = mapped_column(String(40), default="note")
    name: Mapped[str] = mapped_column(String(255), default="")
    value: Mapped[str] = mapped_column(Text, default="")
    confidence: Mapped[float] = mapped_column(default=1.0)
    needs_review: Mapped[bool] = mapped_column(Boolean, default=False)
    source_snippet: Mapped[str] = mapped_column(Text, default="")