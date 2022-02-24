# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
    from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType

    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["TableWidgetHasSearchBar"] = TableWidgetHasSearchBar
    globals()["TableWidgetRequest"] = TableWidgetRequest
    globals()["WidgetTime"] = WidgetTime
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["TableWidgetDefinitionType"] = TableWidgetDefinitionType


class TableWidgetDefinition(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "custom_links": ([WidgetCustomLink],),
            "has_search_bar": (TableWidgetHasSearchBar,),
            "requests": ([TableWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (TableWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "has_search_bar": "has_search_bar",
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
        The table visualization is available on timeboards and screenboards. It displays columns of metrics grouped by tag key.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param has_search_bar: Controls the display of the search bar.
        :type has_search_bar: TableWidgetHasSearchBar, optional

        :param requests: Widget definition.
        :type requests: [TableWidgetRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the table widget.
        :type type: TableWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(TableWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
