"""
Get cost anomaly returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
configuration.unstable_operations["get_cost_anomaly"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_cost_anomaly(
        anomaly_id="anomaly_id",
    )

    print(response)
