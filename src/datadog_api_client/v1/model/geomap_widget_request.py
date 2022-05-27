# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GeomapWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_formula import WidgetFormula
        from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat

        return {
            "formulas": ([WidgetFormula],),
            "log_query": (LogQueryDefinition,),
            "q": (str,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
        }

    attribute_map = {
        "formulas": "formulas",
        "log_query": "log_query",
        "q": "q",
        "queries": "queries",
        "response_format": "response_format",
        "rum_query": "rum_query",
        "security_query": "security_query",
    }

    def __init__(self, *args, **kwargs):
        """
        An updated geomap widget.

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param log_query: The log query.
        :type log_query: LogQueryDefinition, optional

        :param q: The widget metrics query.
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

        self = super(GeomapWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
