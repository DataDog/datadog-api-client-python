"""
Update an AI Gateway budget returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement
from datadog_api_client.v2.model.ai_gateway_budget_type import AiGatewayBudgetType
from datadog_api_client.v2.model.ai_gateway_budget_update_attributes import AiGatewayBudgetUpdateAttributes
from datadog_api_client.v2.model.ai_gateway_budget_update_data import AiGatewayBudgetUpdateData
from datadog_api_client.v2.model.ai_gateway_budget_update_request import AiGatewayBudgetUpdateRequest
from uuid import UUID

body = AiGatewayBudgetUpdateRequest(
    data=AiGatewayBudgetUpdateData(
        attributes=AiGatewayBudgetUpdateAttributes(
            apply_to_current_period=False,
            capacity_microcents=120000000,
            enabled=True,
            enforcement=AiGatewayBudgetEnforcement.BLOCK,
            name="Coding agents",
            reason="Temporary capacity increase approved for an incident",
            track_existing=False,
            warning_threshold=0.8,
        ),
        id=UUID("11111111-1111-1111-1111-111111111111"),
        type=AiGatewayBudgetType.BUDGETS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_budget"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_budget(id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
