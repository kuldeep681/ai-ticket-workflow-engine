from fastapi import APIRouter
from pydantic import BaseModel

from app.services.classification_service import (
    ClassificationService
)

# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"]
)

# =========================================================
# REQUEST SCHEMA
# =========================================================

class ClassificationRequest(BaseModel):
    text: str

# =========================================================
# CLASSIFICATION ENDPOINT
# =========================================================

@router.post("/classify")
def classify_ticket(request: ClassificationRequest):

    result = ClassificationService.classify_ticket(
        request.text
    )

    return result