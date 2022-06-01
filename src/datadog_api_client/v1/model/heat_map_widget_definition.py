# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HeatMapWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.widget_event import WidgetEvent
        from datadog_api_client.v1.model.heat_map_widget_request import HeatMapWidgetRequest
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.heat_map_widget_definition_type import HeatMapWidgetDefinitionType
        from datadog_api_client.v1.model.widget_axis import WidgetAxis

        return {
            "custom_links": ([WidgetCustomLink],),
            "events": ([WidgetEvent],),
            "legend_size": (str,),
            "requests": ([HeatMapWidgetRequest],),
            "show_legend": (bool,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (HeatMapWidgetDefinitionType,),
            "yaxis": (WidgetAxis,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "events": "events",
        "legend_size": "legend_size",
        "requests": "requests",
        "show_legend": "show_legend",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "yaxis": "yaxis",
    }

    def __init__(self, requests, type, *args, **kwargs):
        """
        The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param events: List of widget events.
        :type events: [WidgetEvent], optional

        :param legend_size: Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
        :type legend_size: str, optional

        :param requests: List of widget types.
        :type requests: [HeatMapWidgetRequest]

        :param show_legend: Whether or not to display the legend on this widget.
        :type show_legend: bool, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the heat map widget.
        :type type: HeatMapWidgetDefinitionType

        :param yaxis: Axis controls for the widget.
        :type yaxis: WidgetAxis, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HeatMapWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
