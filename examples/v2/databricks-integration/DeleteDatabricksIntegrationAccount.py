"""
Delete a Databricks integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.databricks_integration_api import DatabricksIntegrationApi

configuration = Configuration()
configuration.unstable_operations["delete_databricks_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatabricksIntegrationApi(api_client)
    api_instance.delete_databricks_integration_account(
        account_id="account_id",
    )
