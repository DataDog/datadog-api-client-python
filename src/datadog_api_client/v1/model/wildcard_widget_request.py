# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class WildcardWidgetRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Request object for the wildcard widget. Each variant represents a distinct data-fetching pattern: scalar formulas, timeseries formulas, list streams, and histograms.

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param q: The widget metrics query. Deprecated - Use `queries` and `formulas` instead.
        :type q: str, optional

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition], optional

        :param response_format: Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets.
        :type response_format: FormulaAndFunctionResponseFormat, optional

        :param sort: The controls for sorting the widget.
        :type sort: WidgetSortBy, optional

        :param style: Define request widget style.
        :type style: WidgetRequestStyle, optional

        :param apm_query: The log query.
        :type apm_query: LogQueryDefinition, optional

        :param audit_query: The log query.
        :type audit_query: LogQueryDefinition, optional

        :param display_type: Type of display to use for the request.
        :type display_type: WidgetDisplayType, optional

        :param event_query: The log query.
        :type event_query: LogQueryDefinition, optional

        :param log_query: The log query.
        :type log_query: LogQueryDefinition, optional

        :param metadata: Used to define expression aliases.
        :type metadata: [TimeseriesWidgetExpressionAlias], optional

        :param network_query: The log query.
        :type network_query: LogQueryDefinition, optional

        :param on_right_yaxis: Whether or not to display a second y-axis on the right.
        :type on_right_yaxis: bool, optional

        :param process_query: The process query to use in the widget.
        :type process_query: ProcessQueryDefinition, optional

        :param profile_metrics_query: The log query.
        :type profile_metrics_query: LogQueryDefinition, optional

        :param rum_query: The log query.
        :type rum_query: LogQueryDefinition, optional

        :param security_query: The log query.
        :type security_query: LogQueryDefinition, optional

        :param columns: Widget columns.
        :type columns: [ListStreamColumn]

        :param query: Updated list stream widget.
        :type query: ListStreamQuery

        :param apm_stats_query: The APM stats query for table and distributions widgets.
        :type apm_stats_query: ApmStatsQueryDefinition, optional

        :param request_type: Request type for distribution of point values for distribution metrics. Query space aggregator must be `histogram:<metric name>` for points distributions.
        :type request_type: WidgetHistogramRequestType, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.tree_map_widget_request import TreeMapWidgetRequest
        from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
        from datadog_api_client.v1.model.list_stream_widget_request import ListStreamWidgetRequest
        from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest

        return {
            "oneOf": [
                TreeMapWidgetRequest,
                TimeseriesWidgetRequest,
                ListStreamWidgetRequest,
                DistributionWidgetRequest,
            ],
        }
