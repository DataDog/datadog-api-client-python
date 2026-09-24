"""
Get all span-based metrics returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.list_spans_metrics()

    print(response)
