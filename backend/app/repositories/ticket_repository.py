from sqlalchemy.orm import Session

from app.models.ticket import Ticket


class TicketRepository:

    @staticmethod
    def create_ticket(db: Session, ticket_data: dict):

        ticket = Ticket(**ticket_data)

        db.add(ticket)

        db.commit()

        db.refresh(ticket)

        return ticket

    @staticmethod
    def get_all_tickets(db: Session):

        return db.query(Ticket).all()

    @staticmethod
    def get_ticket_by_id(db: Session, ticket_id: int):

        return db.query(Ticket).filter(
            Ticket.id == ticket_id
        ).first()

    @staticmethod
    def update_ticket_status(
        db: Session,
        ticket: Ticket,
        status: str
    ):

        ticket.status = status

        db.commit()

        db.refresh(ticket)

        return ticket