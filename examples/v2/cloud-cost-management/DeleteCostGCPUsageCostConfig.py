"""
Delete Cloud Cost Management GCP Usage Cost config returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_cost_gcp_usage_cost_config(
        cloud_account_id="100",
    )
