# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelComposed,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.alert_graph_widget_definition import AlertGraphWidgetDefinition
    from datadog_api_client.v1.model.alert_value_widget_definition import AlertValueWidgetDefinition
    from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
    from datadog_api_client.v1.model.check_status_widget_definition import CheckStatusWidgetDefinition
    from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
    from datadog_api_client.v1.model.event_stream_widget_definition import EventStreamWidgetDefinition
    from datadog_api_client.v1.model.event_timeline_widget_definition import EventTimelineWidgetDefinition
    from datadog_api_client.v1.model.free_text_widget_definition import FreeTextWidgetDefinition
    from datadog_api_client.v1.model.funnel_widget_definition import FunnelWidgetDefinition
    from datadog_api_client.v1.model.funnel_widget_definition_type import FunnelWidgetDefinitionType
    from datadog_api_client.v1.model.funnel_widget_request import FunnelWidgetRequest
    from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
    from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
    from datadog_api_client.v1.model.group_widget_definition import GroupWidgetDefinition
    from datadog_api_client.v1.model.heat_map_widget_definition import HeatMapWidgetDefinition
    from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition
    from datadog_api_client.v1.model.host_map_widget_definition_style import HostMapWidgetDefinitionStyle
    from datadog_api_client.v1.model.i_frame_widget_definition import IFrameWidgetDefinition
    from datadog_api_client.v1.model.image_widget_definition import ImageWidgetDefinition
    from datadog_api_client.v1.model.list_stream_widget_definition import ListStreamWidgetDefinition
    from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
    from datadog_api_client.v1.model.monitor_summary_widget_definition import MonitorSummaryWidgetDefinition
    from datadog_api_client.v1.model.note_widget_definition import NoteWidgetDefinition
    from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition
    from datadog_api_client.v1.model.scatter_plot_widget_definition import ScatterPlotWidgetDefinition
    from datadog_api_client.v1.model.service_map_widget_definition import ServiceMapWidgetDefinition
    from datadog_api_client.v1.model.service_summary_widget_definition import ServiceSummaryWidgetDefinition
    from datadog_api_client.v1.model.slo_widget_definition import SLOWidgetDefinition
    from datadog_api_client.v1.model.sunburst_widget_definition import SunburstWidgetDefinition
    from datadog_api_client.v1.model.sunburst_widget_legend import SunburstWidgetLegend
    from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
    from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
    from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
    from datadog_api_client.v1.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
    from datadog_api_client.v1.model.timeseries_widget_legend_layout import TimeseriesWidgetLegendLayout
    from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition
    from datadog_api_client.v1.model.tree_map_color_by import TreeMapColorBy
    from datadog_api_client.v1.model.tree_map_group_by import TreeMapGroupBy
    from datadog_api_client.v1.model.tree_map_size_by import TreeMapSizeBy
    from datadog_api_client.v1.model.tree_map_widget_definition import TreeMapWidgetDefinition
    from datadog_api_client.v1.model.widget import Widget
    from datadog_api_client.v1.model.widget_axis import WidgetAxis
    from datadog_api_client.v1.model.widget_color_preference import WidgetColorPreference
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_event import WidgetEvent
    from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
    from datadog_api_client.v1.model.widget_grouping import WidgetGrouping
    from datadog_api_client.v1.model.widget_horizontal_align import WidgetHorizontalAlign
    from datadog_api_client.v1.model.widget_image_sizing import WidgetImageSizing
    from datadog_api_client.v1.model.widget_layout_type import WidgetLayoutType
    from datadog_api_client.v1.model.widget_margin import WidgetMargin
    from datadog_api_client.v1.model.widget_marker import WidgetMarker
    from datadog_api_client.v1.model.widget_message_display import WidgetMessageDisplay
    from datadog_api_client.v1.model.widget_monitor_summary_sort import WidgetMonitorSummarySort
    from datadog_api_client.v1.model.widget_node_type import WidgetNodeType
    from datadog_api_client.v1.model.widget_service_summary_display_format import WidgetServiceSummaryDisplayFormat
    from datadog_api_client.v1.model.widget_size_format import WidgetSizeFormat
    from datadog_api_client.v1.model.widget_summary_type import WidgetSummaryType
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_tick_edge import WidgetTickEdge
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_time_windows import WidgetTimeWindows
    from datadog_api_client.v1.model.widget_vertical_align import WidgetVerticalAlign
    from datadog_api_client.v1.model.widget_view_mode import WidgetViewMode
    from datadog_api_client.v1.model.widget_viz_type import WidgetVizType

    globals()["AlertGraphWidgetDefinition"] = AlertGraphWidgetDefinition
    globals()["AlertValueWidgetDefinition"] = AlertValueWidgetDefinition
    globals()["ChangeWidgetDefinition"] = ChangeWidgetDefinition
    globals()["CheckStatusWidgetDefinition"] = CheckStatusWidgetDefinition
    globals()["DistributionWidgetDefinition"] = DistributionWidgetDefinition
    globals()["EventStreamWidgetDefinition"] = EventStreamWidgetDefinition
    globals()["EventTimelineWidgetDefinition"] = EventTimelineWidgetDefinition
    globals()["FreeTextWidgetDefinition"] = FreeTextWidgetDefinition
    globals()["FunnelWidgetDefinition"] = FunnelWidgetDefinition
    globals()["FunnelWidgetDefinitionType"] = FunnelWidgetDefinitionType
    globals()["FunnelWidgetRequest"] = FunnelWidgetRequest
    globals()["GeomapWidgetDefinition"] = GeomapWidgetDefinition
    globals()["GeomapWidgetDefinitionView"] = GeomapWidgetDefinitionView
    globals()["GroupWidgetDefinition"] = GroupWidgetDefinition
    globals()["HeatMapWidgetDefinition"] = HeatMapWidgetDefinition
    globals()["HostMapWidgetDefinition"] = HostMapWidgetDefinition
    globals()["HostMapWidgetDefinitionStyle"] = HostMapWidgetDefinitionStyle
    globals()["IFrameWidgetDefinition"] = IFrameWidgetDefinition
    globals()["ImageWidgetDefinition"] = ImageWidgetDefinition
    globals()["ListStreamWidgetDefinition"] = ListStreamWidgetDefinition
    globals()["LogStreamWidgetDefinition"] = LogStreamWidgetDefinition
    globals()["MonitorSummaryWidgetDefinition"] = MonitorSummaryWidgetDefinition
    globals()["NoteWidgetDefinition"] = NoteWidgetDefinition
    globals()["QueryValueWidgetDefinition"] = QueryValueWidgetDefinition
    globals()["SLOWidgetDefinition"] = SLOWidgetDefinition
    globals()["ScatterPlotWidgetDefinition"] = ScatterPlotWidgetDefinition
    globals()["ServiceMapWidgetDefinition"] = ServiceMapWidgetDefinition
    globals()["ServiceSummaryWidgetDefinition"] = ServiceSummaryWidgetDefinition
    globals()["SunburstWidgetDefinition"] = SunburstWidgetDefinition
    globals()["SunburstWidgetLegend"] = SunburstWidgetLegend
    globals()["TableWidgetDefinition"] = TableWidgetDefinition
    globals()["TableWidgetHasSearchBar"] = TableWidgetHasSearchBar
    globals()["TimeseriesWidgetDefinition"] = TimeseriesWidgetDefinition
    globals()["TimeseriesWidgetLegendColumn"] = TimeseriesWidgetLegendColumn
    globals()["TimeseriesWidgetLegendLayout"] = TimeseriesWidgetLegendLayout
    globals()["ToplistWidgetDefinition"] = ToplistWidgetDefinition
    globals()["TreeMapColorBy"] = TreeMapColorBy
    globals()["TreeMapGroupBy"] = TreeMapGroupBy
    globals()["TreeMapSizeBy"] = TreeMapSizeBy
    globals()["TreeMapWidgetDefinition"] = TreeMapWidgetDefinition
    globals()["Widget"] = Widget
    globals()["WidgetAxis"] = WidgetAxis
    globals()["WidgetColorPreference"] = WidgetColorPreference
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetEvent"] = WidgetEvent
    globals()["WidgetEventSize"] = WidgetEventSize
    globals()["WidgetGrouping"] = WidgetGrouping
    globals()["WidgetHorizontalAlign"] = WidgetHorizontalAlign
    globals()["WidgetImageSizing"] = WidgetImageSizing
    globals()["WidgetLayoutType"] = WidgetLayoutType
    globals()["WidgetMargin"] = WidgetMargin
    globals()["WidgetMarker"] = WidgetMarker
    globals()["WidgetMessageDisplay"] = WidgetMessageDisplay
    globals()["WidgetMonitorSummarySort"] = WidgetMonitorSummarySort
    globals()["WidgetNodeType"] = WidgetNodeType
    globals()["WidgetServiceSummaryDisplayFormat"] = WidgetServiceSummaryDisplayFormat
    globals()["WidgetSizeFormat"] = WidgetSizeFormat
    globals()["WidgetSummaryType"] = WidgetSummaryType
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTickEdge"] = WidgetTickEdge
    globals()["WidgetTime"] = WidgetTime
    globals()["WidgetTimeWindows"] = WidgetTimeWindows
    globals()["WidgetVerticalAlign"] = WidgetVerticalAlign
    globals()["WidgetViewMode"] = WidgetViewMode
    globals()["WidgetVizType"] = WidgetVizType


class WidgetDefinition(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
        "filters": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types():
        return {}

    def __init__(self, *args, **kwargs):
        """WidgetDefinition - a model defined in OpenAPI


        :type time: WidgetTime, optional

        :param title: The title of the widget.
        :type title: str, optional

        :type title_align: WidgetTextAlign, optional

        :param title_size: The size of the title.
        :type title_size: str, optional

        :param precision: Number of decimals to show. If not defined, the widget uses the raw value.
        :type precision: int, optional

        :type text_align: WidgetTextAlign, optional

        :param unit: Unit to display with the value.
        :type unit: str, optional

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param group: List of tag prefixes to group by.
        :type group: [str], optional

        :type group_by: TreeMapGroupBy, optional

        :param tags: List of tags used to filter the groups reporting a cluster check.
        :type tags: [str], optional

        :param legend_size: Available legend sizes for a widget. Should be one of \"0\", \"2\", \"4\", \"8\", \"16\", or \"auto\".
        :type legend_size: str, optional

        :param markers: List of markers.
        :type markers: [WidgetMarker], optional

        :param show_legend: Whether or not to display the legend on this widget.
        :type show_legend: bool, optional

        :type xaxis: WidgetAxis, optional

        :type yaxis: WidgetAxis, optional

        :type event_size: WidgetEventSize, optional

        :param tags_execution: The execution method for multi-value filters. Can be either and or or.
        :type tags_execution: str, optional

        :param color: Color of the text.
        :type color: str, optional

        :param font_size: Size of the text.
        :type font_size: str, optional

        :param background_color: Background color of the note.
        :type background_color: str, optional

        :param banner_img: URL of image to display as a banner for the group.
        :type banner_img: str, optional

        :param show_title: Whether to show the title or not. If omitted the server will use the default value of True.
        :type show_title: bool, optional

        :param events: List of widget events.
        :type events: [WidgetEvent], optional

        :param no_group_hosts: Whether to show the hosts that don’t fit in a group.
        :type no_group_hosts: bool, optional

        :param no_metric_hosts: Whether to show the hosts with no metrics.
        :type no_metric_hosts: bool, optional

        :type node_type: WidgetNodeType, optional

        :param notes: Notes on the title.
        :type notes: str, optional

        :param scope: List of tags used to filter the map.
        :type scope: [str], optional

        :param has_background: Whether to display a background or not. If omitted the server will use the default value of True.
        :type has_background: bool, optional

        :param has_border: Whether to display a border or not. If omitted the server will use the default value of True.
        :type has_border: bool, optional

        :type horizontal_align: WidgetHorizontalAlign, optional

        :type margin: WidgetMargin, optional

        :type sizing: WidgetImageSizing, optional

        :param url_dark_theme: URL of the image in dark mode.
        :type url_dark_theme: str, optional

        :type vertical_align: WidgetVerticalAlign, optional

        :param columns: Which columns to display on the widget.
        :type columns: [str], optional

        :param indexes: An array of index names to query in the stream. Use [] to query all indexes at once.
        :type indexes: [str], optional

        :param logset: ID of the log set to use.
        :type logset: str, optional

        :type message_display: WidgetMessageDisplay, optional

        :param show_date_column: Whether to show the date column or not
        :type show_date_column: bool, optional

        :param show_message_column: Whether to show the message column or not
        :type show_message_column: bool, optional

        :type sort: WidgetMonitorSummarySort, optional

        :type color_preference: WidgetColorPreference, optional

        :param count: The number of monitors to display.
        :type count: int, optional

        :type display_format: WidgetServiceSummaryDisplayFormat, optional

        :param hide_zero_counts: Whether to show counts of 0 or not.
        :type hide_zero_counts: bool, optional

        :param show_last_triggered: Whether to show the time that has elapsed since the monitor/group triggered.
        :type show_last_triggered: bool, optional

        :param start: The start of the list. Typically 0.
        :type start: int, optional

        :type summary_type: WidgetSummaryType, optional

        :param has_padding: Whether to add padding or not. If omitted the server will use the default value of True.
        :type has_padding: bool, optional

        :param show_tick: Whether to show a tick or not.
        :type show_tick: bool, optional

        :type tick_edge: WidgetTickEdge, optional

        :param tick_pos: Where to position the tick on an edge.
        :type tick_pos: str, optional

        :param autoscale: Whether to use auto-scaling or not.
        :type autoscale: bool, optional

        :param custom_unit: Display a unit of your choice on the widget.
        :type custom_unit: str, optional

        :param color_by_groups: List of groups used for colors.
        :type color_by_groups: [str], optional

        :param global_time_target: Defined global time target.
        :type global_time_target: str, optional

        :param show_error_budget: Defined error budget.
        :type show_error_budget: bool, optional

        :param slo_id: ID of the SLO displayed.
        :type slo_id: str, optional

        :param time_windows: Times being monitored.
        :type time_windows: [WidgetTimeWindows], optional

        :type view_mode: WidgetViewMode, optional

        :param show_breakdown: Whether to show the latency breakdown or not.
        :type show_breakdown: bool, optional

        :param show_distribution: Whether to show the latency distribution or not.
        :type show_distribution: bool, optional

        :param show_errors: Whether to show the error metrics or not.
        :type show_errors: bool, optional

        :param show_hits: Whether to show the hits metrics or not.
        :type show_hits: bool, optional

        :param show_latency: Whether to show the latency metrics or not.
        :type show_latency: bool, optional

        :param show_resource_list: Whether to show the resource list or not.
        :type show_resource_list: bool, optional

        :type size_format: WidgetSizeFormat, optional

        :param hide_total: Show the total value in this widget.
        :type hide_total: bool, optional

        :type legend: SunburstWidgetLegend, optional

        :type has_search_bar: TableWidgetHasSearchBar, optional

        :param legend_columns: Columns displayed in the legend.
        :type legend_columns: [TimeseriesWidgetLegendColumn], optional

        :type legend_layout: TimeseriesWidgetLegendLayout, optional

        :type right_yaxis: WidgetAxis, optional

        :type color_by: TreeMapColorBy, optional

        :type size_by: TreeMapSizeBy, optional

        :param alert_id: ID of the alert to use in the widget.
        :type alert_id: str, optional

        :type type: FunnelWidgetDefinitionType, optional

        :type viz_type: WidgetVizType, optional

        :param requests: Request payload used to query items.
        :type requests: [FunnelWidgetRequest], optional

        :param check: Name of the check to use in the widget.
        :type check: str, optional

        :type grouping: WidgetGrouping, optional

        :param query: Query to filter the monitors with.
        :type query: str, optional

        :param text: Text to display.
        :type text: str, optional

        :type style: HostMapWidgetDefinitionStyle, optional

        :type view: GeomapWidgetDefinitionView, optional

        :type layout_type: WidgetLayoutType, optional

        :param widgets: List of widget groups.
        :type widgets: [Widget], optional

        :param url: URL of the image.
        :type url: str, optional

        :param content: Content of the note.
        :type content: str, optional

        :param view_type: Type of view displayed by the widget. If omitted the server will use the default value of "detail".
        :type view_type: str, optional

        :param filters: Your environment and primary tag (or * if enabled for your account).
        :type filters: [str], optional

        :param service: APM service.
        :type service: str, optional

        :param env: APM environment.
        :type env: str, optional

        :param span_name: APM span name.
        :type span_name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                AlertGraphWidgetDefinition,
                AlertValueWidgetDefinition,
                ChangeWidgetDefinition,
                CheckStatusWidgetDefinition,
                DistributionWidgetDefinition,
                EventStreamWidgetDefinition,
                EventTimelineWidgetDefinition,
                FreeTextWidgetDefinition,
                FunnelWidgetDefinition,
                GeomapWidgetDefinition,
                GroupWidgetDefinition,
                HeatMapWidgetDefinition,
                HostMapWidgetDefinition,
                IFrameWidgetDefinition,
                ImageWidgetDefinition,
                ListStreamWidgetDefinition,
                LogStreamWidgetDefinition,
                MonitorSummaryWidgetDefinition,
                NoteWidgetDefinition,
                QueryValueWidgetDefinition,
                SLOWidgetDefinition,
                ScatterPlotWidgetDefinition,
                ServiceMapWidgetDefinition,
                ServiceSummaryWidgetDefinition,
                SunburstWidgetDefinition,
                TableWidgetDefinition,
                TimeseriesWidgetDefinition,
                ToplistWidgetDefinition,
                TreeMapWidgetDefinition,
            ],
        }
