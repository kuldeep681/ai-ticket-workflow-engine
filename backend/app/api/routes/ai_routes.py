from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.conversation_service import (
    ConversationService
)

from app.schemas.conversation_schema import (
    MessageResponse
)

router = APIRouter(
    prefix="/tickets",
    tags=["AI"]
)


@router.post(
    "/{ticket_id}/ai-response",
    response_model=MessageResponse
)
def generate_ai_response(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    response = (
        ConversationService.generate_ai_response(
            db,
            ticket_id
        )
    )

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return response