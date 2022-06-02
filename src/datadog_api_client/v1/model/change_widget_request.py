# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ChangeWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
        from datadog_api_client.v1.model.widget_change_type import WidgetChangeType
        from datadog_api_client.v1.model.widget_compare_to import WidgetCompareTo
        from datadog_api_client.v1.model.widget_formula import WidgetFormula
        from datadog_api_client.v1.model.widget_order_by import WidgetOrderBy
        from datadog_api_client.v1.model.widget_sort import WidgetSort
        from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat

        return {
            "apm_query": (LogQueryDefinition,),
            "change_type": (WidgetChangeType,),
            "compare_to": (WidgetCompareTo,),
            "event_query": (LogQueryDefinition,),
            "formulas": ([WidgetFormula],),
            "increase_good": (bool,),
            "log_query": (LogQueryDefinition,),
            "network_query": (LogQueryDefinition,),
            "order_by": (WidgetOrderBy,),
            "order_dir": (WidgetSort,),
            "process_query": (ProcessQueryDefinition,),
            "profile_metrics_query": (LogQueryDefinition,),
            "q": (str,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
            "show_present": (bool,),
        }

    attribute_map = {
        "apm_query": "apm_query",
        "change_type": "change_type",
        "compare_to": "compare_to",
        "event_query": "event_query",
        "formulas": "formulas",
        "increase_good": "increase_good",
        "log_query": "log_query",
        "network_query": "network_query",
        "order_by": "order_by",
        "order_dir": "order_dir",
        "process_query": "process_query",
        "profile_metrics_query": "profile_metrics_query",
        "q": "q",
        "queries": "queries",
        "response_format": "response_format",
        "rum_query": "rum_query",
        "security_query": "security_query",
        "show_present": "show_present",
    }

    def __init__(self, *args, **kwargs):
        """
        Updated change widget.

        :param apm_query: The log query.
        :type apm_query: LogQueryDefinition, optional

        :param change_type: Show the absolute or the relative change.
        :type change_type: WidgetChangeType, optional

        :param compare_to: Timeframe used for the change comparison.
        :type compare_to: WidgetCompareTo, optional

        :param event_query: The log query.
        :type event_query: LogQueryDefinition, optional

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param increase_good: Whether to show increase as good.
        :type increase_good: bool, optional

        :param log_query: The log query.
        :type log_query: LogQueryDefinition, optional

        :param network_query: The log query.
        :type network_query: LogQueryDefinition, optional

        :param order_by: What to order by.
        :type order_by: WidgetOrderBy, optional

        :param order_dir: Widget sorting methods.
        :type order_dir: WidgetSort, optional

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

        :param show_present: Whether to show the present value.
        :type show_present: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ChangeWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
