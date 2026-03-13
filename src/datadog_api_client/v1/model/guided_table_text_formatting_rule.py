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
    from datadog_api_client.v1.model.table_widget_text_format_match import TableWidgetTextFormatMatch
    from datadog_api_client.v1.model.guided_table_threshold_palette import GuidedTableThresholdPalette
    from datadog_api_client.v1.model.guided_table_text_formatting_rule_replace import (
        GuidedTableTextFormattingRuleReplace,
    )
    from datadog_api_client.v1.model.table_widget_text_format_replace_all import TableWidgetTextFormatReplaceAll
    from datadog_api_client.v1.model.guided_table_text_formatting_rule_replace_one_of4484404608 import (
        GuidedTableTextFormattingRuleReplaceOneOf4484404608,
    )


class GuidedTableTextFormattingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.table_widget_text_format_match import TableWidgetTextFormatMatch
        from datadog_api_client.v1.model.guided_table_threshold_palette import GuidedTableThresholdPalette
        from datadog_api_client.v1.model.guided_table_text_formatting_rule_replace import (
            GuidedTableTextFormattingRuleReplace,
        )

        return {
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "match": (TableWidgetTextFormatMatch,),
            "palette": (GuidedTableThresholdPalette,),
            "replace": (GuidedTableTextFormattingRuleReplace,),
        }

    attribute_map = {
        "custom_bg_color": "custom_bg_color",
        "custom_fg_color": "custom_fg_color",
        "match": "match",
        "palette": "palette",
        "replace": "replace",
    }

    def __init__(
        self_,
        match: TableWidgetTextFormatMatch,
        custom_bg_color: Union[str, UnsetType] = unset,
        custom_fg_color: Union[str, UnsetType] = unset,
        palette: Union[GuidedTableThresholdPalette, UnsetType] = unset,
        replace: Union[
            GuidedTableTextFormattingRuleReplace,
            TableWidgetTextFormatReplaceAll,
            GuidedTableTextFormattingRuleReplaceOneOf4484404608,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Rule for applying visual formatting to text values in a guided table group-by column.

        :param custom_bg_color: Custom background color hex code. Used with ``custom_bg`` palette.
        :type custom_bg_color: str, optional

        :param custom_fg_color: Custom text color hex code. Used with ``custom_text`` palette.
        :type custom_fg_color: str, optional

        :param match: Match rule for the table widget text format.
        :type match: TableWidgetTextFormatMatch

        :param palette: Color palette used by threshold-based conditional formatting and text formatting rules in a guided table.
        :type palette: GuidedTableThresholdPalette, optional

        :param replace: Optional replacement to apply to matched text.
        :type replace: GuidedTableTextFormattingRuleReplace, optional
        """
        if custom_bg_color is not unset:
            kwargs["custom_bg_color"] = custom_bg_color
        if custom_fg_color is not unset:
            kwargs["custom_fg_color"] = custom_fg_color
        if palette is not unset:
            kwargs["palette"] = palette
        if replace is not unset:
            kwargs["replace"] = replace
        super().__init__(kwargs)

        self_.match = match
