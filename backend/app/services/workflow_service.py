from sqlalchemy.orm import Session

from app.repositories.workflow_repository import (
    WorkflowRepository
)


class WorkflowService:

    @staticmethod
    def log_action(
        db: Session,
        ticket_id: int,
        action: str,
        details: str
    ):

        log_data = {
            "ticket_id": ticket_id,
            "action": action,
            "details": details
        }

        return WorkflowRepository.create_log(
            db,
            log_data
        )

    @staticmethod
    def get_logs(
        db: Session,
        ticket_id: int
    ):

        return WorkflowRepository.get_ticket_logs(
            db,
            ticket_id
        )