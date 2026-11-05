"""
Create an AI Gateway rate limit returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_rate_limit_create_attributes import AiGatewayRateLimitCreateAttributes
from datadog_api_client.v2.model.ai_gateway_rate_limit_create_data import AiGatewayRateLimitCreateData
from datadog_api_client.v2.model.ai_gateway_rate_limit_create_request import AiGatewayRateLimitCreateRequest
from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode
from datadog_api_client.v2.model.ai_gateway_rate_limit_type import AiGatewayRateLimitType
from uuid import UUID

body = AiGatewayRateLimitCreateRequest(
    data=AiGatewayRateLimitCreateData(
        attributes=AiGatewayRateLimitCreateAttributes(
            input_tokens_per_minute=None,
            mode=AiGatewayRateLimitMode.ALERT,
            name="Default rate limit",
            output_tokens_per_minute=None,
            requests_per_minute=600,
            team_id=UUID("00000000-0000-4000-8000-000000000002"),
            user_id=UUID("00000000-0000-4000-8000-000000000001"),
        ),
        type=AiGatewayRateLimitType.RATE_LIMITS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_gateway_rate_limit"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.create_ai_gateway_rate_limit(body=body)

    print(response)
