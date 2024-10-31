"""
Get all rum-based metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.list_rum_metrics()

    print(response)
