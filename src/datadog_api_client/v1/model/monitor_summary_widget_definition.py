# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorSummaryWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_color_preference import WidgetColorPreference
        from datadog_api_client.v1.model.widget_monitor_summary_display_format import WidgetMonitorSummaryDisplayFormat
        from datadog_api_client.v1.model.widget_monitor_summary_sort import WidgetMonitorSummarySort
        from datadog_api_client.v1.model.widget_summary_type import WidgetSummaryType
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.monitor_summary_widget_definition_type import (
            MonitorSummaryWidgetDefinitionType,
        )

        return {
            "color_preference": (WidgetColorPreference,),
            "count": (int,),
            "display_format": (WidgetMonitorSummaryDisplayFormat,),
            "hide_zero_counts": (bool,),
            "query": (str,),
            "show_last_triggered": (bool,),
            "sort": (WidgetMonitorSummarySort,),
            "start": (int,),
            "summary_type": (WidgetSummaryType,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (MonitorSummaryWidgetDefinitionType,),
        }

    attribute_map = {
        "color_preference": "color_preference",
        "count": "count",
        "display_format": "display_format",
        "hide_zero_counts": "hide_zero_counts",
        "query": "query",
        "show_last_triggered": "show_last_triggered",
        "sort": "sort",
        "start": "start",
        "summary_type": "summary_type",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self, query, type, *args, **kwargs):
        """
        The monitor summary widget displays a summary view of all your Datadog monitors, or a subset based on a query. Only available on FREE layout dashboards.

        :param color_preference: Which color to use on the widget.
        :type color_preference: WidgetColorPreference, optional

        :param count: The number of monitors to display.
        :type count: int, optional

        :param display_format: What to display on the widget.
        :type display_format: WidgetMonitorSummaryDisplayFormat, optional

        :param hide_zero_counts: Whether to show counts of 0 or not.
        :type hide_zero_counts: bool, optional

        :param query: Query to filter the monitors with.
        :type query: str

        :param show_last_triggered: Whether to show the time that has elapsed since the monitor/group triggered.
        :type show_last_triggered: bool, optional

        :param sort: Widget sorting methods.
        :type sort: WidgetMonitorSummarySort, optional

        :param start: The start of the list. Typically 0.
        :type start: int, optional

        :param summary_type: Which summary type should be used.
        :type summary_type: WidgetSummaryType, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the monitor summary widget.
        :type type: MonitorSummaryWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type

    @classmethod
    def _from_openapi_data(cls, query, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorSummaryWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type
        return self
