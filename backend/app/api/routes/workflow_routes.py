from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.workflow_schema import (
    WorkflowLogResponse
)

from app.services.workflow_service import (
    WorkflowService
)

router = APIRouter(
    prefix="/tickets",
    tags=["Workflow Logs"]
)


@router.get(
    "/{ticket_id}/logs",
    response_model=list[WorkflowLogResponse]
)
def get_logs(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    return WorkflowService.get_logs(
        db,
        ticket_id
    )