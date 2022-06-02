# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ScatterPlotWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.scatter_plot_widget_definition_requests import (
            ScatterPlotWidgetDefinitionRequests,
        )
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.scatter_plot_widget_definition_type import ScatterPlotWidgetDefinitionType
        from datadog_api_client.v1.model.widget_axis import WidgetAxis

        return {
            "color_by_groups": ([str],),
            "custom_links": ([WidgetCustomLink],),
            "requests": (ScatterPlotWidgetDefinitionRequests,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ScatterPlotWidgetDefinitionType,),
            "xaxis": (WidgetAxis,),
            "yaxis": (WidgetAxis,),
        }

    attribute_map = {
        "color_by_groups": "color_by_groups",
        "custom_links": "custom_links",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "xaxis": "xaxis",
        "yaxis": "yaxis",
    }

    def __init__(self, requests, type, *args, **kwargs):
        """
        The scatter plot visualization allows you to graph a chosen scope over two different metrics with their respective aggregation.

        :param color_by_groups: List of groups used for colors.
        :type color_by_groups: [str], optional

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: Widget definition.
        :type requests: ScatterPlotWidgetDefinitionRequests

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the scatter plot widget.
        :type type: ScatterPlotWidgetDefinitionType

        :param xaxis: Axis controls for the widget.
        :type xaxis: WidgetAxis, optional

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

        self = super(ScatterPlotWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
