# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetFormula(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
        from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
        from datadog_api_client.v1.model.widget_formula_limit import WidgetFormulaLimit

        return {
            "alias": (str,),
            "cell_display_mode": (TableWidgetCellDisplayMode,),
            "conditional_formats": ([WidgetConditionalFormat],),
            "formula": (str,),
            "limit": (WidgetFormulaLimit,),
        }

    attribute_map = {
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "conditional_formats": "conditional_formats",
        "formula": "formula",
        "limit": "limit",
    }

    def __init__(self, formula, *args, **kwargs):
        """
        Formula to be used in a widget query.

        :param alias: Expression alias.
        :type alias: str, optional

        :param cell_display_mode: Define a display mode for the table cell.
        :type cell_display_mode: TableWidgetCellDisplayMode, optional

        :param conditional_formats: List of conditional formats.
        :type conditional_formats: [WidgetConditionalFormat], optional

        :param formula: String expression built from queries, formulas, and functions.
        :type formula: str

        :param limit: Options for limiting results returned.
        :type limit: WidgetFormulaLimit, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.formula = formula

    @classmethod
    def _from_openapi_data(cls, formula, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetFormula, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.formula = formula
        return self
