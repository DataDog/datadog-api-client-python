"""
List network health insights returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_health_insights_api import NetworkHealthInsightsApi

configuration = Configuration()
configuration.unstable_operations["list_network_health_insights"] = True
with ApiClient(configuration) as api_client:
    api_instance = NetworkHealthInsightsApi(api_client)
    response = api_instance.list_network_health_insights()

    print(response)
