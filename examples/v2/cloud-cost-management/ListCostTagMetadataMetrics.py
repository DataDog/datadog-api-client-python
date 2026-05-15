"""
List available Cloud Cost Management metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
configuration.unstable_operations["list_cost_tag_metadata_metrics"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_cost_tag_metadata_metrics(
        filter_month="filter[month]",
    )

    print(response)
