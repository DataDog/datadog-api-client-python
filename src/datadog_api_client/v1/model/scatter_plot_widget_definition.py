# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.scatter_plot_widget_definition_requests import ScatterPlotWidgetDefinitionRequests
    from datadog_api_client.v1.model.scatter_plot_widget_definition_type import ScatterPlotWidgetDefinitionType
    from datadog_api_client.v1.model.widget_axis import WidgetAxis
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["ScatterPlotWidgetDefinitionRequests"] = ScatterPlotWidgetDefinitionRequests
    globals()["ScatterPlotWidgetDefinitionType"] = ScatterPlotWidgetDefinitionType
    globals()["WidgetAxis"] = WidgetAxis
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class ScatterPlotWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
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
        "requests": "requests",
        "type": "type",
        "color_by_groups": "color_by_groups",
        "custom_links": "custom_links",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "xaxis": "xaxis",
        "yaxis": "yaxis",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """ScatterPlotWidgetDefinition - a model defined in OpenAPI

        Args:
            requests (ScatterPlotWidgetDefinitionRequests):
            type (ScatterPlotWidgetDefinitionType):

        Keyword Args:
            color_by_groups ([str]): [optional] List of groups used for colors.
            custom_links ([WidgetCustomLink]): [optional] List of custom links.
            time (WidgetTime): [optional]
            title (str): [optional] Title of your widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] Size of the title.
            xaxis (WidgetAxis): [optional]
            yaxis (WidgetAxis): [optional]
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
