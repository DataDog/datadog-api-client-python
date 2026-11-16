"""
Update an AI Gateway rate limit returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode
from datadog_api_client.v2.model.ai_gateway_rate_limit_type import AiGatewayRateLimitType
from datadog_api_client.v2.model.ai_gateway_rate_limit_update_attributes import AiGatewayRateLimitUpdateAttributes
from datadog_api_client.v2.model.ai_gateway_rate_limit_update_data import AiGatewayRateLimitUpdateData
from datadog_api_client.v2.model.ai_gateway_rate_limit_update_request import AiGatewayRateLimitUpdateRequest
from uuid import UUID

body = AiGatewayRateLimitUpdateRequest(
    data=AiGatewayRateLimitUpdateData(
        attributes=AiGatewayRateLimitUpdateAttributes(
            cost_microcents_per_minute=None,
            input_tokens_per_minute=None,
            mode=AiGatewayRateLimitMode.ALERT,
            output_tokens_per_minute=None,
            requests_per_minute=None,
            tags=None,
            team_id=None,
            user_id=None,
        ),
        id=UUID("11111111-1111-1111-1111-111111111111"),
        type=AiGatewayRateLimitType.RATE_LIMITS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_rate_limit"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_rate_limit(id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
