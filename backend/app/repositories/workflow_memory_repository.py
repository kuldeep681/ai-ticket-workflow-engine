from sqlalchemy.orm import Session

from app.models.workflow_memory_profile import (
    WorkflowMemoryProfile
)


class WorkflowMemoryRepository:

    # ==========================================
    # CREATE MEMORY PROFILE
    # ==========================================

    @staticmethod
    def create_memory_profile(
        db: Session,
        memory_data: dict
    ):

        memory_profile = (
            WorkflowMemoryProfile(
                **memory_data
            )
        )

        db.add(memory_profile)

        db.commit()

        db.refresh(memory_profile)

        return memory_profile

    # ==========================================
    # GET WORKFLOW MEMORIES
    # ==========================================

    @staticmethod
    def get_workflow_memories(
        db: Session,
        workflow_type: str,
        issue_type: str
    ):

        return (
            db.query(
                WorkflowMemoryProfile
            )
            .filter(
                WorkflowMemoryProfile.workflow_type
                == workflow_type,

                WorkflowMemoryProfile.issue_type
                == issue_type
            )
            .all()
        )