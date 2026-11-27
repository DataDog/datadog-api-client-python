"""
List OpenAI Usage and Costs accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_usage_and_costs_integration_api import OpenAIUsageAndCostsIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_open_ai_usage_and_costs_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAIUsageAndCostsIntegrationApi(api_client)
    response = api_instance.list_open_ai_usage_and_costs_integration_accounts()

    print(response)
