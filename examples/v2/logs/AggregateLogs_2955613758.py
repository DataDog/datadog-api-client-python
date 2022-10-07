"""
Aggregate compute events with group by returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest
from datadog_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort
from datadog_api_client.v2.model.logs_aggregate_sort_type import LogsAggregateSortType
from datadog_api_client.v2.model.logs_aggregation_function import LogsAggregationFunction
from datadog_api_client.v2.model.logs_compute import LogsCompute
from datadog_api_client.v2.model.logs_compute_type import LogsComputeType
from datadog_api_client.v2.model.logs_group_by import LogsGroupBy
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_sort_order import LogsSortOrder

body = LogsAggregateRequest(
    compute=[
        LogsCompute(
            aggregation=LogsAggregationFunction.COUNT,
            interval="5m",
            type=LogsComputeType.TIMESERIES,
        ),
    ],
    filter=LogsQueryFilter(
        _from="now-15m",
        indexes=[
            "main",
        ],
        query="*",
        to="now",
    ),
    group_by=[
        LogsGroupBy(
            facet="host",
            missing="miss",
            sort=LogsAggregateSort(
                type=LogsAggregateSortType.MEASURE,
                order=LogsSortOrder.ASCENDING,
                aggregation=LogsAggregationFunction.PERCENTILE_90,
                metric="@duration",
            ),
            total="recall",
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.aggregate_logs(body=body)

    print(response)
