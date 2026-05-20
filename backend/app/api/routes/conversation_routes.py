from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.conversation_schema import (
    MessageCreate,
    MessageResponse
)

from app.services.conversation_service import (
    ConversationService
)

router = APIRouter(
    prefix="/tickets",
    tags=["Conversations"]
)


@router.post(
    "/{ticket_id}/messages",
    response_model=MessageResponse
)
def add_message(
    ticket_id: int,
    payload: MessageCreate,
    db: Session = Depends(get_db)
):

    message = ConversationService.add_message(
        db,
        ticket_id,
        payload
    )

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return message


@router.get(
    "/{ticket_id}/messages",
    response_model=list[MessageResponse]
)
def get_messages(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    messages = ConversationService.get_messages(
        db,
        ticket_id
    )

    if messages is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return messages