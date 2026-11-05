"""
Archive an AI Gateway budget returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_ai_gateway_budget"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    api_instance.delete_ai_gateway_budget(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
