"""
Delete an Azure integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi
from datadog_api_client.v1.model.azure_account import AzureAccount

body = AzureAccount(
    app_service_plan_filters="key:value,filter:example",
    automute=True,
    client_id="testc7f6-1234-5678-9101-3fcbf464test",
    client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
    cspm_enabled=True,
    custom_metrics_enabled=True,
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
    new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
    tenant_name="testc44-1234-5678-9101-cc00736ftest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AzureIntegrationApi(api_client)
    response = api_instance.delete_azure_integration(body=body)

    print(response)
