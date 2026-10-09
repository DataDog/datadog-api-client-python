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
    from datadog_api_client.v1.model.heatgrid_color_config import HeatgridColorConfig
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.heatgrid_label_column import HeatgridLabelColumn
    from datadog_api_client.v1.model.heatgrid_legend import HeatgridLegend
    from datadog_api_client.v1.model.heatgrid_widget_request import HeatgridWidgetRequest
    from datadog_api_client.v1.model.heatgrid_sort import HeatgridSort
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.heatgrid_widget_definition_type import HeatgridWidgetDefinitionType
    from datadog_api_client.v1.model.heatgrid_gradient_custom_color import HeatgridGradientCustomColor
    from datadog_api_client.v1.model.heatgrid_gradient_preset_color import HeatgridGradientPresetColor
    from datadog_api_client.v1.model.heatgrid_discrete_custom_color import HeatgridDiscreteCustomColor
    from datadog_api_client.v1.model.heatgrid_discrete_preset_color import HeatgridDiscretePresetColor
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class HeatgridWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_color_config import HeatgridColorConfig
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.heatgrid_label_column import HeatgridLabelColumn
        from datadog_api_client.v1.model.heatgrid_legend import HeatgridLegend
        from datadog_api_client.v1.model.heatgrid_widget_request import HeatgridWidgetRequest
        from datadog_api_client.v1.model.heatgrid_sort import HeatgridSort
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.heatgrid_widget_definition_type import HeatgridWidgetDefinitionType

        return {
            "color": (HeatgridColorConfig,),
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "label_column": (HeatgridLabelColumn,),
            "legend": (HeatgridLegend,),
            "requests": ([HeatgridWidgetRequest],),
            "sort": (HeatgridSort,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (HeatgridWidgetDefinitionType,),
        }

    attribute_map = {
        "color": "color",
        "custom_links": "custom_links",
        "description": "description",
        "label_column": "label_column",
        "legend": "legend",
        "requests": "requests",
        "sort": "sort",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[HeatgridWidgetRequest],
        sort: HeatgridSort,
        type: HeatgridWidgetDefinitionType,
        color: Union[
            HeatgridColorConfig,
            HeatgridGradientCustomColor,
            HeatgridGradientPresetColor,
            HeatgridDiscreteCustomColor,
            HeatgridDiscretePresetColor,
            UnsetType,
        ] = unset,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        label_column: Union[HeatgridLabelColumn, UnsetType] = unset,
        legend: Union[HeatgridLegend, UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The heatgrid visualization displays values for each group over time using color.

        :param color: Color configuration for continuous gradients or discrete thresholds.
        :type color: HeatgridColorConfig, optional

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Description of the widget.
        :type description: str, optional

        :param label_column: Configuration of the group label column.
        :type label_column: HeatgridLabelColumn, optional

        :param legend: Legend configuration for the heatgrid widget.
        :type legend: HeatgridLegend, optional

        :param requests: Widget requests. The widget displays one formula, which can combine multiple queries.
        :type requests: [HeatgridWidgetRequest]

        :param sort: Ordering of the heatgrid rows.
        :type sort: HeatgridSort

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the heatgrid widget.
        :type type: HeatgridWidgetDefinitionType
        """
        if color is not unset:
            kwargs["color"] = color
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if label_column is not unset:
            kwargs["label_column"] = label_column
        if legend is not unset:
            kwargs["legend"] = legend
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
        self_.sort = sort
        self_.type = type
