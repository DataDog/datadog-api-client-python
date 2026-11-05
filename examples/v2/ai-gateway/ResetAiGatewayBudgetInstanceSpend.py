"""
Reset a budget instance's spend returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_attributes import (
    AiGatewayBudgetInstanceResetAttributes,
)
from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_data import AiGatewayBudgetInstanceResetData
from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_request import AiGatewayBudgetInstanceResetRequest
from datadog_api_client.v2.model.ai_gateway_budget_instance_type import AiGatewayBudgetInstanceType
from uuid import UUID

body = AiGatewayBudgetInstanceResetRequest(
    data=AiGatewayBudgetInstanceResetData(
        attributes=AiGatewayBudgetInstanceResetAttributes(
            instance_key="v1|7:user_id=36:22222222-2222-2222-2222-222222222222",
            reason="Credit approved after incorrect usage attribution",
        ),
        type=AiGatewayBudgetInstanceType.BUDGET_INSTANCES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["reset_ai_gateway_budget_instance_spend"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.reset_ai_gateway_budget_instance_spend(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
