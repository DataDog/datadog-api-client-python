"""
List integration accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_integration_id import IntegrationAccountIntegrationId
from datadog_api_client.v2.model.integration_account_interface_id import IntegrationAccountInterfaceId

configuration = Configuration()
configuration.unstable_operations["list_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    response = api_instance.list_integration_accounts(
        integration_id=IntegrationAccountIntegrationId.TWILIO,
        interface_id=IntegrationAccountInterfaceId.TWILIO,
    )

    print(response)
