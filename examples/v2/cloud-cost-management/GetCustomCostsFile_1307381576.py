"""
Get Custom Costs File returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_custom_costs_file(
        file_id="9d055d22-a838-4e9f-bc34-a4f9ab66280c",
    )

    print(response)
