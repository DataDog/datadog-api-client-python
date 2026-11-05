"""
Create an AI Gateway budget returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_budget_create_attributes import AiGatewayBudgetCreateAttributes
from datadog_api_client.v2.model.ai_gateway_budget_create_data import AiGatewayBudgetCreateData
from datadog_api_client.v2.model.ai_gateway_budget_create_request import AiGatewayBudgetCreateRequest
from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement
from datadog_api_client.v2.model.ai_gateway_budget_selector_entry import AiGatewayBudgetSelectorEntry
from datadog_api_client.v2.model.ai_gateway_budget_tags import AiGatewayBudgetTags
from datadog_api_client.v2.model.ai_gateway_budget_type import AiGatewayBudgetType
from datadog_api_client.v2.model.ai_gateway_budget_window_policy import AiGatewayBudgetWindowPolicy

body = AiGatewayBudgetCreateRequest(
    data=AiGatewayBudgetCreateData(
        attributes=AiGatewayBudgetCreateAttributes(
            capacity_microcents=100000000,
            enforcement=AiGatewayBudgetEnforcement.BLOCK,
            name="Coding agents",
            selector=[
                AiGatewayBudgetSelectorEntry(
                    dim="user_id",
                    per_value=True,
                    values=[
                        "11111111-1111-1111-1111-111111111111",
                    ],
                ),
            ],
            tags=AiGatewayBudgetTags(
                model="gpt-5.2-codex",
            ),
            track_existing=False,
            warning_threshold=0.9,
            window_policy=AiGatewayBudgetWindowPolicy.MONTHLY,
        ),
        type=AiGatewayBudgetType.BUDGETS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_gateway_budget"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.create_ai_gateway_budget(body=body)

    print(response)
