"""
Upload Custom Costs File returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.custom_costs_file_line_item import CustomCostsFileLineItem

body = [
    CustomCostsFileLineItem(
        provider_name="my_provider",
        charge_period_start="2023-05-06",
        charge_period_end="2023-06-06",
        charge_description="my_description",
        billed_cost=250.0,
        billing_currency="USD",
        tags=dict(
            key="value",
        ),
    ),
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.upload_custom_costs_file(body=body)

    print(response)
