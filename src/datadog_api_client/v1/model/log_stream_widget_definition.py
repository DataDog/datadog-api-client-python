# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogStreamWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_message_display import WidgetMessageDisplay
        from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.log_stream_widget_definition_type import LogStreamWidgetDefinitionType

        return {
            "columns": ([str],),
            "indexes": ([str],),
            "logset": (str,),
            "message_display": (WidgetMessageDisplay,),
            "query": (str,),
            "show_date_column": (bool,),
            "show_message_column": (bool,),
            "sort": (WidgetFieldSort,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (LogStreamWidgetDefinitionType,),
        }

    attribute_map = {
        "columns": "columns",
        "indexes": "indexes",
        "logset": "logset",
        "message_display": "message_display",
        "query": "query",
        "show_date_column": "show_date_column",
        "show_message_column": "show_message_column",
        "sort": "sort",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.

        :param columns: Which columns to display on the widget.
        :type columns: [str], optional

        :param indexes: An array of index names to query in the stream. Use [] to query all indexes at once.
        :type indexes: [str], optional

        :param logset: ID of the log set to use.
        :type logset: str, optional

        :param message_display: Amount of log lines to display
        :type message_display: WidgetMessageDisplay, optional

        :param query: Query to filter the log stream with.
        :type query: str, optional

        :param show_date_column: Whether to show the date column or not
        :type show_date_column: bool, optional

        :param show_message_column: Whether to show the message column or not
        :type show_message_column: bool, optional

        :param sort: Which column and order to sort by
        :type sort: WidgetFieldSort, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the log stream widget.
        :type type: LogStreamWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogStreamWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
