"""
Delete an AI Gateway provider returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_ai_gateway_provider"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    api_instance.delete_ai_gateway_provider(
        id=9223372036854775807,
    )
