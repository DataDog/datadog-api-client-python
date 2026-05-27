"""
List Cloud Cost Management tag metadata months returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
configuration.unstable_operations["list_cost_tag_metadata_months"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_cost_tag_metadata_months(
        filter_provider="filter[provider]",
    )

    print(response)
