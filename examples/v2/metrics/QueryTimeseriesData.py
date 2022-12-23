"""
Timeseries cross product query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.formula_limit import FormulaLimit
from datadog_api_client.v2.model.metrics_data_source import MetricsDataSource
from datadog_api_client.v2.model.metrics_timeseries_query import MetricsTimeseriesQuery
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
            _from=1671612804000,
            interval=5000,
            queries=TimeseriesFormulaRequestQueries(
                [
                    MetricsTimeseriesQuery(
                        data_source=MetricsDataSource.METRICS,
                        query="avg:system.cpu.user{*}",
                        name="a",
                    ),
                ]
            ),
            to=1671620004000,
        ),
        type=TimeseriesFormulaRequestType.TIMESERIES_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_timeseries_data"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_timeseries_data(body=body)

    print(response)
