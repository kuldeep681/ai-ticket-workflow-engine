from app.services.routing_service import (
    RoutingService
)

sample_ticket = "VPN not connecting after password reset"

result = RoutingService.predict_department(
    sample_ticket
)

print(result)