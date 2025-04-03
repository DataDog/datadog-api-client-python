"""
Get aggregated connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_network_monitoring_api import CloudNetworkMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_aggregated_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudNetworkMonitoringApi(api_client)
    response = api_instance.get_aggregated_connections()

    print(response)
