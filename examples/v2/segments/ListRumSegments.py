"""
List rum segments returns "Successful response with list of segments" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.segments_api import SegmentsApi

configuration = Configuration()
configuration.unstable_operations["list_rum_segments"] = True
with ApiClient(configuration) as api_client:
    api_instance = SegmentsApi(api_client)
    response = api_instance.list_rum_segments()

    print(response)
