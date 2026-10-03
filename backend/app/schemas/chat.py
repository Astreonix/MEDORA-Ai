from pydantic import BaseModel, Field, model_validator


class ChatSource(BaseModel):
    document_id: int
    document_name: str
    snippet: str
    page: int | None = None


class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)
    language: str = Field(default="English", min_length=2, max_length=40)
    session_id: int | None = None

    @model_validator(mode="before")
    @classmethod
    def accept_legacy_message(cls, values: object) -> object:
        if isinstance(values, dict) and "question" not in values and "message" in values:
            values = {**values, "question": values["message"]}
        return values


class ChatResponse(BaseModel):
    answer: str
    session_id: int
    language: str
    sources: list[ChatSource] = []
    disclaimer: str
    is_emergency: bool = False
    not_enough_information: bool = False