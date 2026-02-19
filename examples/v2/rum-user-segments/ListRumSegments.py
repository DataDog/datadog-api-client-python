"""
List all RUM segments returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_user_segments_api import RUMUserSegmentsApi

configuration = Configuration()
configuration.unstable_operations["list_rum_segments"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMUserSegmentsApi(api_client)
    response = api_instance.list_rum_segments()

    print(response)
