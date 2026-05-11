"""
Get a web integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi

configuration = Configuration()
configuration.unstable_operations["get_web_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.get_web_integration_account(
        integration_name="integration_name",
        account_id="account_id",
    )

    print(response)
