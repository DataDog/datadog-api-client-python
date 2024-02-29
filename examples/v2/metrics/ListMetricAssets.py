"""
Related Assets to a Metric returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_metric_assets(
        metric_name="system.cpu.user",
    )

    print(response)
