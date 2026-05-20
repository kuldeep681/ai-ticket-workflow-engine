from app.services.classification_service import (
    ClassificationService
)

sample_ticket = "VPN not connecting after password reset"

result = ClassificationService.classify_ticket(
    sample_ticket
)

print(result)