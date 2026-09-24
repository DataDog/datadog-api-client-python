"""
Edit metric metadata returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metric_metadata import MetricMetadata

body = MetricMetadata(
    per_unit="second",
    type="count",
    unit="byte",
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_metric_metadata(metric_name="metric_name", body=body)

    print(response)
