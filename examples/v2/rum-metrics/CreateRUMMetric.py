"""
Create a RUM-based metric returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RUMMetricsApi
from datadog_api_client.v2.model.rum_metric_compute import RUMMetricCompute
from datadog_api_client.v2.model.rum_metric_compute_aggregation_type import RUMMetricComputeAggregationType
from datadog_api_client.v2.model.rum_metric_create_attributes import RUMMetricCreateAttributes
from datadog_api_client.v2.model.rum_metric_create_data import RUMMetricCreateData
from datadog_api_client.v2.model.rum_metric_create_request import RUMMetricCreateRequest
from datadog_api_client.v2.model.rum_metric_event_type import RUMMetricEventType
from datadog_api_client.v2.model.rum_metric_filter import RUMMetricFilter
from datadog_api_client.v2.model.rum_metric_group_by import RUMMetricGroupBy
from datadog_api_client.v2.model.rum_metric_type import RUMMetricType
from datadog_api_client.v2.model.rum_metric_uniqueness import RUMMetricUniqueness
from datadog_api_client.v2.model.rum_metric_uniqueness_when import RUMMetricUniquenessWhen

body = RUMMetricCreateRequest(
    data=RUMMetricCreateData(
        attributes=RUMMetricCreateAttributes(
            compute=RUMMetricCompute(
                aggregation_type=RUMMetricComputeAggregationType.DISTRIBUTION,
                include_percentiles=True,
                path="@duration",
            ),
            event_type=RUMMetricEventType.SESSION,
            filter=RUMMetricFilter(
                query="@service:web-ui",
            ),
            group_by=[
                RUMMetricGroupBy(
                    path="@browser.name",
                    tag_name="browser_name",
                ),
            ],
            uniqueness=RUMMetricUniqueness(
                when=RUMMetricUniquenessWhen.WHEN_MATCH,
            ),
        ),
        id="examplerummetric",
        type=RUMMetricType.RUM_METRICS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMMetricsApi(api_client)
    response = api_instance.create_rum_metric(body=body)

    print(response)
