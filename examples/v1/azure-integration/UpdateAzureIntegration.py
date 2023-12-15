"""
Update an Azure integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount

body = AzureAccount(
    app_service_plan_filters="key:value,filter:example",
    automute=True,
    client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
    container_app_filters="key:value,filter:example",
    cspm_enabled=True,
    custom_metrics_enabled=True,
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    new_client_id="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    new_tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
    resource_collection_enabled=True,
    tenant_name="9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.update_azure_integration(body=body)

    print(response)
