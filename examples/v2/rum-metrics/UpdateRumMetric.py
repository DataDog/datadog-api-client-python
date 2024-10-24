"""
Update a rum-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RumMetricsApi
from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy
from datadog_api_client.v2.model.rum_metric_type import RumMetricType
from datadog_api_client.v2.model.rum_metric_update_attributes import RumMetricUpdateAttributes
from datadog_api_client.v2.model.rum_metric_update_compute import RumMetricUpdateCompute
from datadog_api_client.v2.model.rum_metric_update_data import RumMetricUpdateData
from datadog_api_client.v2.model.rum_metric_update_request import RumMetricUpdateRequest

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = environ["RUM_METRIC_DATA_ID"]

body = RumMetricUpdateRequest(
    data=RumMetricUpdateData(
        id=RUM_METRIC_DATA_ID,
        type=RumMetricType.RUM_METRICS,
        attributes=RumMetricUpdateAttributes(
            compute=RumMetricUpdateCompute(
                include_percentiles=False,
            ),
            filter=RumMetricFilter(
                query="@service:rum-config",
            ),
            group_by=[
                RumMetricGroupBy(
                    path="@browser.version",
                    tag_name="browser_version",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumMetricsApi(api_client)
    response = api_instance.update_rum_metric(metric_id=RUM_METRIC_DATA_ID, body=body)

    print(response)
