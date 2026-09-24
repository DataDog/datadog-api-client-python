"""
List network health insights returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_health_insights_api import NetworkHealthInsightsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_network_health_insights"] = True
with ApiClient(configuration) as api_client:
    api_instance = NetworkHealthInsightsApi(api_client)
    response = api_instance.list_network_health_insights()

    print(response)
