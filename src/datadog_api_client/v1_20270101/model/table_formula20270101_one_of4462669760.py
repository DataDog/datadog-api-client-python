# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.table_formula_any_of_any_of_item_cell_display_mode4452532448 import (
        TableFormulaAnyOfAnyOfItemCellDisplayMode4452532448,
    )
    from datadog_api_client.v1_20270101.model.table_trend_cell_display_mode_options import (
        TableTrendCellDisplayModeOptions,
    )
    from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
    from datadog_api_client.v1_20270101.model.table_formula_any_of_any_of_item_limit4452334816 import (
        TableFormulaAnyOfAnyOfItemLimit4452334816,
    )
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.widget_formula_style import WidgetFormulaStyle
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule


class TableFormula20270101OneOf4462669760(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_formula_any_of_any_of_item_cell_display_mode4452532448 import (
            TableFormulaAnyOfAnyOfItemCellDisplayMode4452532448,
        )
        from datadog_api_client.v1_20270101.model.table_trend_cell_display_mode_options import (
            TableTrendCellDisplayModeOptions,
        )
        from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
        from datadog_api_client.v1_20270101.model.table_formula_any_of_any_of_item_limit4452334816 import (
            TableFormulaAnyOfAnyOfItemLimit4452334816,
        )
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.widget_formula_style import WidgetFormulaStyle

        return {
            "alias": (str,),
            "cell_display_mode": (TableFormulaAnyOfAnyOfItemCellDisplayMode4452532448,),
            "cell_display_mode_options": (TableTrendCellDisplayModeOptions,),
            "conditional_formats": (ConditionalFormats,),
            "formula": (str,),
            "limit": (TableFormulaAnyOfAnyOfItemLimit4452334816,),
            "number_format": (WidgetNumberFormat,),
            "style": (WidgetFormulaStyle,),
        }

    attribute_map = {
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "cell_display_mode_options": "cell_display_mode_options",
        "conditional_formats": "conditional_formats",
        "formula": "formula",
        "limit": "limit",
        "number_format": "number_format",
        "style": "style",
    }

    def __init__(
        self_,
        cell_display_mode: TableFormulaAnyOfAnyOfItemCellDisplayMode4452532448,
        formula: str,
        alias: Union[str, UnsetType] = unset,
        cell_display_mode_options: Union[TableTrendCellDisplayModeOptions, UnsetType] = unset,
        conditional_formats: Union[ConditionalFormats, List[ThresholdFormattingRule], List[Any], UnsetType] = unset,
        limit: Union[TableFormulaAnyOfAnyOfItemLimit4452334816, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        style: Union[WidgetFormulaStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param cell_display_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode: TableFormulaAnyOfAnyOfItemCellDisplayMode4452532448

        :param cell_display_mode_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode_options: TableTrendCellDisplayModeOptions, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: ConditionalFormats, optional

        :param formula: Test-only generated schema for the dashboard versioning proof of concept.
        :type formula: str

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: TableFormulaAnyOfAnyOfItemLimit4452334816, optional

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: WidgetFormulaStyle, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if cell_display_mode_options is not unset:
            kwargs["cell_display_mode_options"] = cell_display_mode_options
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if limit is not unset:
            kwargs["limit"] = limit
        if number_format is not unset:
            kwargs["number_format"] = number_format
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.cell_display_mode = cell_display_mode
        self_.formula = formula
