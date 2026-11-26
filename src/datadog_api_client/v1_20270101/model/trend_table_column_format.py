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
    from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
    from datadog_api_client.v1_20270101.model.trend_table_column_format_mode import TrendTableColumnFormatMode
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.table_trend_cell_display_mode_options import (
        TableTrendCellDisplayModeOptions,
    )
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule


class TrendTableColumnFormat(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
        from datadog_api_client.v1_20270101.model.trend_table_column_format_mode import TrendTableColumnFormatMode
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.table_trend_cell_display_mode_options import (
            TableTrendCellDisplayModeOptions,
        )

        return {
            "conditional_formats": (ConditionalFormats,),
            "mode": (TrendTableColumnFormatMode,),
            "number_format": (WidgetNumberFormat,),
            "trend_options": (TableTrendCellDisplayModeOptions,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "mode": "mode",
        "number_format": "number_format",
        "trend_options": "trend_options",
    }

    def __init__(
        self_,
        mode: TrendTableColumnFormatMode,
        trend_options: TableTrendCellDisplayModeOptions,
        conditional_formats: Union[ConditionalFormats, List[ThresholdFormattingRule], List[Any], UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: ConditionalFormats, optional

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: TrendTableColumnFormatMode

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param trend_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type trend_options: TableTrendCellDisplayModeOptions
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.mode = mode
        self_.trend_options = trend_options
