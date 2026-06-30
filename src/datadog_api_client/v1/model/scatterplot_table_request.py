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
    from datadog_api_client.v1.model.scatterplot_widget_formula import ScatterplotWidgetFormula
    from datadog_api_client.v1.model.scatterplot_data_projection_projection import ScatterplotDataProjectionProjection
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.scatterplot_data_projection_query import ScatterplotDataProjectionQuery
    from datadog_api_client.v1.model.scatterplot_table_request_type import ScatterplotTableRequestType
    from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
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


class ScatterplotTableRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.scatterplot_widget_formula import ScatterplotWidgetFormula
        from datadog_api_client.v1.model.scatterplot_data_projection_projection import (
            ScatterplotDataProjectionProjection,
        )
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.scatterplot_data_projection_query import ScatterplotDataProjectionQuery
        from datadog_api_client.v1.model.scatterplot_table_request_type import ScatterplotTableRequestType
        from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat

        return {
            "formulas": ([ScatterplotWidgetFormula],),
            "limit": (int,),
            "projection": (ScatterplotDataProjectionProjection,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "query": (ScatterplotDataProjectionQuery,),
            "request_type": (ScatterplotTableRequestType,),
            "response_format": (FormulaAndFunctionResponseFormat,),
        }

    attribute_map = {
        "formulas": "formulas",
        "limit": "limit",
        "projection": "projection",
        "queries": "queries",
        "query": "query",
        "request_type": "request_type",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        formulas: Union[List[ScatterplotWidgetFormula], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        projection: Union[ScatterplotDataProjectionProjection, UnsetType] = unset,
        queries: Union[
            List[
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
            UnsetType,
        ] = unset,
        query: Union[ScatterplotDataProjectionQuery, UnsetType] = unset,
        request_type: Union[ScatterplotTableRequestType, UnsetType] = unset,
        response_format: Union[FormulaAndFunctionResponseFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Scatterplot table request. Supports two modes:

        * **Formulas and functions** (default): ``request_type`` is absent or ``"table"``. Uses ``queries`` and ``formulas``.
        * **Data projection** : ``request_type`` is ``"data_projection"``. Uses ``query`` , ``projection`` , and optionally ``limit``.

        :param formulas: List of Scatterplot formulas that operate on queries.
        :type formulas: [ScatterplotWidgetFormula], optional

        :param limit: Maximum number of rows to return. Used when ``request_type`` is ``"data_projection"``.
        :type limit: int, optional

        :param projection: The projection configuration for a scatterplot data projection request.
        :type projection: ScatterplotDataProjectionProjection, optional

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition], optional

        :param query: The query for a scatterplot data projection request.
        :type query: ScatterplotDataProjectionQuery, optional

        :param request_type: The type of the scatterplot table request.
        :type request_type: ScatterplotTableRequestType, optional

        :param response_format: Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets.
        :type response_format: FormulaAndFunctionResponseFormat, optional
        """
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if limit is not unset:
            kwargs["limit"] = limit
        if projection is not unset:
            kwargs["projection"] = projection
        if queries is not unset:
            kwargs["queries"] = queries
        if query is not unset:
            kwargs["query"] = query
        if request_type is not unset:
            kwargs["request_type"] = request_type
        if response_format is not unset:
            kwargs["response_format"] = response_format
        super().__init__(kwargs)
