"""
Update an AI Gateway provider returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType
from datadog_api_client.v2.model.ai_gateway_provider_update_attributes import AiGatewayProviderUpdateAttributes
from datadog_api_client.v2.model.ai_gateway_provider_update_data import AiGatewayProviderUpdateData
from datadog_api_client.v2.model.ai_gateway_provider_update_request import AiGatewayProviderUpdateRequest

body = AiGatewayProviderUpdateRequest(
    data=AiGatewayProviderUpdateData(
        attributes=AiGatewayProviderUpdateAttributes(
            cost_multiplier=1.0,
            name="production-us-v2",
        ),
        id="42",
        type=AiGatewayProviderType.PROVIDERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_provider"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_provider(id=9223372036854775807, body=body)

    print(response)
