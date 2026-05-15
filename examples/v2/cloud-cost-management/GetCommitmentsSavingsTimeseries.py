"""
Get commitments savings (timeseries) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.commitments_provider import CommitmentsProvider

configuration = Configuration()
configuration.unstable_operations["get_commitments_savings_timeseries"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_commitments_savings_timeseries(
        provider=CommitmentsProvider.AWS,
        product="product",
        start=9223372036854775807,
        end=9223372036854775807,
    )

    print(response)
