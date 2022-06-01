# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ToplistWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.toplist_widget_request import ToplistWidgetRequest
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.toplist_widget_definition_type import ToplistWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "requests": ([ToplistWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ToplistWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self, requests, type, *args, **kwargs):
        """
        The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: List of top list widget requests.
        :type requests: [ToplistWidgetRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the top list widget.
        :type type: ToplistWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ToplistWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
