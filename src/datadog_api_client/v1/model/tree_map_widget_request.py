# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TreeMapWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_formula import WidgetFormula
        from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
        from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat

        return {
            "formulas": ([WidgetFormula],),
            "q": (str,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
        }

    attribute_map = {
        "formulas": "formulas",
        "q": "q",
        "queries": "queries",
        "response_format": "response_format",
    }

    def __init__(self_, *args, **kwargs):
        """
        An updated treemap widget.

        :param formulas: List of formulas that operate on queries.
        :type formulas: [WidgetFormula], optional

        :param q: The widget metrics query.
        :type q: str, optional

        :param queries: List of queries that can be returned directly or used in formulas.
        :type queries: [FormulaAndFunctionQueryDefinition], optional

        :param response_format: Timeseries or Scalar response.
        :type response_format: FormulaAndFunctionResponseFormat, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
