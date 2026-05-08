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
    from datadog_api_client.v1.model.point_plot_widget_legend import PointPlotWidgetLegend
    from datadog_api_client.v1.model.widget_marker import WidgetMarker
    from datadog_api_client.v1.model.point_plot_widget_request import PointPlotWidgetRequest
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.point_plot_widget_definition_type import PointPlotWidgetDefinitionType
    from datadog_api_client.v1.model.widget_axis import WidgetAxis
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class PointPlotWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.point_plot_widget_legend import PointPlotWidgetLegend
        from datadog_api_client.v1.model.widget_marker import WidgetMarker
        from datadog_api_client.v1.model.point_plot_widget_request import PointPlotWidgetRequest
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.point_plot_widget_definition_type import PointPlotWidgetDefinitionType
        from datadog_api_client.v1.model.widget_axis import WidgetAxis

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "legend": (PointPlotWidgetLegend,),
            "markers": ([WidgetMarker],),
            "requests": ([PointPlotWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (PointPlotWidgetDefinitionType,),
            "yaxis": (WidgetAxis,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "description": "description",
        "legend": "legend",
        "markers": "markers",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "yaxis": "yaxis",
    }

    def __init__(
        self_,
        requests: List[PointPlotWidgetRequest],
        type: PointPlotWidgetDefinitionType,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        legend: Union[PointPlotWidgetLegend, UnsetType] = unset,
        markers: Union[List[WidgetMarker], UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        yaxis: Union[WidgetAxis, UnsetType] = unset,
        **kwargs,
    ):
        """
        The point plot displays individual data points over time.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param description: The description of the widget.
        :type description: str, optional

        :param legend: Legend configuration for the point plot widget.
        :type legend: PointPlotWidgetLegend, optional

        :param markers: List of markers for the widget.
        :type markers: [WidgetMarker], optional

        :param requests: List of request configurations for the widget.
        :type requests: [PointPlotWidgetRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the point plot widget.
        :type type: PointPlotWidgetDefinitionType

        :param yaxis: Axis controls for the widget.
        :type yaxis: WidgetAxis, optional
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if legend is not unset:
            kwargs["legend"] = legend
        if markers is not unset:
            kwargs["markers"] = markers
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        if yaxis is not unset:
            kwargs["yaxis"] = yaxis
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
