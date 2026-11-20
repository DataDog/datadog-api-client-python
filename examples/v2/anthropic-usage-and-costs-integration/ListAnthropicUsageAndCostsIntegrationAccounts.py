"""
List Anthropic Usage and Costs accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.anthropic_usage_and_costs_integration_api import AnthropicUsageAndCostsIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_anthropic_usage_and_costs_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnthropicUsageAndCostsIntegrationApi(api_client)
    response = api_instance.list_anthropic_usage_and_costs_integration_accounts()

    print(response)
