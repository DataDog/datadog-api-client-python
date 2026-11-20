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
    from datadog_api_client.v1_20270101.model.advanced_query_table_cell_display_mode import (
        AdvancedQueryTableCellDisplayMode,
    )
    from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
    from datadog_api_client.v1_20270101.model.query_table_date_format import QueryTableDateFormat
    from datadog_api_client.v1_20270101.model.query_table_projection_dimension_dimension import (
        QueryTableProjectionDimensionDimension,
    )
    from datadog_api_client.v1_20270101.model.query_table_column_link import QueryTableColumnLink
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.text_formatting_rule import TextFormattingRule
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule


class QueryTableProjectionDimension(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.advanced_query_table_cell_display_mode import (
            AdvancedQueryTableCellDisplayMode,
        )
        from datadog_api_client.v1_20270101.model.conditional_formats import ConditionalFormats
        from datadog_api_client.v1_20270101.model.query_table_date_format import QueryTableDateFormat
        from datadog_api_client.v1_20270101.model.query_table_projection_dimension_dimension import (
            QueryTableProjectionDimensionDimension,
        )
        from datadog_api_client.v1_20270101.model.query_table_column_link import QueryTableColumnLink
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.text_formatting_rule import TextFormattingRule

        return {
            "cell_display_mode": (AdvancedQueryTableCellDisplayMode,),
            "column": (str,),
            "conditional_formats": (ConditionalFormats,),
            "date_format": (QueryTableDateFormat,),
            "dimension": (QueryTableProjectionDimensionDimension,),
            "is_hidden": (bool,),
            "link": (QueryTableColumnLink,),
            "number_format": (WidgetNumberFormat,),
            "text_align": (WidgetTextAlign,),
            "text_formats": ([TextFormattingRule],),
        }

    attribute_map = {
        "cell_display_mode": "cell_display_mode",
        "column": "column",
        "conditional_formats": "conditional_formats",
        "date_format": "date_format",
        "dimension": "dimension",
        "is_hidden": "is_hidden",
        "link": "link",
        "number_format": "number_format",
        "text_align": "text_align",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        column: str,
        dimension: QueryTableProjectionDimensionDimension,
        cell_display_mode: Union[AdvancedQueryTableCellDisplayMode, UnsetType] = unset,
        conditional_formats: Union[ConditionalFormats, List[ThresholdFormattingRule], List[Any], UnsetType] = unset,
        date_format: Union[QueryTableDateFormat, str, UnsetType] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        link: Union[QueryTableColumnLink, UnsetType] = unset,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        text_align: Union[WidgetTextAlign, UnsetType] = unset,
        text_formats: Union[List[TextFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param cell_display_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode: AdvancedQueryTableCellDisplayMode, optional

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: ConditionalFormats, optional

        :param date_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type date_format: QueryTableDateFormat, optional

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: QueryTableProjectionDimensionDimension

        :param is_hidden: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hidden: bool, optional

        :param link: Test-only generated schema for the dashboard versioning proof of concept.
        :type link: QueryTableColumnLink, optional

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param text_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_align: WidgetTextAlign, optional

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [TextFormattingRule], optional
        """
        if cell_display_mode is not unset:
            kwargs["cell_display_mode"] = cell_display_mode
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if date_format is not unset:
            kwargs["date_format"] = date_format
        if is_hidden is not unset:
            kwargs["is_hidden"] = is_hidden
        if link is not unset:
            kwargs["link"] = link
        if number_format is not unset:
            kwargs["number_format"] = number_format
        if text_align is not unset:
            kwargs["text_align"] = text_align
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
