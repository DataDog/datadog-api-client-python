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

        Keyword Args:
            time (WidgetTime): [optional]
            title (str): [optional] The title of the widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] The size of the title.
            precision (int): [optional] Number of decimals to show. If not defined, the widget uses the raw value.
            text_align (WidgetTextAlign): [optional]
            unit (str): [optional] Unit to display with the value.
            custom_links ([WidgetCustomLink]): [optional] List of custom links.
            group ([str]): [optional] List of tag prefixes to group by.
            group_by (TreeMapGroupBy): [optional]
            tags ([str]): [optional] List of tags used to filter the groups reporting a cluster check.
            legend_size (str): [optional] Available legend sizes for a widget. Should be one of \"0\", \"2\", \"4\", \"8\", \"16\", or \"auto\".
            markers ([WidgetMarker]): [optional] List of markers.
            show_legend (bool): [optional] Whether or not to display the legend on this widget.
            xaxis (WidgetAxis): [optional]
            yaxis (WidgetAxis): [optional]
            event_size (WidgetEventSize): [optional]
            tags_execution (str): [optional] The execution method for multi-value filters. Can be either and or or.
            color (str): [optional] Color of the text.
            font_size (str): [optional] Size of the text.
            background_color (str): [optional] Background color of the note.
            banner_img (str): [optional] URL of image to display as a banner for the group.
            show_title (bool): [optional] Whether to show the title or not. If omitted the server will use the default value of True.
            events ([WidgetEvent]): [optional] List of widget events.
            no_group_hosts (bool): [optional] Whether to show the hosts that don’t fit in a group.
            no_metric_hosts (bool): [optional] Whether to show the hosts with no metrics.
            node_type (WidgetNodeType): [optional]
            notes (str): [optional] Notes on the title.
            scope ([str]): [optional] List of tags used to filter the map.
            has_background (bool): [optional] Whether to display a background or not. If omitted the server will use the default value of True.
            has_border (bool): [optional] Whether to display a border or not. If omitted the server will use the default value of True.
            horizontal_align (WidgetHorizontalAlign): [optional]
            margin (WidgetMargin): [optional]
            sizing (WidgetImageSizing): [optional]
            url_dark_theme (str): [optional] URL of the image in dark mode.
            vertical_align (WidgetVerticalAlign): [optional]
            columns ([str]): [optional] Which columns to display on the widget.
            indexes ([str]): [optional] An array of index names to query in the stream. Use [] to query all indexes at once.
            logset (str): [optional] ID of the log set to use.
            message_display (WidgetMessageDisplay): [optional]
            show_date_column (bool): [optional] Whether to show the date column or not
            show_message_column (bool): [optional] Whether to show the message column or not
            sort (WidgetMonitorSummarySort): [optional]
            color_preference (WidgetColorPreference): [optional]
            count (int): [optional] The number of monitors to display.
            display_format (WidgetServiceSummaryDisplayFormat): [optional]
            hide_zero_counts (bool): [optional] Whether to show counts of 0 or not.
            show_last_triggered (bool): [optional] Whether to show the time that has elapsed since the monitor/group triggered.
            start (int): [optional] The start of the list. Typically 0.
            summary_type (WidgetSummaryType): [optional]
            has_padding (bool): [optional] Whether to add padding or not. If omitted the server will use the default value of True.
            show_tick (bool): [optional] Whether to show a tick or not.
            tick_edge (WidgetTickEdge): [optional]
            tick_pos (str): [optional] Where to position the tick on an edge.
            autoscale (bool): [optional] Whether to use auto-scaling or not.
            custom_unit (str): [optional] Display a unit of your choice on the widget.
            color_by_groups ([str]): [optional] List of groups used for colors.
            global_time_target (str): [optional] Defined global time target.
            show_error_budget (bool): [optional] Defined error budget.
            slo_id (str): [optional] ID of the SLO displayed.
            time_windows ([WidgetTimeWindows]): [optional] Times being monitored.
            view_mode (WidgetViewMode): [optional]
            show_breakdown (bool): [optional] Whether to show the latency breakdown or not.
            show_distribution (bool): [optional] Whether to show the latency distribution or not.
            show_errors (bool): [optional] Whether to show the error metrics or not.
            show_hits (bool): [optional] Whether to show the hits metrics or not.
            show_latency (bool): [optional] Whether to show the latency metrics or not.
            show_resource_list (bool): [optional] Whether to show the resource list or not.
            size_format (WidgetSizeFormat): [optional]
            hide_total (bool): [optional] Show the total value in this widget.
            legend (SunburstWidgetLegend): [optional]
            has_search_bar (TableWidgetHasSearchBar): [optional]
            legend_columns ([TimeseriesWidgetLegendColumn]): [optional] Columns displayed in the legend.
            legend_layout (TimeseriesWidgetLegendLayout): [optional]
            right_yaxis (WidgetAxis): [optional]
            color_by (TreeMapColorBy): [optional]
            size_by (TreeMapSizeBy): [optional]
            alert_id (str): [optional] ID of the alert to use in the widget.
            type (FunnelWidgetDefinitionType): [optional]
            viz_type (WidgetVizType): [optional]
            requests ([FunnelWidgetRequest]): [optional] Request payload used to query items.
            check (str): [optional] Name of the check to use in the widget.
            grouping (WidgetGrouping): [optional]
            query (str): [optional] Query to filter the monitors with.
            text (str): [optional] Text to display.
            style (HostMapWidgetDefinitionStyle): [optional]
            view (GeomapWidgetDefinitionView): [optional]
            layout_type (WidgetLayoutType): [optional]
            widgets ([Widget]): [optional] List of widget groups.
            url (str): [optional] URL of the image.
            content (str): [optional] Content of the note.
            view_type (str): [optional] Type of view displayed by the widget. If omitted the server will use the default value of "detail".
            filters ([str]): [optional] Your environment and primary tag (or * if enabled for your account).
            service (str): [optional] APM service.
            env (str): [optional] APM environment.
            span_name (str): [optional] APM span name.
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
