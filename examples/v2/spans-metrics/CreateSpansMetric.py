"""
Create a span-based metric returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi
from datadog_api_client.v2.model.spans_metric_compute import SpansMetricCompute
from datadog_api_client.v2.model.spans_metric_compute_aggregation_type import SpansMetricComputeAggregationType
from datadog_api_client.v2.model.spans_metric_create_attributes import SpansMetricCreateAttributes
from datadog_api_client.v2.model.spans_metric_create_data import SpansMetricCreateData
from datadog_api_client.v2.model.spans_metric_create_request import SpansMetricCreateRequest
from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy
from datadog_api_client.v2.model.spans_metric_type import SpansMetricType

body = SpansMetricCreateRequest(
    data=SpansMetricCreateData(
        attributes=SpansMetricCreateAttributes(
            compute=SpansMetricCompute(
                aggregation_type=SpansMetricComputeAggregationType.DISTRIBUTION,
                include_percentiles=False,
                path="@duration",
            ),
            filter=SpansMetricFilter(
                query="@http.status_code:200 service:my-service",
            ),
            group_by=[
                SpansMetricGroupBy(
                    path="resource_name",
                    tag_name="resource_name",
                ),
            ],
        ),
        id="ExampleSpansMetric",
        type=SpansMetricType.SPANS_METRICS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.create_spans_metric(body=body)

    print(response)
