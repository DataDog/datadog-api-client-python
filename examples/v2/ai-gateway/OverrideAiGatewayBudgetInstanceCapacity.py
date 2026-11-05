"""
Override a budget instance's capacity returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_budget_instance_capacity_override_attributes import (
    AiGatewayBudgetInstanceCapacityOverrideAttributes,
)
from datadog_api_client.v2.model.ai_gateway_budget_instance_capacity_override_data import (
    AiGatewayBudgetInstanceCapacityOverrideData,
)
from datadog_api_client.v2.model.ai_gateway_budget_instance_capacity_override_request import (
    AiGatewayBudgetInstanceCapacityOverrideRequest,
)
from datadog_api_client.v2.model.ai_gateway_budget_instance_type import AiGatewayBudgetInstanceType
from uuid import UUID

body = AiGatewayBudgetInstanceCapacityOverrideRequest(
    data=AiGatewayBudgetInstanceCapacityOverrideData(
        attributes=AiGatewayBudgetInstanceCapacityOverrideAttributes(
            capacity_microcents=250000000,
            instance_key="v1|7:user_id=36:22222222-2222-2222-2222-222222222222",
            reason="Temporary increase for a launch week",
        ),
        type=AiGatewayBudgetInstanceType.BUDGET_INSTANCES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["override_ai_gateway_budget_instance_capacity"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.override_ai_gateway_budget_instance_capacity(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
