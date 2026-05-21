from sqlalchemy.orm import Session

from app.repositories.workflow_memory_repository import (
    WorkflowMemoryRepository
)

from app.services.workflow_state_service import (
    WorkflowStateService
)

from app.services.summary_service import (
    SummaryService
)


class WorkflowMemoryService:

    # ==========================================
    # STORE RESOLVED WORKFLOW MEMORY
    # ==========================================

    @staticmethod
    def store_resolution_memory(
        db: Session,
        ticket_id: int
    ):

        workflow_state = (
            WorkflowStateService.get_workflow_state(
                db,
                ticket_id
            )
        )

        if not workflow_state:
            return None

        # ======================================
        # STORE ONLY RESOLVED WORKFLOWS
        # ======================================

        if workflow_state.status != "resolved":
            return None

        summaries = (
            SummaryService.get_ticket_summaries(
                db,
                ticket_id
            )
        )

        if not summaries:
            return None

        latest_summary = summaries[-1]

        return (
            WorkflowMemoryRepository
            .create_memory_profile(
                db,
                {
                    "workflow_type":
                    workflow_state.workflow_type,

                    "issue_type":
                    workflow_state.current_issue,

                    "resolution_summary":
                    latest_summary.summary
                }
            )
        )

    # ==========================================
    # GET HISTORICAL MEMORIES
    # ==========================================

    @staticmethod
    def get_historical_memories(
        db: Session,
        workflow_type: str,
        issue_type: str
    ):

        memories = (
            WorkflowMemoryRepository
            .get_workflow_memories(
                db,
                workflow_type,
                issue_type
            )
        )

        if not memories:
            return ""

        memory_lines = []

        for memory in memories:

            memory_lines.append(
                f"- {memory.resolution_summary}"
            )

        return "\n".join(memory_lines)