from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.ticket_schema import (
    TicketCreate,
    TicketResponse,
    TicketStatusUpdate
)

from app.services.ticket_service import TicketService

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/", response_model=TicketResponse)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):

    return TicketService.create_ticket(db, ticket)


@router.get("/", response_model=list[TicketResponse])
def get_all_tickets(
    db: Session = Depends(get_db)
):

    return TicketService.get_all_tickets(db)


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    ticket = TicketService.get_ticket_by_id(
        db,
        ticket_id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.patch("/{ticket_id}/status")
def update_ticket_status(
    ticket_id: int,
    payload: TicketStatusUpdate,
    db: Session = Depends(get_db)
):

    updated_ticket = TicketService.update_ticket_status(
        db,
        ticket_id,
        payload.status
    )

    if not updated_ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "success": True,
        "data": updated_ticket
    }