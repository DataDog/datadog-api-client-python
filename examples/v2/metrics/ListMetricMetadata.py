"""
List metadata for multiple metrics returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_metric_metadata"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_metric_metadata(
        filter_metric_name="static_test_metric_donotdelete,static_test_metric_donotdelete,not.a.real.metric.examplemetric",
    )

    print(response)
