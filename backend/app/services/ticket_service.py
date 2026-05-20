from sqlalchemy.orm import Session

from app.repositories.ticket_repository import TicketRepository

from app.services.workflow_service import WorkflowService

from app.services.classification_service import (
    ClassificationService
)

from app.services.priority_service import (
    PriorityService
)

from app.services.routing_service import (
    RoutingService
)

class TicketService:

    @staticmethod
    def create_ticket(db: Session, ticket_data):
        
        # ==========================================
        # CATEGORY PREDICTION
        # ==========================================
        predicted_category = (
            ClassificationService.classify_ticket(
                ticket_data.description
            )["category"]
        )

        # ==========================================
        # PRIORITY PREDICTION
        # ==========================================

        predicted_priority = (
            PriorityService.predict_priority(
                ticket_data.description
            )["priority"]
        )

        # ==========================================
        # DEPARTMENT ROUTING
        # ==========================================

        predicted_department = (
            RoutingService.predict_department(
                ticket_data.description
            )["department"]
        )

        # ==========================================
        # PREPARE TICKET DATA
        # ==========================================

        ticket_dict = ticket_data.dict()

        ticket_dict["category"] = predicted_category

        ticket_dict["priority"] = predicted_priority

        ticket_dict["department"] = predicted_department

        # ==========================================
        # CREATE TICKET
        # ==========================================

        ticket = TicketRepository.create_ticket(
            db,
            ticket_dict
        )

        # ==========================================
        # WORKFLOW LOG
        # ==========================================

        WorkflowService.log_action(
            db=db,
            ticket_id=ticket.id,
            action="TICKET_CREATED",
            details=(
                f"Ticket '{ticket.title}' created "
                f"with category '{predicted_category}', "
                f"priority '{predicted_priority}', "
                f"department '{predicted_department}'"
            )
        )
        
        return ticket

    @staticmethod
    def get_all_tickets(db: Session):

        return TicketRepository.get_all_tickets(db)

    @staticmethod
    def get_ticket_by_id(db: Session, ticket_id: int):

        return TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )
    
    @staticmethod
    def update_ticket_status(
        db: Session,
        ticket_id: int,
        status: str
    ):
        ticket = TicketRepository.get_ticket_by_id(
            db,
            ticket_id
        )
        
        if not ticket:
            return None
        
        updated_ticket = TicketRepository.update_ticket_status(
            db,
            ticket,
            status
        )

        WorkflowService.log_action(
            db=db,
            ticket_id=ticket.id,
            action="STATUS_UPDATED",
            details=f"Status updated to '{status}'"
        )

        return updated_ticket