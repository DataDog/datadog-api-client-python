# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.heat_map_widget_definition_type import HeatMapWidgetDefinitionType
    from datadog_api_client.v1.model.heat_map_widget_request import HeatMapWidgetRequest
    from datadog_api_client.v1.model.widget_axis import WidgetAxis
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_event import WidgetEvent
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["HeatMapWidgetDefinitionType"] = HeatMapWidgetDefinitionType
    globals()["HeatMapWidgetRequest"] = HeatMapWidgetRequest
    globals()["WidgetAxis"] = WidgetAxis
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetEvent"] = WidgetEvent
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class HeatMapWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
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
        "requests": "requests",
        "type": "type",
        "custom_links": "custom_links",
        "events": "events",
        "legend_size": "legend_size",
        "show_legend": "show_legend",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "yaxis": "yaxis",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """HeatMapWidgetDefinition - a model defined in OpenAPI

        Args:
            requests ([HeatMapWidgetRequest]): List of widget types.
            type (HeatMapWidgetDefinitionType):

        Keyword Args:
            custom_links ([WidgetCustomLink]): [optional] List of custom links.
            events ([WidgetEvent]): [optional] List of widget events.
            legend_size (str): [optional] Available legend sizes for a widget. Should be one of \"0\", \"2\", \"4\", \"8\", \"16\", or \"auto\".
            show_legend (bool): [optional] Whether or not to display the legend on this widget.
            time (WidgetTime): [optional]
            title (str): [optional] Title of the widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] Size of the title.
            yaxis (WidgetAxis): [optional]
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
