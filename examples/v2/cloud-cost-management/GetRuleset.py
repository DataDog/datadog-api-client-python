"""
Get ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_ruleset(
        ruleset_id="da0e30e2-615d-4dae-9a22-38cf86a87dde",
    )

    print(response)
