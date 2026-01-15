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
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.bar_chart_widget_request import BarChartWidgetRequest
    from datadog_api_client.v1.model.bar_chart_widget_style import BarChartWidgetStyle
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.bar_chart_widget_definition_type import BarChartWidgetDefinitionType
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class BarChartWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.bar_chart_widget_request import BarChartWidgetRequest
        from datadog_api_client.v1.model.bar_chart_widget_style import BarChartWidgetStyle
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.bar_chart_widget_definition_type import BarChartWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "requests": ([BarChartWidgetRequest],),
            "style": (BarChartWidgetStyle,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (BarChartWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "requests": "requests",
        "style": "style",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[BarChartWidgetRequest],
        type: BarChartWidgetDefinitionType,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        style: Union[BarChartWidgetStyle, UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The bar chart visualization displays categorical data using vertical bars, allowing you to compare values across different groups.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: List of bar chart widget requests.
        :type requests: [BarChartWidgetRequest]

        :param style: Style customization for a bar chart widget.
        :type style: BarChartWidgetStyle, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the bar chart widget.
        :type type: BarChartWidgetDefinitionType
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if style is not unset:
            kwargs["style"] = style
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
