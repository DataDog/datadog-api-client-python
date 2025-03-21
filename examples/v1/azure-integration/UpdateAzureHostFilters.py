"""
Update Azure integration host filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount
from datadog_api_client.v1.model.resource_provider_config import ResourceProviderConfig

body = AzureAccount(
    app_service_plan_filters="key:value,filter:example",
    automute=True,
    client_id="testc7f6-1234-5678-9101-3fcbf464test",
    client_secret="TestingRh2nx664kUy5dIApvM54T4AtO",
    container_app_filters="key:value,filter:example",
    cspm_enabled=True,
    custom_metrics_enabled=True,
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    metrics_enabled=True,
    metrics_enabled_default=True,
    new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
    new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
    resource_collection_enabled=True,
    resource_provider_configs=[
        ResourceProviderConfig(
            metrics_enabled=True,
            namespace="Microsoft.Compute",
        ),
    ],
    tenant_name="testc44-1234-5678-9101-cc00736ftest",
    usage_metrics_enabled=True,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.update_azure_host_filters(body=body)

    print(response)
