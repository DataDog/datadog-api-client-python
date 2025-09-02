"""
Create Cloud Cost Management GCP Usage Cost config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.gcp_usage_cost_config_post_data import GCPUsageCostConfigPostData
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request import GCPUsageCostConfigPostRequest
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_attributes import (
    GCPUsageCostConfigPostRequestAttributes,
)
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_type import GCPUsageCostConfigPostRequestType

body = GCPUsageCostConfigPostRequest(
    data=GCPUsageCostConfigPostData(
        attributes=GCPUsageCostConfigPostRequestAttributes(
            billing_account_id="123456_A123BC_12AB34",
            bucket_name="dd-cost-bucket",
            export_dataset_name="billing",
            export_prefix="datadog_cloud_cost_usage_export",
            export_project_name="dd-cloud-cost-report",
            service_account="dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
        ),
        type=GCPUsageCostConfigPostRequestType.GCP_USAGE_COST_CONFIG_POST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_gcp_usage_cost_config(body=body)

    print(response)
