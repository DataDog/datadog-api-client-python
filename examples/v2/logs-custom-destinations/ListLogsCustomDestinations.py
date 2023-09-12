"""
List custom destinations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi

configuration = Configuration()
configuration.unstable_operations["list_logs_custom_destinations"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.list_logs_custom_destinations()

    print(response)
