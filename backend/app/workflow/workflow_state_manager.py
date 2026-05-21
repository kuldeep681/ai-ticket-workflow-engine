from app.workflow.workflow_rules import (
    WORKFLOW_RULES
)

from app.workflow.workflow_lifecycle import (
    WORKFLOW_LIFECYCLE
)

from app.services.workflow_state_service import (
    WorkflowStateService
)

from app.services.ticket_service import (
    TicketService
)


class WorkflowStateManager:

    # =====================================================
    # DETECT WORKFLOW
    # =====================================================

    @staticmethod
    def detect_workflow(
        message: str
    ):

        if not message:
            return None

        normalized = (
            message
            .lower()
            .strip()
        )

        # =================================================
        # HARD NORMALIZATION
        # =================================================

        normalized = " ".join(
            normalized.split()
        )

        for workflow in WORKFLOW_RULES:

            for keyword in workflow["keywords"]:

                keyword_normalized = (
                    keyword
                    .lower()
                    .strip()
                )

                if keyword_normalized in normalized:

                    return workflow

        return None

    # =====================================================
    # DETECT LIFECYCLE
    # =====================================================

    @staticmethod
    def detect_lifecycle(
        message: str
    ):

        if not message:
            return None

        normalized = (
            message
            .lower()
            .strip()
        )

        # =================================================
        # REMOVE PUNCTUATION
        # =================================================

        replacements = [

            ".",
            ",",
            "!",
            "?",
            ":",
            ";",
            "-",
            "_",
            "\n",
            "\t"

        ]

        for item in replacements:

            normalized = normalized.replace(
                item,
                " "
            )

        # =================================================
        # REMOVE EXTRA SPACES
        # =================================================

        normalized = " ".join(
            normalized.split()
        )

        # =================================================
        # DEBUGGING
        # =================================================

        print("\n========== LIFECYCLE CHECK ==========")
        print("USER MESSAGE:", message)
        print("NORMALIZED:", normalized)

        # =================================================
        # DETECT LIFECYCLE
        # =================================================

        for lifecycle, phrases in (
            WORKFLOW_LIFECYCLE.items()
        ):

            for phrase in phrases:

                phrase_normalized = (
                    phrase
                    .lower()
                    .strip()
                )

                if phrase_normalized in normalized:

                    print(
                        f"MATCHED LIFECYCLE: {lifecycle}"
                    )

                    return lifecycle

        print("NO LIFECYCLE MATCH")
        print("====================================\n")

        return None

    # =====================================================
    # INITIALIZE WORKFLOW
    # =====================================================

    @staticmethod
    def initialize_workflow(
        db,
        ticket_id: int,
        user_message: str
    ):

        existing = (
            WorkflowStateService
            .get_workflow_state(
                db,
                ticket_id
            )
        )

        # =================================================
        # PREVENT DUPLICATE STATES
        # =================================================

        if existing:
            return existing

        # =================================================
        # LOAD TICKET
        # =================================================

        ticket = TicketService.get_ticket_by_id(
            db,
            ticket_id
        )

        workflow_source = user_message

        # =================================================
        # USE ORIGINAL TICKET DESCRIPTION
        # =================================================

        if ticket and ticket.description:

            workflow_source = (
                ticket.description
            )

        print(
            f"\nWORKFLOW SOURCE: "
            f"{workflow_source}"
        )

        workflow = (
            WorkflowStateManager
            .detect_workflow(
                workflow_source
            )
        )

        if not workflow:

            print(
                "NO WORKFLOW DETECTED"
            )

            return None

        workflow_state = (
            WorkflowStateService
            .initialize_workflow_state(
                db=db,

                ticket_id=ticket_id,

                workflow_type=(
                    workflow["workflow_type"]
                ),

                current_issue=(
                    workflow["current_issue"]
                ),

                current_step=(
                    workflow["current_step"]
                )
            )
        )

        print(
            f"WORKFLOW INITIALIZED: "
            f"{workflow['workflow_type']}"
        )

        # =================================================
        # UPDATE TICKET STATUS
        # =================================================

        TicketService.update_ticket_status(
            db,
            ticket_id,
            "IN_PROGRESS"
        )

        print(
            "TICKET STATUS UPDATED "
            "TO IN_PROGRESS"
        )

        return workflow_state

    # =====================================================
    # PROCESS MESSAGE
    # =====================================================

    @staticmethod
    def process_message(
        db,
        ticket_id: int,
        user_message: str
    ):

        workflow_state = (
            WorkflowStateService
            .get_workflow_state(
                db,
                ticket_id
            )
        )

        # =================================================
        # INITIALIZE WORKFLOW
        # =================================================

        if not workflow_state:

            workflow_state = (
                WorkflowStateManager
                .initialize_workflow(
                    db,
                    ticket_id,
                    user_message
                )
            )

            return workflow_state

        print(
            f"\nCURRENT WORKFLOW STATUS: "
            f"{workflow_state.status}"
        )

        # =================================================
        # DETECT LIFECYCLE
        # =================================================

        lifecycle = (
            WorkflowStateManager
            .detect_lifecycle(
                user_message
            )
        )

        print(
            f"DETECTED LIFECYCLE: {lifecycle}"
        )

        # =================================================
        # RESOLVED
        # =================================================

        if lifecycle == "resolved":

            updated_state = (
                WorkflowStateService
                .update_workflow_state(
                    db,
                    ticket_id,
                    {
                        "status":
                        "resolved"
                    }
                )
            )

            TicketService.update_ticket_status(
                db,
                ticket_id,
                "RESOLVED"
            )

            print(
                "TICKET STATUS UPDATED "
                "TO RESOLVED"
            )

            return updated_state

        # =================================================
        # ESCALATED
        # =================================================

        if lifecycle == "escalated":

            updated_state = (
                WorkflowStateService
                .update_workflow_state(
                    db,
                    ticket_id,
                    {
                        "status":
                        "escalated"
                    }
                )
            )

            TicketService.update_ticket_status(
                db,
                ticket_id,
                "ESCALATED"
            )

            print(
                "TICKET STATUS UPDATED "
                "TO ESCALATED"
            )

            return updated_state

        # =================================================
        # AWAITING USER
        # =================================================

        if lifecycle == "awaiting_user":

            updated_state = (
                WorkflowStateService
                .update_workflow_state(
                    db,
                    ticket_id,
                    {
                        "status":
                        "awaiting_user"
                    }
                )
            )

            TicketService.update_ticket_status(
                db,
                ticket_id,
                "IN_PROGRESS"
            )

            print(
                "WORKFLOW WAITING "
                "FOR USER"
            )

            return updated_state

        # =================================================
        # KEEP ACTIVE STATE
        # =================================================

        print(
            "NO STATE CHANGE"
        )

        return workflow_state