"""
Get a span-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ID = environ["SPANS_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.get_spans_metric(
        metric_id=SPANS_METRIC_DATA_ID,
    )

    print(response)
