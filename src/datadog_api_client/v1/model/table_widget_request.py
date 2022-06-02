# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TableWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator
        from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
        from datadog_api_client.v1.model.apm_stats_query_definition import ApmStatsQueryDefinition
        from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
        from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
        from datadog_api_client.v1.model.widget_formula import WidgetFormula
        from datadog_api_client.v1.model.widget_sort import WidgetSort
        from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat

        return {
            "aggregator": (WidgetAggregator,),
            "alias": (str,),
            "apm_query": (LogQueryDefinition,),
            "apm_stats_query": (ApmStatsQueryDefinition,),
            "cell_display_mode": ([TableWidgetCellDisplayMode],),
            "conditional_formats": ([WidgetConditionalFormat],),
            "event_query": (LogQueryDefinition,),
            "formulas": ([WidgetFormula],),
            "limit": (int,),
            "log_query": (LogQueryDefinition,),
            "network_query": (LogQueryDefinition,),
            "order": (WidgetSort,),
            "process_query": (ProcessQueryDefinition,),
            "profile_metrics_query": (LogQueryDefinition,),
            "q": (str,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "alias": "alias",
        "apm_query": "apm_query",
        "apm_stats_query": "apm_stats_query",
        "cell_display_mode": "cell_display_mode",
        "conditional_formats": "conditional_formats",
        "event_query": "event_query",
        "formulas": "formulas",
        "limit": "limit",
        "log_query": "log_query",
        "network_query": "network_query",
        "order": "order",
        "process_query": "process_query",
        "profile_metrics_query": "profile_metrics_query",
        "q": "q",
        "queries": "queries",
        "response_format": "response_format",
        "rum_query": "rum_query",
        "security_query": "security_query",
    }

    def __init__(self, *args, **kwargs):
        """
        Updated table widget.

        :param aggregator: Aggregator used for the request.
        :type aggregator: WidgetAggregator, optional

        :param alias: The column name (defaults to the metric name).
        :type alias: str, optional

        :param apm_query: The log query.
        :type apm_query: LogQueryDefinition, optional

        :param apm_stats_query: The APM stats query for table and distributions widgets.
        :type apm_stats_query: ApmStatsQueryDefinition, optional

        :param cell_display_mode: A list of display modes for each table cell.
        :type cell_display_mode: [TableWidgetCellDisplayMode], optional

        :param conditional_formats: List of conditional formats.
        :type conditional_formats: [WidgetConditionalFormat], optional

        :param event_query: The log query.
        :type event_query: LogQueryDefinition, optional

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param limit: For metric queries, the number of lines to show in the table. Only one request should have this property.
        :type limit: int, optional

        :param log_query: The log query.
        :type log_query: LogQueryDefinition, optional

        :param network_query: The log query.
        :type network_query: LogQueryDefinition, optional

        :param order: Widget sorting methods.
        :type order: WidgetSort, optional

        :param process_query: The process query to use in the widget.
        :type process_query: ProcessQueryDefinition, optional

        :param profile_metrics_query: The log query.
        :type profile_metrics_query: LogQueryDefinition, optional

        :param q: Query definition.
        :type q: str, optional

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition], optional

        :param response_format: Timeseries or Scalar response.
        :type response_format: FormulaAndFunctionResponseFormat, optional

        :param rum_query: The log query.
        :type rum_query: LogQueryDefinition, optional

        :param security_query: The log query.
        :type security_query: LogQueryDefinition, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(TableWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
