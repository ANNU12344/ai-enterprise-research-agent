from datetime import datetime

from pydantic import BaseModel


class ResearchRequest(BaseModel):
    company_name: str


class SourceResponse(BaseModel):
    id: int
    url: str
    title: str | None
    report_id: int

    model_config = {
        "from_attributes": True
    }


class ResearchResponse(BaseModel):
    id: int
    company_name: str
    report_content: str
    user_id: int
    created_at: datetime
    sources: list[SourceResponse] = []

    model_config = {
        "from_attributes": True
    }