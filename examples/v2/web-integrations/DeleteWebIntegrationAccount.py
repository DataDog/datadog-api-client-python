"""
Delete a web integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi

configuration = Configuration()
configuration.unstable_operations["delete_web_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    api_instance.delete_web_integration_account(
        integration_name="integration_name",
        account_id="account_id",
    )
