"""
Create a log-based metric returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_metric_compute_aggregation_type import LogsMetricComputeAggregationType
from datadog_api_client.v2.model.logs_metric_create_request import LogsMetricCreateRequestJSON

body = LogsMetricCreateRequestJSON(
    compute=LogsMetricCompute(
        aggregation_type=LogsMetricComputeAggregationType.DISTRIBUTION,
        include_percentiles=True,
        path="@duration",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.create_logs_metric(body=body)

    print(response)
