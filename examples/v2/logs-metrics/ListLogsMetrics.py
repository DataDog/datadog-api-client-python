"""
Get all log-based metrics returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.list_logs_metrics()

    print(response)
