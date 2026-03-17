"""
List integration accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    response = api_instance.list_web_integration_accounts(
        integration_name="twilio",
    )

    print(response)
