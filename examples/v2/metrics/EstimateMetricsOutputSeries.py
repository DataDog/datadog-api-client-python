"""
Tag Configuration Cardinality Estimator returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.estimate_metrics_output_series(
        metric_name="system.cpu.idle",
        filter_groups="app,host",
        filter_num_aggregations=4,
    )

    print(response)
