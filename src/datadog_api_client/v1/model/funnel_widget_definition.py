# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.funnel_widget_definition_type import FunnelWidgetDefinitionType
    from datadog_api_client.v1.model.funnel_widget_request import FunnelWidgetRequest
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["FunnelWidgetDefinitionType"] = FunnelWidgetDefinitionType
    globals()["FunnelWidgetRequest"] = FunnelWidgetRequest
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class FunnelWidgetDefinition(ModelNormal):
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
            "requests": ([FunnelWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (FunnelWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "type": "type",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """FunnelWidgetDefinition - a model defined in OpenAPI

        Args:
            requests ([FunnelWidgetRequest]): Request payload used to query items.
            type (FunnelWidgetDefinitionType):

        Keyword Args:
            time (WidgetTime): [optional]
            title (str): [optional] The title of the widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] The size of the title.
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
