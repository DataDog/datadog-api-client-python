"""
Get the Governance Console configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_console_api import GovernanceConsoleApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_governance_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceConsoleApi(api_client)
    response = api_instance.get_governance_config()

    print(response)
