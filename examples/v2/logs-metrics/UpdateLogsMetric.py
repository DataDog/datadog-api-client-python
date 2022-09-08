"""
Update a log-based metric returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType
from datadog_api_client.v2.model.logs_metric_update_attributes import LogsMetricUpdateAttributes
from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData
from datadog_api_client.v2.model.logs_metric_update_request import LogsMetricUpdateRequest

# there is a valid "logs_metric" in the system
LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY = environ["LOGS_METRIC_DATA_ATTRIBUTES_FILTER_QUERY"]
LOGS_METRIC_DATA_ID = environ["LOGS_METRIC_DATA_ID"]

body = LogsMetricUpdateRequest(
    data=LogsMetricUpdateData(
        type=LogsMetricType.LOGS_METRICS,
        attributes=LogsMetricUpdateAttributes(
            filter=LogsMetricFilter(
                query="service:web* AND @http.status_code:[200 TO 299]-updated",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.update_logs_metric(metric_id=LOGS_METRIC_DATA_ID, body=body)

    print(response)
