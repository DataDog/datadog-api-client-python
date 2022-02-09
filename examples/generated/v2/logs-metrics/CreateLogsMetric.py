import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)
    body = LogsMetricCreateRequest(
        data=LogsMetricCreateData(
            attributes=LogsMetricCreateAttributes(
                compute=LogsMetricCompute(
                    aggregation_type=LogsMetricComputeAggregationType("distribution"),
                    path="@duration",
                ),
                filter=LogsMetricFilter(
                    query="service:web* AND @http.status_code:[200 TO 299]",
                ),
                group_by=[
                    LogsMetricGroupBy(
                        path="@http.status_code",
                        tag_name="status_code",
                    ),
                ],
            ),
            id="logs.page.load.count",
            type=LogsMetricType("logs_metrics"),
        ),
    )  # LogsMetricCreateRequest | The definition of the new log-based metric.

    # example passing only required values which don't have defaults set
    try:
        # Create a log-based metric
        api_response = api_instance.create_logs_metric(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->create_logs_metric: %s\n" % e)
