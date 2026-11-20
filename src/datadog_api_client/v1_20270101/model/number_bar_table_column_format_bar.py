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
    from datadog_api_client.v1_20270101.model.number_bar_table_column_format_bar_mode import (
        NumberBarTableColumnFormatBarMode,
    )
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule


class NumberBarTableColumnFormatBar(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
        from datadog_api_client.v1_20270101.model.number_bar_table_column_format_bar_mode import (
            NumberBarTableColumnFormatBarMode,
        )
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat

        return {
            "conditional_formats": (ConditionalFormats,),
            "mode": (NumberBarTableColumnFormatBarMode,),
            "number_format": (WidgetNumberFormat,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "mode": "mode",
        "number_format": "number_format",
    }

    def __init__(
        self_,
        mode: NumberBarTableColumnFormatBarMode,
        conditional_formats: Union[ConditionalFormats, List[ThresholdFormattingRule], List[Any], UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: ConditionalFormats, optional

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: NumberBarTableColumnFormatBarMode

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.mode = mode
