"""
Update a RUM-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_metrics_api import RUMMetricsApi
from datadog_api_client.v2.model.rum_metric_filter import RUMMetricFilter
from datadog_api_client.v2.model.rum_metric_group_by import RUMMetricGroupBy
from datadog_api_client.v2.model.rum_metric_type import RUMMetricType
from datadog_api_client.v2.model.rum_metric_update_attributes import RUMMetricUpdateAttributes
from datadog_api_client.v2.model.rum_metric_update_compute import RUMMetricUpdateCompute
from datadog_api_client.v2.model.rum_metric_update_data import RUMMetricUpdateData
from datadog_api_client.v2.model.rum_metric_update_request import RUMMetricUpdateRequest

# there is a valid "rum_metric" in the system
RUM_METRIC_DATA_ID = environ["RUM_METRIC_DATA_ID"]

body = RUMMetricUpdateRequest(
    data=RUMMetricUpdateData(
        id=RUM_METRIC_DATA_ID,
        type=RUMMetricType.RUM_METRICS,
        attributes=RUMMetricUpdateAttributes(
            compute=RUMMetricUpdateCompute(
                include_percentiles=False,
            ),
            filter=RUMMetricFilter(
                query="@service:rum-config",
            ),
            group_by=[
                RUMMetricGroupBy(
                    path="@browser.version",
                    tag_name="browser_version",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMMetricsApi(api_client)
    response = api_instance.update_rum_metric(metric_id=RUM_METRIC_DATA_ID, body=body)

    print(response)
