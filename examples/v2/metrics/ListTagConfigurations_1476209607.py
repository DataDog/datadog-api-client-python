"""
List all metrics with volumes and query activity for metrics not queried in the last 30 days returns "Success" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tag_configurations(
        filter_queried=False,
        include="metric_volumes",
        page_size=100,
    )

    print(response)
