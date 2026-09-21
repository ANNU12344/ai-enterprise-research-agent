from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import ResearchReport
from app.schemas.research import ResearchRequest, ResearchResponse


router = APIRouter(
    prefix="/research",
    tags=["Research"],
)


@router.post(
    "",
    response_model=ResearchResponse,
)
def create_research(
    research_data: ResearchRequest,
    db: Session = Depends(get_db),
):
    report = ResearchReport(
        company_name=research_data.company_name,
        report_content="Research report will be generated here.",
        user_id=2,
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return report