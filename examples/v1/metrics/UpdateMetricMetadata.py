"""
Edit metric metadata returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metric_metadata import MetricMetadata

body = MetricMetadata(
    description="Number of requests received.",
    per_unit="second",
    short_name="requests",
    statsd_interval=10,
    type="count",
    unit="byte",
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_metric_metadata(metric_name="metric_name", body=body)

    print(response)
