"""
Get a trace by ID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_trace_api import APMTraceApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_trace_by_id"] = True
with ApiClient(configuration) as api_client:
    api_instance = APMTraceApi(api_client)
    response = api_instance.get_trace_by_id(
        trace_id="trace_id",
    )

    print(response)
