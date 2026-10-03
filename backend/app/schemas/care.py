from pydantic import BaseModel, Field


class CareSearchRequest(BaseModel):
    specialty: str = Field(default="", max_length=120)
    city: str = Field(default="", max_length=120)


class CareProviderResponse(BaseModel):
    id: str = ""
    name: str
    specialty: str
    location: str
    visit_type: str = "Contact provider"
    cost: str = "Verify with provider"
    note: str
    is_prototype: bool = True