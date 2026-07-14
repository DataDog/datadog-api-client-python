"""
Get a budget's custom forecast returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
configuration.unstable_operations["get_custom_forecast"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_custom_forecast(
        budget_id="budget_id",
    )

    print(response)
