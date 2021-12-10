# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
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

    Attributes:
      allowed_values (dict): The key is the name of the attribute. The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      validations (dict): The key is the name of the attribute. The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

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
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {}

    def __init__(self, *args, **kwargs):
        """WidgetDefinition - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            time (WidgetTime): [optional]
            title (str): The title of the widget.. [optional]
            title_align (WidgetTextAlign): [optional]
            title_size (str): The size of the title.. [optional]
            precision (int): Number of decimals to show. If not defined, the widget uses the raw value.. [optional]
            text_align (WidgetTextAlign): [optional]
            unit (str): Unit to display with the value.. [optional]
            custom_links ([WidgetCustomLink]): List of custom links.. [optional]
            group ([str]): List of tag prefixes to group by.. [optional]
            tags ([str]): List of tags used to filter the groups reporting a cluster check.. [optional]
            legend_size (str): Available legend sizes for a widget. Should be one of \"0\", \"2\", \"4\", \"8\", \"16\", or \"auto\".. [optional]
            markers ([WidgetMarker]): List of markers.. [optional]
            show_legend (bool): Whether or not to display the legend on this widget.. [optional]
            xaxis (WidgetAxis): [optional]
            yaxis (WidgetAxis): [optional]
            event_size (WidgetEventSize): [optional]
            tags_execution (str): The execution method for multi-value filters. Can be either and or or.. [optional]
            color (str): Color of the text.. [optional]
            font_size (str): Size of the text.. [optional]
            background_color (str): Background color of the note.. [optional]
            banner_img (str): URL of image to display as a banner for the group.. [optional]
            show_title (bool): Whether to show the title or not.. [optional] if omitted the server will use the default value of True
            events ([WidgetEvent]): List of widget events.. [optional]
            no_group_hosts (bool): Whether to show the hosts that don’t fit in a group.. [optional]
            no_metric_hosts (bool): Whether to show the hosts with no metrics.. [optional]
            node_type (WidgetNodeType): [optional]
            notes (str): Notes on the title.. [optional]
            scope ([str]): List of tags used to filter the map.. [optional]
            has_background (bool): Whether to display a background or not.. [optional] if omitted the server will use the default value of True
            has_border (bool): Whether to display a border or not.. [optional] if omitted the server will use the default value of True
            horizontal_align (WidgetHorizontalAlign): [optional]
            margin (WidgetMargin): [optional]
            sizing (WidgetImageSizing): [optional]
            url_dark_theme (str): URL of the image in dark mode.. [optional]
            vertical_align (WidgetVerticalAlign): [optional]
            columns ([str]): Which columns to display on the widget.. [optional]
            indexes ([str]): An array of index names to query in the stream. Use [] to query all indexes at once.. [optional]
            logset (str): ID of the log set to use.. [optional]
            message_display (WidgetMessageDisplay): [optional]
            show_date_column (bool): Whether to show the date column or not. [optional]
            show_message_column (bool): Whether to show the message column or not. [optional]
            sort (WidgetMonitorSummarySort): [optional]
            color_preference (WidgetColorPreference): [optional]
            count (int): The number of monitors to display.. [optional]
            display_format (WidgetServiceSummaryDisplayFormat): [optional]
            hide_zero_counts (bool): Whether to show counts of 0 or not.. [optional]
            show_last_triggered (bool): Whether to show the time that has elapsed since the monitor/group triggered.. [optional]
            start (int): The start of the list. Typically 0.. [optional]
            summary_type (WidgetSummaryType): [optional]
            has_padding (bool): Whether to add padding or not.. [optional] if omitted the server will use the default value of True
            show_tick (bool): Whether to show a tick or not.. [optional]
            tick_edge (WidgetTickEdge): [optional]
            tick_pos (str): Where to position the tick on an edge.. [optional]
            autoscale (bool): Whether to use auto-scaling or not.. [optional]
            custom_unit (str): Display a unit of your choice on the widget.. [optional]
            color_by_groups ([str]): List of groups used for colors.. [optional]
            global_time_target (str): Defined global time target.. [optional]
            show_error_budget (bool): Defined error budget.. [optional]
            slo_id (str): ID of the SLO displayed.. [optional]
            time_windows ([WidgetTimeWindows]): Times being monitored.. [optional]
            view_mode (WidgetViewMode): [optional]
            show_breakdown (bool): Whether to show the latency breakdown or not.. [optional]
            show_distribution (bool): Whether to show the latency distribution or not.. [optional]
            show_errors (bool): Whether to show the error metrics or not.. [optional]
            show_hits (bool): Whether to show the hits metrics or not.. [optional]
            show_latency (bool): Whether to show the latency metrics or not.. [optional]
            show_resource_list (bool): Whether to show the resource list or not.. [optional]
            size_format (WidgetSizeFormat): [optional]
            has_search_bar (TableWidgetHasSearchBar): [optional]
            legend_columns ([TimeseriesWidgetLegendColumn]): Columns displayed in the legend.. [optional]
            legend_layout (TimeseriesWidgetLegendLayout): [optional]
            right_yaxis (WidgetAxis): [optional]
            alert_id (str): ID of the alert to use in the widget.. [optional]
            type (FunnelWidgetDefinitionType): [optional]
            viz_type (WidgetVizType): [optional]
            requests ([FunnelWidgetRequest]): Request payload used to query items.. [optional]
            check (str): Name of the check to use in the widget.. [optional]
            group_by (TreeMapGroupBy): [optional]
            grouping (WidgetGrouping): [optional]
            query (str): Query to filter the monitors with.. [optional]
            text (str): Text to display.. [optional]
            style (HostMapWidgetDefinitionStyle): [optional]
            view (GeomapWidgetDefinitionView): [optional]
            layout_type (WidgetLayoutType): [optional]
            widgets ([Widget]): List of widget groups.. [optional]
            url (str): URL of the image.. [optional]
            content (str): Content of the note.. [optional]
            view_type (str): Type of view displayed by the widget.. [optional] if omitted the server will use the default value of "detail"
            filters ([str]): Your environment and primary tag (or * if enabled for your account).. [optional]
            service (str): APM service.. [optional]
            env (str): APM environment.. [optional]
            span_name (str): APM span name.. [optional]
            color_by (TreeMapColorBy): [optional]
            size_by (TreeMapSizeBy): [optional]
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
                TableWidgetDefinition,
                TimeseriesWidgetDefinition,
                ToplistWidgetDefinition,
                TreeMapWidgetDefinition,
            ],
        }
