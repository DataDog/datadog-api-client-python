"""
Delete a Claude Compliance integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.claude_compliance_integration_api import ClaudeComplianceIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_claude_compliance_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ClaudeComplianceIntegrationApi(api_client)
    api_instance.delete_claude_compliance_integration_account(
        account_id="account_id",
    )
