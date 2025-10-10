"""
Delete tag pipeline ruleset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_tag_pipelines_ruleset(
        ruleset_id="ee10c3ff-312f-464c-b4f6-46adaa6d00a1",
    )
