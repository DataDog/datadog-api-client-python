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
    from datadog_api_client.v1.model.table_widget_text_format_palette import TableWidgetTextFormatPalette
    from datadog_api_client.v1.model.table_widget_text_format_replace import TableWidgetTextFormatReplace
    from datadog_api_client.v1.model.table_widget_text_format_replace_all import TableWidgetTextFormatReplaceAll
    from datadog_api_client.v1.model.table_widget_text_format_replace_substring import (
        TableWidgetTextFormatReplaceSubstring,
    )


class TableWidgetTextFormatRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.table_widget_text_format_match import TableWidgetTextFormatMatch
        from datadog_api_client.v1.model.table_widget_text_format_palette import TableWidgetTextFormatPalette
        from datadog_api_client.v1.model.table_widget_text_format_replace import TableWidgetTextFormatReplace

        return {
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "match": (TableWidgetTextFormatMatch,),
            "palette": (TableWidgetTextFormatPalette,),
            "replace": (TableWidgetTextFormatReplace,),
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
        palette: Union[TableWidgetTextFormatPalette, UnsetType] = unset,
        replace: Union[
            TableWidgetTextFormatReplace,
            TableWidgetTextFormatReplaceAll,
            TableWidgetTextFormatReplaceSubstring,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Text format rules.

        :param custom_bg_color: Hex representation of the custom background color. Used with custom background palette option.
        :type custom_bg_color: str, optional

        :param custom_fg_color: Hex representation of the custom text color. Used with custom text palette option.
        :type custom_fg_color: str, optional

        :param match: Match rule for the table widget text format.
        :type match: TableWidgetTextFormatMatch

        :param palette: Color-on-color palette to highlight replaced text.
        :type palette: TableWidgetTextFormatPalette, optional

        :param replace: Replace rule for the table widget text format.
        :type replace: TableWidgetTextFormatReplace, optional
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
