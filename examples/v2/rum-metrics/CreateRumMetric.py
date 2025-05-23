"""
Create a rum-based metric returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi
from datadog_api_client.v2.model.rum_metric_compute import RumMetricCompute
from datadog_api_client.v2.model.rum_metric_compute_aggregation_type import RumMetricComputeAggregationType
from datadog_api_client.v2.model.rum_metric_create_attributes import RumMetricCreateAttributes
from datadog_api_client.v2.model.rum_metric_create_data import RumMetricCreateData
from datadog_api_client.v2.model.rum_metric_create_request import RumMetricCreateRequest
from datadog_api_client.v2.model.rum_metric_event_type import RumMetricEventType
from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy
from datadog_api_client.v2.model.rum_metric_type import RumMetricType
from datadog_api_client.v2.model.rum_metric_uniqueness import RumMetricUniqueness
from datadog_api_client.v2.model.rum_metric_uniqueness_when import RumMetricUniquenessWhen

body = RumMetricCreateRequest(
    data=RumMetricCreateData(
        attributes=RumMetricCreateAttributes(
            compute=RumMetricCompute(
                aggregation_type=RumMetricComputeAggregationType.DISTRIBUTION,
                include_percentiles=True,
                path="@duration",
            ),
            event_type=RumMetricEventType.SESSION,
            filter=RumMetricFilter(
                query="@service:web-ui",
            ),
            group_by=[
                RumMetricGroupBy(
                    path="@browser.name",
                    tag_name="browser_name",
                ),
            ],
            uniqueness=RumMetricUniqueness(
                when=RumMetricUniquenessWhen.WHEN_MATCH,
            ),
        ),
        id="examplerummetric",
        type=RumMetricType.RUM_METRICS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.create_rum_metric(body=body)

    print(response)
