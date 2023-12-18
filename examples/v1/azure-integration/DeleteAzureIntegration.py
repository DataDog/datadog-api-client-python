"""
Delete an Azure integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount

body = AzureAccount(
    client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.delete_azure_integration(body=body)

    print(response)
