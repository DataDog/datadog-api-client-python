# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.widget_comparator import WidgetComparator
    from datadog_api_client.v1.model.guided_table_threshold_palette import GuidedTableThresholdPalette
    from datadog_api_client.v1.model.guided_table_threshold_formatting_rule_value import (
        GuidedTableThresholdFormattingRuleValue,
    )


class GuidedTableThresholdFormattingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_comparator import WidgetComparator
        from datadog_api_client.v1.model.guided_table_threshold_palette import GuidedTableThresholdPalette
        from datadog_api_client.v1.model.guided_table_threshold_formatting_rule_value import (
            GuidedTableThresholdFormattingRuleValue,
        )

        return {
            "comparator": (WidgetComparator,),
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "hide_value": (bool,),
            "image_url": (str,),
            "palette": (GuidedTableThresholdPalette,),
            "value": (GuidedTableThresholdFormattingRuleValue,),
        }

    attribute_map = {
        "comparator": "comparator",
        "custom_bg_color": "custom_bg_color",
        "custom_fg_color": "custom_fg_color",
        "hide_value": "hide_value",
        "image_url": "image_url",
        "palette": "palette",
        "value": "value",
    }

    def __init__(
        self_,
        comparator: WidgetComparator,
        palette: GuidedTableThresholdPalette,
        custom_bg_color: Union[str, UnsetType] = unset,
        custom_fg_color: Union[str, UnsetType] = unset,
        hide_value: Union[bool, UnsetType] = unset,
        image_url: Union[str, UnsetType] = unset,
        value: Union[GuidedTableThresholdFormattingRuleValue, float, str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Conditional formatting rule that applies when a value satisfies a threshold comparator condition.

        :param comparator: Comparator to apply.
        :type comparator: WidgetComparator

        :param custom_bg_color: Custom background color. Used with ``custom_bg`` palette.
        :type custom_bg_color: str, optional

        :param custom_fg_color: Custom text color. Used with ``custom_text`` palette.
        :type custom_fg_color: str, optional

        :param hide_value: Whether to hide the data value when this rule matches.
        :type hide_value: bool, optional

        :param image_url: URL of an image to display as background.
        :type image_url: str, optional

        :param palette: Color palette used by threshold-based conditional formatting and text formatting rules in a guided table.
        :type palette: GuidedTableThresholdPalette

        :param value: Threshold value to compare against.
        :type value: GuidedTableThresholdFormattingRuleValue, optional
        """
        if custom_bg_color is not unset:
            kwargs["custom_bg_color"] = custom_bg_color
        if custom_fg_color is not unset:
            kwargs["custom_fg_color"] = custom_fg_color
        if hide_value is not unset:
            kwargs["hide_value"] = hide_value
        if image_url is not unset:
            kwargs["image_url"] = image_url
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.comparator = comparator
        self_.palette = palette
