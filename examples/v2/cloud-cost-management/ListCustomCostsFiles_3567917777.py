"""
List Custom Costs files with pagination parameters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_custom_costs_files(
        page_number=1,
        page_size=10,
        sort="-created_at",
    )

    print(response)
