"""
Delete integration account returns "OK: The account was successfully deleted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    api_instance.delete_web_integration_account(
        integration_name="integration_name",
        account_id="account_id",
    )
