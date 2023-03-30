"""
Update a span-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_metrics_api import SpansMetricsApi
from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy
from datadog_api_client.v2.model.spans_metric_type import SpansMetricType
from datadog_api_client.v2.model.spans_metric_update_attributes import SpansMetricUpdateAttributes
from datadog_api_client.v2.model.spans_metric_update_compute import SpansMetricUpdateCompute
from datadog_api_client.v2.model.spans_metric_update_data import SpansMetricUpdateData
from datadog_api_client.v2.model.spans_metric_update_request import SpansMetricUpdateRequest

# there is a valid "spans_metric" in the system
SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY = environ["SPANS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY"]
SPANS_METRIC_DATA_ID = environ["SPANS_METRIC_DATA_ID"]

body = SpansMetricUpdateRequest(
    data=SpansMetricUpdateData(
        attributes=SpansMetricUpdateAttributes(
            compute=SpansMetricUpdateCompute(
                include_percentiles=False,
            ),
            filter=SpansMetricFilter(
                query="@http.status_code:200 service:my-service-updated",
            ),
            group_by=[
                SpansMetricGroupBy(
                    path="resource_name",
                    tag_name="resource_name",
                ),
            ],
        ),
        type=SpansMetricType.SPANS_METRICS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansMetricsApi(api_client)
    response = api_instance.update_spans_metric(metric_id=SPANS_METRIC_DATA_ID, body=body)

    print(response)
