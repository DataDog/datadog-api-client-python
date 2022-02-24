# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.funnel_widget_request import FunnelWidgetRequest
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.funnel_widget_definition_type import FunnelWidgetDefinitionType

    globals()["FunnelWidgetRequest"] = FunnelWidgetRequest
    globals()["WidgetTime"] = WidgetTime
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["FunnelWidgetDefinitionType"] = FunnelWidgetDefinitionType


class FunnelWidgetDefinition(ModelNormal):

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
            "requests": ([FunnelWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (FunnelWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """
        The funnel visualization displays a funnel of user sessions that maps a sequence of view navigation and user interaction in your application.


        :param requests: Request payload used to query items.
        :type requests: [FunnelWidgetRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: The title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: The size of the title.
        :type title_size: str, optional

        :param type: Type of funnel widget.
        :type type: FunnelWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FunnelWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
