"""
Delete a rum-based metric returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = environ["RUM_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    api_instance.delete_rum_metric(
        metric_id=RUM_METRIC_DATA_ID,
    )
