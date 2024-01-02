"""
Update Cloud Cost Management Azure config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.azure_uc_config_patch_data import AzureUCConfigPatchData
from datadog_api_client.v2.model.azure_uc_config_patch_request import AzureUCConfigPatchRequest
from datadog_api_client.v2.model.azure_uc_config_patch_request_attributes import AzureUCConfigPatchRequestAttributes
from datadog_api_client.v2.model.azure_uc_config_patch_request_type import AzureUCConfigPatchRequestType

body = AzureUCConfigPatchRequest(
    data=AzureUCConfigPatchData(
        attributes=AzureUCConfigPatchRequestAttributes(
            is_enabled=True,
        ),
        type=AzureUCConfigPatchRequestType.AZURE_UC_CONFIG_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_azure_uc_configs(cloud_account_id="100", body=body)

    print(response)
