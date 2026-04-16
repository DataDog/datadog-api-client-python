"""
Timeseries cross product query with apm_resource_stats data source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.apm_resource_stat_name import ApmResourceStatName
from datadog_api_client.v2.model.apm_resource_stats_data_source import ApmResourceStatsDataSource
from datadog_api_client.v2.model.apm_resource_stats_query import ApmResourceStatsQuery
from datadog_api_client.v2.model.formula_limit import FormulaLimit
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.timeseries_formula_query_request import TimeseriesFormulaQueryRequest
from datadog_api_client.v2.model.timeseries_formula_request import TimeseriesFormulaRequest
from datadog_api_client.v2.model.timeseries_formula_request_attributes import TimeseriesFormulaRequestAttributes
from datadog_api_client.v2.model.timeseries_formula_request_queries import TimeseriesFormulaRequestQueries
from datadog_api_client.v2.model.timeseries_formula_request_type import TimeseriesFormulaRequestType

body = TimeseriesFormulaQueryRequest(
    data=TimeseriesFormulaRequest(
        attributes=TimeseriesFormulaRequestAttributes(
            formulas=[
                QueryFormula(
                    formula="a",
                    limit=FormulaLimit(
                        count=10,
                        order=QuerySortOrder.DESC,
                    ),
                ),
            ],
            _from=1636625471000,
            interval=5000,
            queries=TimeseriesFormulaRequestQueries(
                [
                    ApmResourceStatsQuery(
                        data_source=ApmResourceStatsDataSource.APM_RESOURCE_STATS,
                        name="a",
                        env="staging",
                        service="azure-bill-import",
                        stat=ApmResourceStatName.HITS,
                        operation_name="cassandra.query",
                        group_by=[
                            "resource_name",
                        ],
                        primary_tag_name="datacenter",
                        primary_tag_value="*",
                    ),
                ]
            ),
            to=1636629071000,
        ),
        type=TimeseriesFormulaRequestType.TIMESERIES_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_timeseries_data(body=body)

    print(response)
