"""
List Databricks integration accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.databricks_integration_accounts_api import DatabricksIntegrationAccountsApi

configuration = Configuration()
configuration.unstable_operations["list_databricks_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatabricksIntegrationAccountsApi(api_client)
    response = api_instance.list_databricks_integration_accounts()

    print(response)
