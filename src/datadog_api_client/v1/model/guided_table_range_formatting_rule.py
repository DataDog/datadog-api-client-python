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
    from datadog_api_client.v1.model.guided_table_range_palette import GuidedTableRangePalette
    from datadog_api_client.v1.model.guided_table_range_formatting_rule_scale import GuidedTableRangeFormattingRuleScale
    from datadog_api_client.v1.model.guided_table_range_formatting_rule_type import GuidedTableRangeFormattingRuleType


class GuidedTableRangeFormattingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_range_palette import GuidedTableRangePalette
        from datadog_api_client.v1.model.guided_table_range_formatting_rule_scale import (
            GuidedTableRangeFormattingRuleScale,
        )
        from datadog_api_client.v1.model.guided_table_range_formatting_rule_type import (
            GuidedTableRangeFormattingRuleType,
        )

        return {
            "max": (float,),
            "min": (float,),
            "palette": (GuidedTableRangePalette,),
            "reverse": (bool,),
            "scale": (GuidedTableRangeFormattingRuleScale,),
            "type": (GuidedTableRangeFormattingRuleType,),
        }

    attribute_map = {
        "max": "max",
        "min": "min",
        "palette": "palette",
        "reverse": "reverse",
        "scale": "scale",
        "type": "type",
    }

    def __init__(
        self_,
        palette: GuidedTableRangePalette,
        type: GuidedTableRangeFormattingRuleType,
        max: Union[float, UnsetType] = unset,
        min: Union[float, UnsetType] = unset,
        reverse: Union[bool, UnsetType] = unset,
        scale: Union[GuidedTableRangeFormattingRuleScale, UnsetType] = unset,
        **kwargs,
    ):
        """
        Formats values according to where they fall on a color scale.

        :param max: Maximum value on the mapping scale.
        :type max: float, optional

        :param min: Minimum value on the mapping scale.
        :type min: float, optional

        :param palette: Color palette used by range-based conditional formatting rules.
        :type palette: GuidedTableRangePalette

        :param reverse: Whether to reverse the palette scale direction.
        :type reverse: bool, optional

        :param scale: Scale function for mapping values to colors.
        :type scale: GuidedTableRangeFormattingRuleScale, optional

        :param type:
        :type type: GuidedTableRangeFormattingRuleType
        """
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        if reverse is not unset:
            kwargs["reverse"] = reverse
        if scale is not unset:
            kwargs["scale"] = scale
        super().__init__(kwargs)

        self_.palette = palette
        self_.type = type
