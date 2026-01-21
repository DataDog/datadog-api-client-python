"""
List integration accounts returns "OK: List of all accounts for the specified integration." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.list_web_integration_accounts(
        integration_name="integration_name",
    )

    print(response)
