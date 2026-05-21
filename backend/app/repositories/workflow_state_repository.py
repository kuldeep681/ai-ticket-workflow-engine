from sqlalchemy.orm import Session

from app.models.workflow_state import (
    WorkflowState
)


class WorkflowStateRepository:

    @staticmethod
    def create_workflow_state(
        db: Session,
        workflow_state_data: dict
    ):

        workflow_state = WorkflowState(
            **workflow_state_data
        )

        db.add(workflow_state)

        db.commit()

        db.refresh(workflow_state)

        return workflow_state

    @staticmethod
    def get_workflow_state(
        db: Session,
        ticket_id: int
    ):

        return db.query(WorkflowState).filter(
            WorkflowState.ticket_id == ticket_id
        ).first()

    @staticmethod
    def update_workflow_state(
        db: Session,
        workflow_state: WorkflowState,
        updated_data: dict
    ):

        for key, value in updated_data.items():

            setattr(
                workflow_state,
                key,
                value
            )

        db.commit()

        db.refresh(workflow_state)

        return workflow_state