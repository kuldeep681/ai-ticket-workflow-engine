from app.services.priority_service import (
    PriorityService
)

sample_ticket = "Entire office network is down"

result = PriorityService.predict_priority(
    sample_ticket
)

print(result)