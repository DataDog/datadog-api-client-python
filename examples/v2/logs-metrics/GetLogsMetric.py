"""
Get a log-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ID = environ["LOGS_METRIC_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.get_logs_metric(
        metric_id=LOGS_METRIC_DATA_ID,
    )

    print(response)
