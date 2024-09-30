"""
Upload Custom Costs file returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.custom_costs_file_line_item import CustomCostsFileLineItem

body = [
    CustomCostsFileLineItem(
        billed_cost=100.5,
        billing_currency="USD",
        charge_description="Monthly usage charge for my service",
        charge_period_end="2023-02-28",
        charge_period_start="2023-02-01",
    ),
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.upload_custom_costs_file(body=body)

    print(response)
