"""
Get a failure event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.get_dora_failure(
        failure_id="failure_id",
    )

    print(response)
