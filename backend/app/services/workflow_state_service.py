from sqlalchemy.orm import Session

from app.repositories.workflow_state_repository import (
    WorkflowStateRepository
)

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.workflow.workflow_transitions import (
    WORKFLOW_TRANSITIONS,
    TERMINAL_STATES
)


class WorkflowStateService:

    # =====================================================
    # INITIALIZE WORKFLOW
    # =====================================================

    @staticmethod
    def initialize_workflow_state(
        db: Session,
        ticket_id: int,
        workflow_type: str,
        current_issue: str,
        current_step: str
    ):

        existing_state = (
            WorkflowStateRepository.get_workflow_state(
                db,
                ticket_id
            )
        )

        # =================================================
        # PREVENT DUPLICATE STATES
        # =================================================

        if existing_state:
            return existing_state

        workflow_state_data = {

            "ticket_id":
            ticket_id,

            "workflow_type":
            workflow_type,

            "current_issue":
            current_issue,

            "current_step":
            current_step,

            "status":
            "in_progress"
        }

        workflow_state = (
            WorkflowStateRepository.create_workflow_state(
                db,
                workflow_state_data
            )
        )

        # =================================================
        # SYNC TICKET STATUS
        # =================================================

        ticket = (
            TicketRepository.get_ticket_by_id(
                db,
                ticket_id
            )
        )

        if ticket:

            TicketRepository.update_ticket_status(
                db,
                ticket,
                "IN_PROGRESS"
            )

        return workflow_state

    # =====================================================
    # GET WORKFLOW STATE
    # =====================================================

    @staticmethod
    def get_workflow_state(
        db: Session,
        ticket_id: int
    ):

        return (
            WorkflowStateRepository.get_workflow_state(
                db,
                ticket_id
            )
        )

    # =====================================================
    # VALIDATE TRANSITION
    # =====================================================

    @staticmethod
    def is_valid_transition(
        workflow_type: str,
        current_step: str,
        next_step: str
    ):

        workflow_graph = (
            WORKFLOW_TRANSITIONS.get(
                workflow_type,
                {}
            )
        )

        allowed_steps = (
            workflow_graph.get(
                current_step,
                []
            )
        )

        return next_step in allowed_steps

    # =====================================================
    # UPDATE WORKFLOW STATE
    # =====================================================

    @staticmethod
    def update_workflow_state(
        db: Session,
        ticket_id: int,
        updated_data: dict
    ):

        workflow_state = (
            WorkflowStateRepository.get_workflow_state(
                db,
                ticket_id
            )
        )

        if not workflow_state:
            return None

        current_step = workflow_state.current_step

        workflow_type = workflow_state.workflow_type

        next_step = updated_data.get(
            "current_step",
            current_step
        )

        # =================================================
        # VALIDATE STEP TRANSITION
        # =================================================

        if next_step != current_step:

            is_valid = (
                WorkflowStateService.is_valid_transition(
                    workflow_type,
                    current_step,
                    next_step
                )
            )

            if not is_valid:

                print(
                    f"Blocked invalid transition: "
                    f"{workflow_type} | "
                    f"{current_step} -> {next_step}"
                )

                return workflow_state

        # =================================================
        # TERMINAL STATE DETECTION
        # =================================================

        if next_step in TERMINAL_STATES:

            updated_data["status"] = next_step

        # =================================================
        # UPDATE STATE
        # =================================================

        updated_state = (
            WorkflowStateRepository.update_workflow_state(
                db,
                workflow_state,
                updated_data
            )
        )

        # =================================================
        # SYNC TICKET STATUS
        # =================================================

        ticket = (
            TicketRepository.get_ticket_by_id(
                db,
                ticket_id
            )
        )

        if ticket:

            workflow_status = (
                updated_state.status.lower()
            )

            if workflow_status == "resolved":

                TicketRepository.update_ticket_status(
                    db,
                    ticket,
                    "RESOLVED"
                )

            elif workflow_status == "escalated":

                TicketRepository.update_ticket_status(
                    db,
                    ticket,
                    "ESCALATED"
                )

            elif workflow_status == "awaiting_user":

                TicketRepository.update_ticket_status(
                    db,
                    ticket,
                    "WAITING_FOR_USER"
                )

            else:

                TicketRepository.update_ticket_status(
                    db,
                    ticket,
                    "IN_PROGRESS"
                )

        return updated_state