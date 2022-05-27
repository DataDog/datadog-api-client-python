# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GeomapWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.geomap_widget_request import GeomapWidgetRequest
        from datadog_api_client.v1.model.geomap_widget_definition_style import GeomapWidgetDefinitionStyle
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.geomap_widget_definition_type import GeomapWidgetDefinitionType
        from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView

        return {
            "custom_links": ([WidgetCustomLink],),
            "requests": ([GeomapWidgetRequest],),
            "style": (GeomapWidgetDefinitionStyle,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (GeomapWidgetDefinitionType,),
            "view": (GeomapWidgetDefinitionView,),
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
        "view": "view",
    }

    def __init__(self, requests, style, type, view, *args, **kwargs):
        """
        This visualization displays a series of values by country on a world map.

        :param custom_links: A list of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: Array of one request object to display in the widget. The request must contain a ``group-by`` tag whose value is a country ISO code.

            See the `Request JSON schema documentation <https://docs.datadoghq.com/dashboards/graphing_json/request_json>`_
            for information about building the ``REQUEST_SCHEMA``.
        :type requests: [GeomapWidgetRequest]

        :param style: The style to apply to the widget.
        :type style: GeomapWidgetDefinitionStyle

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: The title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: The size of the title.
        :type title_size: str, optional

        :param type: Type of the geomap widget.
        :type type: GeomapWidgetDefinitionType

        :param view: The view of the world that the map should render.
        :type view: GeomapWidgetDefinitionView
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.style = style
        self.type = type
        self.view = view

    @classmethod
    def _from_openapi_data(cls, requests, style, type, view, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(GeomapWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.style = style
        self.type = type
        self.view = view
        return self
