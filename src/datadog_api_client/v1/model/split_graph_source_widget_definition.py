# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SplitGraphSourceWidgetDefinition(ModelComposed):
    def __init__(self, **kwargs):
        """
        The original widget we are splitting on.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: Array of one request object to display in the widget.

            See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json)
             to learn how to build the `REQUEST_SCHEMA`.
        :type requests: [ChangeWidgetRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the change widget.
        :type type: ChangeWidgetDefinitionType

        :param style: The style to apply to the widget.
        :type style: GeomapWidgetDefinitionStyle

        :param view: The view of the world that the map should render.
        :type view: GeomapWidgetDefinitionView

        :param autoscale: Whether to use auto-scaling or not.
        :type autoscale: bool, optional

        :param custom_unit: Display a unit of your choice on the widget.
        :type custom_unit: str, optional

        :param precision: Number of decimals to show. If not defined, the widget uses the raw value.
        :type precision: int, optional

        :param text_align: How to align the text on the widget.
        :type text_align: WidgetTextAlign, optional

        :param timeseries_background: Set a timeseries on the widget background.
        :type timeseries_background: TimeseriesBackground, optional

        :param color_by_groups: List of groups used for colors.
        :type color_by_groups: [str], optional

        :param xaxis: Axis controls for the widget.
        :type xaxis: WidgetAxis, optional

        :param yaxis: Axis controls for the widget.
        :type yaxis: WidgetAxis, optional

        :param hide_total: Show the total value in this widget.
        :type hide_total: bool, optional

        :param legend: Configuration of the legend.
        :type legend: SunburstWidgetLegend, optional

        :param has_search_bar: Controls the display of the search bar.
        :type has_search_bar: TableWidgetHasSearchBar, optional

        :param events: List of widget events.
        :type events: [WidgetEvent], optional

        :param legend_columns: Columns displayed in the legend.
        :type legend_columns: [TimeseriesWidgetLegendColumn], optional

        :param legend_layout: Layout of the legend.
        :type legend_layout: TimeseriesWidgetLegendLayout, optional

        :param legend_size: Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
        :type legend_size: str, optional

        :param markers: List of markers.
        :type markers: [WidgetMarker], optional

        :param right_yaxis: Axis controls for the widget.
        :type right_yaxis: WidgetAxis, optional

        :param show_legend: (screenboard only) Show the legend for this widget.
        :type show_legend: bool, optional

        :param color_by: (deprecated) The attribute formerly used to determine color in the widget.
        :type color_by: TreeMapColorBy, optional

        :param group_by: (deprecated) The attribute formerly used to group elements in the widget.
        :type group_by: TreeMapGroupBy, optional

        :param size_by: (deprecated) The attribute formerly used to determine size in the widget.
        :type size_by: TreeMapSizeBy, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
        from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
        from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition
        from datadog_api_client.v1.model.scatter_plot_widget_definition import ScatterPlotWidgetDefinition
        from datadog_api_client.v1.model.sunburst_widget_definition import SunburstWidgetDefinition
        from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
        from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
        from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition
        from datadog_api_client.v1.model.tree_map_widget_definition import TreeMapWidgetDefinition

        return {
            "oneOf": [
                ChangeWidgetDefinition,
                GeomapWidgetDefinition,
                QueryValueWidgetDefinition,
                ScatterPlotWidgetDefinition,
                SunburstWidgetDefinition,
                TableWidgetDefinition,
                TimeseriesWidgetDefinition,
                ToplistWidgetDefinition,
                TreeMapWidgetDefinition,
            ],
        }
