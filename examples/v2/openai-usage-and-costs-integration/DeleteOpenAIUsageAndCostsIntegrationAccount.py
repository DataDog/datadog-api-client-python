"""
Delete an OpenAI Usage and Costs account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_usageand_costs_integration_api import OpenAIUsageandCostsIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_open_ai_usage_and_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAIUsageandCostsIntegrationApi(api_client)
    api_instance.delete_open_ai_usage_and_costs_integration_account(
        account_id="account_id",
    )
