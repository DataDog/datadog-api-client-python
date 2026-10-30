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
    from datadog_api_client.v1.model.widget_formula import WidgetFormula
    from datadog_api_client.v1.model.topology_request_custom_projection import TopologyRequestCustomProjection
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.topology_request_custom_response_format import TopologyRequestCustomResponseFormat
    from datadog_api_client.v1.model.widget_sort_by import WidgetSortBy
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


class TopologyRequestCustom(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_formula import WidgetFormula
        from datadog_api_client.v1.model.topology_request_custom_projection import TopologyRequestCustomProjection
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.topology_request_custom_response_format import (
            TopologyRequestCustomResponseFormat,
        )
        from datadog_api_client.v1.model.widget_sort_by import WidgetSortBy

        return {
            "formulas": ([WidgetFormula],),
            "projection": (TopologyRequestCustomProjection,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (TopologyRequestCustomResponseFormat,),
            "sort": (WidgetSortBy,),
        }

    attribute_map = {
        "formulas": "formulas",
        "projection": "projection",
        "queries": "queries",
        "response_format": "response_format",
        "sort": "sort",
    }

    def __init__(
        self_,
        projection: TopologyRequestCustomProjection,
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
        response_format: TopologyRequestCustomResponseFormat,
        formulas: Union[List[WidgetFormula], UnsetType] = unset,
        sort: Union[WidgetSortBy, UnsetType] = unset,
        **kwargs,
    ):
        """
        Scalar request whose result rows become nodes.

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param projection: Mapping from result columns to node fields. Each result row feeds one node.
        :type projection: TopologyRequestCustomProjection

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Response format of a custom topology map request.
        :type response_format: TopologyRequestCustomResponseFormat

        :param sort: The controls for sorting the widget.
        :type sort: WidgetSortBy, optional
        """
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.projection = projection
        self_.queries = queries
        self_.response_format = response_format
