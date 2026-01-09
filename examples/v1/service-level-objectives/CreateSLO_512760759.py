"""
Create a new metric SLO object using sli_specification returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_count_definition import SLOCountDefinition
from datadog_api_client.v1.model.slo_count_spec import SLOCountSpec
from datadog_api_client.v1.model.slo_formula import SLOFormula
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

body = ServiceLevelObjectiveRequest(
    type=SLOType.METRIC,
    description="Metric SLO using sli_specification",
    name="Example-Service-Level-Objective",
    sli_specification=SLOCountSpec(
        count=SLOCountDefinition(
            good_events_formula=SLOFormula(
                formula="query1 - query2",
            ),
            total_events_formula=SLOFormula(
                formula="query1",
            ),
            queries=[
                FormulaAndFunctionMetricQueryDefinition(
                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                    name="query1",
                    query="sum:httpservice.hits{*}.as_count()",
                ),
                FormulaAndFunctionMetricQueryDefinition(
                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                    name="query2",
                    query="sum:httpservice.errors{*}.as_count()",
                ),
            ],
        ),
    ),
    tags=[
        "env:prod",
        "type:count",
    ],
    thresholds=[
        SLOThreshold(
            target=99.0,
            target_display="99.0",
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=99.5,
            warning_display="99.5",
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=99.0,
    warning_threshold=99.5,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo(body=body)

    print(response)
