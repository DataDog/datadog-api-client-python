# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SunburstWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.sunburst_widget_legend import SunburstWidgetLegend
        from datadog_api_client.v1.model.sunburst_widget_request import SunburstWidgetRequest
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.sunburst_widget_definition_type import SunburstWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "hide_total": (bool,),
            "legend": (SunburstWidgetLegend,),
            "requests": ([SunburstWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SunburstWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "hide_total": "hide_total",
        "legend": "legend",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self, requests, type, *args, **kwargs):
        """
        Sunbursts are spot on to highlight how groups contribute to the total of a query.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param hide_total: Show the total value in this widget.
        :type hide_total: bool, optional

        :param legend: Configuration of the legend.
        :type legend: SunburstWidgetLegend, optional

        :param requests: List of sunburst widget requests.
        :type requests: [SunburstWidgetRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the Sunburst widget.
        :type type: SunburstWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SunburstWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
