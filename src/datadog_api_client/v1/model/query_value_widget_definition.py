# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.query_value_widget_definition_type import QueryValueWidgetDefinitionType

    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["QueryValueWidgetRequest"] = QueryValueWidgetRequest
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["QueryValueWidgetDefinitionType"] = QueryValueWidgetDefinitionType


class QueryValueWidgetDefinition(ModelNormal):

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
            "autoscale": (bool,),
            "custom_links": ([WidgetCustomLink],),
            "custom_unit": (str,),
            "precision": (int,),
            "requests": ([QueryValueWidgetRequest],),
            "text_align": (WidgetTextAlign,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (QueryValueWidgetDefinitionType,),
        }

    attribute_map = {
        "autoscale": "autoscale",
        "custom_links": "custom_links",
        "custom_unit": "custom_unit",
        "precision": "precision",
        "requests": "requests",
        "text_align": "text_align",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """
        Query values display the current value of a given metric, APM, or log query.

        :param autoscale: Whether to use auto-scaling or not.
        :type autoscale: bool, optional

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param custom_unit: Display a unit of your choice on the widget.
        :type custom_unit: str, optional

        :param precision: Number of decimals to show. If not defined, the widget uses the raw value.
        :type precision: int, optional

        :param requests: Widget definition.
        :type requests: [QueryValueWidgetRequest]

        :param text_align: How to align the text on the widget.
        :type text_align: WidgetTextAlign, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the query value widget.
        :type type: QueryValueWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(QueryValueWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
