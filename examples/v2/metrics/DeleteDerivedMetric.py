"""
Delete a derived metric returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

# there is a valid "derived_metric" in the system
DERIVED_METRIC_DATA_ID = environ["DERIVED_METRIC_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    api_instance.delete_derived_metric(
        metric_name=DERIVED_METRIC_DATA_ID,
    )
