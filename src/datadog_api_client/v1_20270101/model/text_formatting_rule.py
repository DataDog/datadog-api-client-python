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
    from datadog_api_client.v1_20270101.model.text_match import TextMatch
    from datadog_api_client.v1_20270101.model.threshold_palette_with_custom import ThresholdPaletteWithCustom
    from datadog_api_client.v1_20270101.model.text_formatting_rule20270101_replace import (
        TextFormattingRule20270101Replace,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of import TextMatch20270101OneOf
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462865408 import (
        TextMatch20270101OneOf4462865408,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462866048 import (
        TextMatch20270101OneOf4462866048,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462866688 import (
        TextMatch20270101OneOf4462866688,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462867328 import (
        TextMatch20270101OneOf4462867328,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462867968 import (
        TextMatch20270101OneOf4462867968,
    )
    from datadog_api_client.v1_20270101.model.text_formatting_rule20270101_replace_one_of import (
        TextFormattingRule20270101ReplaceOneOf,
    )
    from datadog_api_client.v1_20270101.model.text_formatting_rule20270101_replace_one_of4462863328 import (
        TextFormattingRule20270101ReplaceOneOf4462863328,
    )


class TextFormattingRule(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.text_match import TextMatch
        from datadog_api_client.v1_20270101.model.threshold_palette_with_custom import ThresholdPaletteWithCustom
        from datadog_api_client.v1_20270101.model.text_formatting_rule20270101_replace import (
            TextFormattingRule20270101Replace,
        )

        return {
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "highlight_row": (bool,),
            "match": (TextMatch,),
            "palette": (ThresholdPaletteWithCustom,),
            "replace": (TextFormattingRule20270101Replace,),
        }

    attribute_map = {
        "custom_bg_color": "custom_bg_color",
        "custom_fg_color": "custom_fg_color",
        "highlight_row": "highlight_row",
        "match": "match",
        "palette": "palette",
        "replace": "replace",
    }

    def __init__(
        self_,
        match: Union[
            TextMatch,
            TextMatch20270101OneOf,
            TextMatch20270101OneOf4462865408,
            TextMatch20270101OneOf4462866048,
            TextMatch20270101OneOf4462866688,
            TextMatch20270101OneOf4462867328,
            TextMatch20270101OneOf4462867968,
        ],
        custom_bg_color: Union[str, UnsetType] = unset,
        custom_fg_color: Union[str, UnsetType] = unset,
        highlight_row: Union[bool, UnsetType] = unset,
        palette: Union[ThresholdPaletteWithCustom, str, UnsetType] = unset,
        replace: Union[
            TextFormattingRule20270101Replace,
            TextFormattingRule20270101ReplaceOneOf,
            TextFormattingRule20270101ReplaceOneOf4462863328,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param custom_bg_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_bg_color: str, optional

        :param custom_fg_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_fg_color: str, optional

        :param highlight_row: Test-only generated schema for the dashboard versioning proof of concept.
        :type highlight_row: bool, optional

        :param match: Test-only generated schema for the dashboard versioning proof of concept.
        :type match: TextMatch

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: ThresholdPaletteWithCustom, optional

        :param replace: Test-only generated schema for the dashboard versioning proof of concept.
        :type replace: TextFormattingRule20270101Replace, optional
        """
        if custom_bg_color is not unset:
            kwargs["custom_bg_color"] = custom_bg_color
        if custom_fg_color is not unset:
            kwargs["custom_fg_color"] = custom_fg_color
        if highlight_row is not unset:
            kwargs["highlight_row"] = highlight_row
        if palette is not unset:
            kwargs["palette"] = palette
        if replace is not unset:
            kwargs["replace"] = replace
        super().__init__(kwargs)

        self_.match = match
