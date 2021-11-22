"""
Create a log-based metric returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_metric_compute_aggregation_type import LogsMetricComputeAggregationType
from datadog_api_client.v2.model.logs_metric_create_attributes import LogsMetricCreateAttributes
from datadog_api_client.v2.model.logs_metric_create_data import LogsMetricCreateData
from datadog_api_client.v2.model.logs_metric_create_request import LogsMetricCreateRequest
from datadog_api_client.v2.model.logs_metric_id import LogsMetricID
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType

body = LogsMetricCreateRequest(
    data=LogsMetricCreateData(
        id=LogsMetricID("Example-Create_a_log_based_metric_returns_OK_response"),
        type=LogsMetricType("logs_metrics"),
        attributes=LogsMetricCreateAttributes(
            compute=LogsMetricCompute(aggregation_type=LogsMetricComputeAggregationType("count"))
        ),
    )
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.create_logs_metric(body=body)

    print(response)
