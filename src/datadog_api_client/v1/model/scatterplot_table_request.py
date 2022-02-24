# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.scatterplot_widget_formula import ScatterplotWidgetFormula
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat

    globals()["ScatterplotWidgetFormula"] = ScatterplotWidgetFormula
    globals()["FormulaAndFunctionQueryDefinition"] = FormulaAndFunctionQueryDefinition
    globals()["FormulaAndFunctionResponseFormat"] = FormulaAndFunctionResponseFormat


class ScatterplotTableRequest(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "formulas": ([ScatterplotWidgetFormula],),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
        "response_format": "response_format",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Scatterplot request containing formulas and functions.

        :param formulas: List of Scatterplot formulas that operate on queries. **This feature is currently in beta.**
        :type formulas: [ScatterplotWidgetFormula], optional

        :param queries: List of queries that can be returned directly or used in formulas. **This feature is currently in beta.**
        :type queries: [FormulaAndFunctionQueryDefinition], optional

        :param response_format: Timeseries or Scalar response. **This feature is currently in beta.**
        :type response_format: FormulaAndFunctionResponseFormat, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ScatterplotTableRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
