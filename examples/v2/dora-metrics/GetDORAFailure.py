"""
Get an incident event returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.get_dora_failure(
        failure_id="failure_id",
    )

    print(response)
