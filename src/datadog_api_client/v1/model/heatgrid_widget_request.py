# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.heatgrid_widget_formula import HeatgridWidgetFormula
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.heatgrid_widget_response_format import HeatgridWidgetResponseFormat
    from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
        FormulaAndFunctionMetricQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_event_query_definition import (
        FormulaAndFunctionEventQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_process_query_definition import (
        FormulaAndFunctionProcessQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_dependency_stats_query_definition import (
        FormulaAndFunctionApmDependencyStatsQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_resource_stats_query_definition import (
        FormulaAndFunctionApmResourceStatsQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_metrics_query_definition import (
        FormulaAndFunctionApmMetricsQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_slo_query_definition import (
        FormulaAndFunctionSLOQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_cloud_cost_query_definition import (
        FormulaAndFunctionCloudCostQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_product_analytics_extended_query_definition import (
        FormulaAndFunctionProductAnalyticsExtendedQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_user_journey_query_definition import (
        FormulaAndFunctionUserJourneyQueryDefinition,
    )
    from datadog_api_client.v1.model.formula_and_function_retention_query_definition import (
        FormulaAndFunctionRetentionQueryDefinition,
    )


class HeatgridWidgetRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_widget_formula import HeatgridWidgetFormula
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.heatgrid_widget_response_format import HeatgridWidgetResponseFormat

        return {
            "formulas": ([HeatgridWidgetFormula],),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (HeatgridWidgetResponseFormat,),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        queries: List[
            Union[
                FormulaAndFunctionQueryDefinition,
                FormulaAndFunctionMetricQueryDefinition,
                FormulaAndFunctionEventQueryDefinition,
                FormulaAndFunctionProcessQueryDefinition,
                FormulaAndFunctionApmDependencyStatsQueryDefinition,
                FormulaAndFunctionApmResourceStatsQueryDefinition,
                FormulaAndFunctionApmMetricsQueryDefinition,
                FormulaAndFunctionSLOQueryDefinition,
                FormulaAndFunctionCloudCostQueryDefinition,
                FormulaAndFunctionProductAnalyticsExtendedQueryDefinition,
                FormulaAndFunctionUserJourneyQueryDefinition,
                FormulaAndFunctionRetentionQueryDefinition,
            ]
        ],
        response_format: HeatgridWidgetResponseFormat,
        formulas: Union[List[HeatgridWidgetFormula], UnsetType] = unset,
        **kwargs,
    ):
        """
        A request for a heatgrid widget that uses formulas and functions.

        :param formulas: The single displayed formula can combine multiple queries.
        :type formulas: [HeatgridWidgetFormula], optional

        :param queries: Queries returned directly or combined in a formula.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Response format for heatgrid queries.
        :type response_format: HeatgridWidgetResponseFormat
        """
        if formulas is not unset:
            kwargs["formulas"] = formulas
        super().__init__(kwargs)

        self_.queries = queries
        self_.response_format = response_format
