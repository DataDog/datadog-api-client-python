"""
Get a historical metrics configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.unstable_operations["get_historical_metrics_configuration"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.get_historical_metrics_configuration(
        metric_name="metric_name",
    )

    print(response)
