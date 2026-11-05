"""
Get an AI Gateway budget instance summary returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_ai_gateway_budget_instances_summary"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.get_ai_gateway_budget_instances_summary(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
