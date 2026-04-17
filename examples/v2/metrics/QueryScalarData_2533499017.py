"""
Scalar cross product query with apm_dependency_stats data source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.apm_dependency_stat_name import ApmDependencyStatName
from datadog_api_client.v2.model.apm_dependency_stats_data_source import ApmDependencyStatsDataSource
from datadog_api_client.v2.model.apm_dependency_stats_query import ApmDependencyStatsQuery
from datadog_api_client.v2.model.formula_limit import FormulaLimit
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
            _from=1636625471000,
            queries=ScalarFormulaRequestQueries(
                [
                    ApmDependencyStatsQuery(
                        data_source=ApmDependencyStatsDataSource.APM_DEPENDENCY_STATS,
                        name="a",
                        env="ci",
                        service="cassandra",
                        stat=ApmDependencyStatName.AVG_DURATION,
                        operation_name="cassandra.query",
                        resource_name="DELETE FROM monitor_history.monitor_state_change_history WHERE org_id = ? AND monitor_id IN ? AND group = ?",
                        primary_tag_name="datacenter",
                        primary_tag_value="edge-eu1.prod.dog",
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
