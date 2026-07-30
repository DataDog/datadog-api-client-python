"""
Delete an integration account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_integration_id import IntegrationAccountIntegrationId
from datadog_api_client.v2.model.integration_account_interface_id import IntegrationAccountInterfaceId

configuration = Configuration()
configuration.unstable_operations["delete_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    api_instance.delete_integration_account(
        integration_id=IntegrationAccountIntegrationId.TWILIO,
        interface_id=IntegrationAccountInterfaceId.TWILIO,
        account_id="account_id",
    )
