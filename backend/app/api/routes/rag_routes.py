from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.schemas.rag_schema import (
    RAGQueryRequest,
    RAGQueryResponse
)

from app.services.rag_service import (
    RAGService
)

from app.workflow.workflow_state_manager import (
    WorkflowStateManager
)

from app.workflow.workflow_context_builder import (
    WorkflowContextBuilder
)

# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

# =========================================================
# RAG QUERY
# =========================================================

@router.post(
    "/query",
    response_model=RAGQueryResponse
)
def query_rag(
    request: RAGQueryRequest,
    db: Session = Depends(get_db)
):

    # =====================================================
    # PROCESS WORKFLOW STATE
    # =====================================================

    WorkflowStateManager.process_message(
        db=db,
        ticket_id=request.ticket_id,
        user_message=request.question
    )

    # =====================================================
    # BUILD WORKFLOW CONTEXT
    # =====================================================

    context = (
        WorkflowContextBuilder.build_context(
            db=db,
            ticket_id=request.ticket_id,
            question=request.question
        )
    )

    # =====================================================
    # GENERATE RAG RESPONSE
    # =====================================================

    result = (
        RAGService.query_knowledge_base(

            question=request.question,

            conversation_memory=
            context.get(
                "conversation_memory",
                ""
            ),

            workflow_context=
            context.get(
                "workflow_context",
                ""
            ),

            workflow_guidance=
            context.get(
                "workflow_guidance",
                ""
            ),

            workflow_actions=
            context.get(
                "workflow_actions",
                ""
            ),

            workflow_lifecycle_context=
            context.get(
                "workflow_lifecycle_context",
                ""
            ),

            historical_memory=
            context.get(
                "historical_memory",
                ""
            ),

            next_troubleshooting_action=
            context.get(
                "next_troubleshooting_action",
                ""
            )
        )
    )

    return result