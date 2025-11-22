"""
Initialize rum segments returns "Default segments created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.segments_api import SegmentsApi

configuration = Configuration()
configuration.unstable_operations["initialize_rum_segments"] = True
with ApiClient(configuration) as api_client:
    api_instance = SegmentsApi(api_client)
    api_instance.initialize_rum_segments()
