"""
Create a time-slice SLO object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_formula import SLOFormula
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_time_slice_comparator import SLOTimeSliceComparator
from datadog_api_client.v1.model.slo_time_slice_condition import SLOTimeSliceCondition
from datadog_api_client.v1.model.slo_time_slice_query import SLOTimeSliceQuery
from datadog_api_client.v1.model.slo_time_slice_spec import SLOTimeSliceSpec
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

body = ServiceLevelObjectiveRequest(
    type=SLOType.TIME_SLICE,
    description="string",
    name="Example-Service-Level-Objective",
    sli_specification=SLOTimeSliceSpec(
        time_slice=SLOTimeSliceCondition(
            query=SLOTimeSliceQuery(
                formulas=[
                    SLOFormula(
                        formula="query1",
                    ),
                ],
                queries=[
                    FormulaAndFunctionMetricQueryDefinition(
                        data_source=FormulaAndFunctionMetricDataSource.METRICS,
                        name="query1",
                        query="trace.servlet.request{env:prod}",
                    ),
                ],
            ),
            comparator=SLOTimeSliceComparator.GREATER,
            threshold=5.0,
        ),
    ),
    tags=[
        "env:prod",
    ],
    thresholds=[
        SLOThreshold(
            target=97.0,
            target_display="97.0",
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=98.0,
            warning_display="98.0",
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=97.0,
    warning_threshold=98.0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo(body=body)

    print(response)
