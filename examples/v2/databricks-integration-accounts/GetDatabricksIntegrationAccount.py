"""
Get a Databricks integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.databricks_integration_accounts_api import DatabricksIntegrationAccountsApi

configuration = Configuration()
configuration.unstable_operations["get_databricks_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatabricksIntegrationAccountsApi(api_client)
    response = api_instance.get_databricks_integration_account(
        account_id="account_id",
    )

    print(response)
