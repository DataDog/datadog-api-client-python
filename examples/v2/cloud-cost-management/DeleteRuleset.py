"""
Delete ruleset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_ruleset(
        ruleset_id="1c5dae14-237d-4b9a-a515-aa55b3939142",
    )
