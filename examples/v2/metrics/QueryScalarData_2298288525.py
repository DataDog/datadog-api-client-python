"""
Scalar cross product query with slo data source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.formula_limit import FormulaLimit
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.scalar_formula_query_request import ScalarFormulaQueryRequest
from datadog_api_client.v2.model.scalar_formula_request import ScalarFormulaRequest
from datadog_api_client.v2.model.scalar_formula_request_attributes import ScalarFormulaRequestAttributes
from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries
from datadog_api_client.v2.model.scalar_formula_request_type import ScalarFormulaRequestType
from datadog_api_client.v2.model.slo_data_source import SloDataSource
from datadog_api_client.v2.model.slo_query import SloQuery
from datadog_api_client.v2.model.slos_group_mode import SlosGroupMode
from datadog_api_client.v2.model.slos_measure import SlosMeasure
from datadog_api_client.v2.model.slos_query_type import SlosQueryType

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
            _from=1636625471000,
            queries=ScalarFormulaRequestQueries(
                [
                    SloQuery(
                        data_source=SloDataSource.SLO,
                        name="a",
                        slo_id="12345678910",
                        measure=SlosMeasure.SLO_STATUS,
                        slo_query_type=SlosQueryType.METRIC,
                        group_mode=SlosGroupMode.OVERALL,
                        additional_query_filters="*",
                    ),
                ]
            ),
            to=1636629071000,
        ),
        type=ScalarFormulaRequestType.SCALAR_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_scalar_data(body=body)

    print(response)
