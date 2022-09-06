# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ToplistWidgetRequest(ModelNormal):
    validations = {
        "conditional_formats": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
        from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
        from datadog_api_client.v1.model.widget_formula import WidgetFormula
        from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
        from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

        return {
            "apm_query": (LogQueryDefinition,),
            "audit_query": (LogQueryDefinition,),
            "conditional_formats": ([WidgetConditionalFormat],),
            "event_query": (LogQueryDefinition,),
            "formulas": ([WidgetFormula],),
            "log_query": (LogQueryDefinition,),
            "network_query": (LogQueryDefinition,),
            "process_query": (ProcessQueryDefinition,),
            "profile_metrics_query": (LogQueryDefinition,),
            "q": (str,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
            "style": (WidgetRequestStyle,),
        }

    attribute_map = {
        "apm_query": "apm_query",
        "audit_query": "audit_query",
        "conditional_formats": "conditional_formats",
        "event_query": "event_query",
        "formulas": "formulas",
        "log_query": "log_query",
        "network_query": "network_query",
        "process_query": "process_query",
        "profile_metrics_query": "profile_metrics_query",
        "q": "q",
        "queries": "queries",
        "response_format": "response_format",
        "rum_query": "rum_query",
        "security_query": "security_query",
        "style": "style",
    }

    def __init__(self_, *args, **kwargs):
        """
        Updated top list widget.

        :param apm_query: The log query.
        :type apm_query: LogQueryDefinition, optional

        :param audit_query: The log query.
        :type audit_query: LogQueryDefinition, optional

        :param conditional_formats: List of conditional formats.
        :type conditional_formats: [WidgetConditionalFormat], optional

        :param event_query: The log query.
        :type event_query: LogQueryDefinition, optional

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param log_query: The log query.
        :type log_query: LogQueryDefinition, optional

        :param network_query: The log query.
        :type network_query: LogQueryDefinition, optional

        :param process_query: The process query to use in the widget.
        :type process_query: ProcessQueryDefinition, optional

        :param profile_metrics_query: The log query.
        :type profile_metrics_query: LogQueryDefinition, optional

        :param q: Widget query.
        :type q: str, optional

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition], optional

        :param response_format: Timeseries or Scalar response.
        :type response_format: FormulaAndFunctionResponseFormat, optional

        :param rum_query: The log query.
        :type rum_query: LogQueryDefinition, optional

        :param security_query: The log query.
        :type security_query: LogQueryDefinition, optional

        :param style: Define request widget style.
        :type style: WidgetRequestStyle, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
