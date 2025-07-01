"""
Update Cloud Cost Management GCP Usage Cost config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_data import GCPUsageCostConfigPatchData
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request import GCPUsageCostConfigPatchRequest
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request_attributes import (
    GCPUsageCostConfigPatchRequestAttributes,
)
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request_type import GCPUsageCostConfigPatchRequestType

body = GCPUsageCostConfigPatchRequest(
    data=GCPUsageCostConfigPatchData(
        attributes=GCPUsageCostConfigPatchRequestAttributes(
            is_enabled=True,
        ),
        type=GCPUsageCostConfigPatchRequestType.GCP_USAGE_COST_CONFIG_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_gcp_usage_cost_config(cloud_account_id="100", body=body)

    print(response)
