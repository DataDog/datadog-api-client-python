"""
Scalar cross product query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.formula_limit import FormulaLimit
from datadog_api_client.v2.model.metrics_aggregator import MetricsAggregator
from datadog_api_client.v2.model.metrics_data_source import MetricsDataSource
from datadog_api_client.v2.model.metrics_scalar_query import MetricsScalarQuery
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.scalar_formula_query_request import ScalarFormulaQueryRequest
from datadog_api_client.v2.model.scalar_formula_request import ScalarFormulaRequest
from datadog_api_client.v2.model.scalar_formula_request_attributes import ScalarFormulaRequestAttributes
from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries
from datadog_api_client.v2.model.scalar_formula_request_type import ScalarFormulaRequestType

body = ScalarFormulaQueryRequest(
    data=ScalarFormulaRequest(
        attributes=ScalarFormulaRequestAttributes(
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
            queries=ScalarFormulaRequestQueries(
                [
                    MetricsScalarQuery(
                        aggregator=MetricsAggregator.AVG,
                        data_source=MetricsDataSource.METRICS,
                        query="avg:system.cpu.user{*}",
                        name="a",
                    ),
                ]
            ),
            to=1671620004000,
        ),
        type=ScalarFormulaRequestType.SCALAR_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_scalar_data"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_scalar_data(body=body)

    print(response)
