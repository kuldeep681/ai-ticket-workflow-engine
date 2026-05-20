from sqlalchemy.orm import Session

from app.models.workflow_log import WorkflowLog


class WorkflowRepository:

    @staticmethod
    def create_log(
        db: Session,
        log_data: dict
    ):

        log = WorkflowLog(**log_data)

        db.add(log)

        db.commit()

        db.refresh(log)

        return log

    @staticmethod
    def get_ticket_logs(
        db: Session,
        ticket_id: int
    ):

        return db.query(WorkflowLog).filter(
            WorkflowLog.ticket_id == ticket_id
        ).all()