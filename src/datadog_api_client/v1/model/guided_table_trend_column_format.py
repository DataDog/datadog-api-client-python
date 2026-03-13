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
    from datadog_api_client.v1.model.guided_table_conditional_formats import GuidedTableConditionalFormats
    from datadog_api_client.v1.model.guided_table_trend_column_format_mode import GuidedTableTrendColumnFormatMode
    from datadog_api_client.v1.model.guided_table_number_format import GuidedTableNumberFormat
    from datadog_api_client.v1.model.widget_formula_cell_display_mode_options import WidgetFormulaCellDisplayModeOptions
    from datadog_api_client.v1.model.guided_table_threshold_formatting_rule import GuidedTableThresholdFormattingRule
    from datadog_api_client.v1.model.guided_table_range_formatting_rule import GuidedTableRangeFormattingRule


class GuidedTableTrendColumnFormat(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_conditional_formats import GuidedTableConditionalFormats
        from datadog_api_client.v1.model.guided_table_trend_column_format_mode import GuidedTableTrendColumnFormatMode
        from datadog_api_client.v1.model.guided_table_number_format import GuidedTableNumberFormat
        from datadog_api_client.v1.model.widget_formula_cell_display_mode_options import (
            WidgetFormulaCellDisplayModeOptions,
        )

        return {
            "conditional_formats": (GuidedTableConditionalFormats,),
            "mode": (GuidedTableTrendColumnFormatMode,),
            "number_format": (GuidedTableNumberFormat,),
            "trend_options": (WidgetFormulaCellDisplayModeOptions,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "mode": "mode",
        "number_format": "number_format",
        "trend_options": "trend_options",
    }

    def __init__(
        self_,
        mode: GuidedTableTrendColumnFormatMode,
        trend_options: WidgetFormulaCellDisplayModeOptions,
        conditional_formats: Union[
            GuidedTableConditionalFormats,
            List[GuidedTableThresholdFormattingRule],
            List[GuidedTableRangeFormattingRule],
            UnsetType,
        ] = unset,
        number_format: Union[GuidedTableNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Formats a guided table column as a trend sparkline.

        :param conditional_formats: Conditional formatting rules for a guided table column. Either an array of threshold-based rules or a single range-based rule.
        :type conditional_formats: GuidedTableConditionalFormats, optional

        :param mode:
        :type mode: GuidedTableTrendColumnFormatMode

        :param number_format: Number display format for a guided table column value.
        :type number_format: GuidedTableNumberFormat, optional

        :param trend_options: Cell display mode options for the widget formula. (only if ``cell_display_mode`` is set to ``trend`` ).
        :type trend_options: WidgetFormulaCellDisplayModeOptions
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.mode = mode
        self_.trend_options = trend_options
