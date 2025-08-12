"""
Delete Custom Costs file returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_custom_costs_file(
        file_id="9ed1a245-8291-44de-9f59-1dc87975ca4a",
    )
