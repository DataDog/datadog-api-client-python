# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.host_map_widget_formula import HostMapWidgetFormula
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.host_map_widget_scalar_request_response_format import (
        HostMapWidgetScalarRequestResponseFormat,
    )
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


class HostMapWidgetScalarRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_map_widget_formula import HostMapWidgetFormula
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.host_map_widget_scalar_request_response_format import (
            HostMapWidgetScalarRequestResponseFormat,
        )

        return {
            "formulas": ([HostMapWidgetFormula],),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (HostMapWidgetScalarRequestResponseFormat,),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        formulas: List[HostMapWidgetFormula],
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
        response_format: HostMapWidgetScalarRequestResponseFormat,
        **kwargs,
    ):
        """
        Scalar formula request for the infrastructure host map widget. Each formula specifies
        which visual dimension it drives.

        :param formulas: List of formulas that operate on queries, each assigned to a visual dimension.
        :type formulas: [HostMapWidgetFormula]

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Response format for the scalar formula request. Only ``scalar`` is supported.
        :type response_format: HostMapWidgetScalarRequestResponseFormat
        """
        super().__init__(kwargs)

        self_.formulas = formulas
        self_.queries = queries
        self_.response_format = response_format
