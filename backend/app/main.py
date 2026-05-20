from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.api.routes.ml_routes import router as ml_router

from app.database.init_db import init_db

from app.api.routes.health_routes import (
    router as health_router
)

from app.api.routes.ai_routes import (
    router as ai_router
)

from app.api.routes.workflow_routes import (
    router as workflow_router
)

from app.api.routes.ticket_routes import (
    router as ticket_router
)

from app.api.routes.conversation_routes import (
    router as conversation_router
)

from app.api.routes.document_routes import (
    router as document_router
)

from app.api.routes.rag_routes import (
    router as rag_router
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Register routes
app.include_router(health_router)
app.include_router(ticket_router)
app.include_router(conversation_router)
app.include_router(workflow_router)
app.include_router(ai_router)
app.include_router(ml_router)
app.include_router(document_router)
app.include_router(rag_router)

@app.get("/")
def root():
    return {
        "success": True,
        "message": f"{settings.APP_NAME} API is running"
    }