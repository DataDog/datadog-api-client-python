"""
Create Cloud Cost Management Azure configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.azure_uc_config_post_data import AzureUCConfigPostData
from datadog_api_client.v2.model.azure_uc_config_post_request import AzureUCConfigPostRequest
from datadog_api_client.v2.model.azure_uc_config_post_request_attributes import AzureUCConfigPostRequestAttributes
from datadog_api_client.v2.model.azure_uc_config_post_request_type import AzureUCConfigPostRequestType
from datadog_api_client.v2.model.bill_config import BillConfig

body = AzureUCConfigPostRequest(
    data=AzureUCConfigPostData(
        attributes=AzureUCConfigPostRequestAttributes(
            account_id="1234abcd-1234-abcd-1234-1234abcd1234",
            actual_bill_config=BillConfig(
                export_name="dd-actual-export",
                export_path="dd-export-path",
                storage_account="dd-storage-account",
                storage_container="dd-storage-container",
            ),
            amortized_bill_config=BillConfig(
                export_name="dd-actual-export",
                export_path="dd-export-path",
                storage_account="dd-storage-account",
                storage_container="dd-storage-container",
            ),
            client_id="1234abcd-1234-abcd-1234-1234abcd1234",
            is_enabled=True,
            scope="subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
        ),
        type=AzureUCConfigPostRequestType.AZURE_UC_CONFIG_POST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_azure_uc_configs(body=body)

    print(response)
