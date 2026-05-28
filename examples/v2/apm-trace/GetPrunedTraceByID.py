"""
Get a pruned trace by ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_trace_api import APMTraceApi

configuration = Configuration()
configuration.unstable_operations["get_pruned_trace_by_id"] = True
with ApiClient(configuration) as api_client:
    api_instance = APMTraceApi(api_client)
    response = api_instance.get_pruned_trace_by_id(
        trace_id="trace_id",
    )

    print(response)
