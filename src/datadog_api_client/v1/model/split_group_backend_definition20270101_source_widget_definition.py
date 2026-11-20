# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SplitGroupBackendDefinition20270101SourceWidgetDefinition(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [BarChartBackendRequest]

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: BarChartBackendDefinitionStyle, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: BarChartBackendDefinitionType

        :param legend_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_columns: [TimeseriesWidgetLegendColumn], optional

        :param legend_layout: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_layout: DistributionBackendDefinitionLegendLayout, optional

        :param legend_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_size: str, optional

        :param markers: Test-only generated schema for the dashboard versioning proof of concept.
        :type markers: [WidgetMarker], optional

        :param show_legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_legend: bool, optional

        :param xaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type xaxis: DistributionXAxis, optional

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: BackendDistributionYAxis, optional

        :param view: Test-only generated schema for the dashboard versioning proof of concept.
        :type view: GeomapView

        :param color: Test-only generated schema for the dashboard versioning proof of concept.
        :type color: HeatgridColorConfig, optional

        :param label_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type label_column: HeatgridLabelColumnConfig, optional

        :param legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend: HeatgridLegendConfig, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: HeatgridSortAndOrderBy

        :param auto_horizontal_scrolling: Test-only generated schema for the dashboard versioning proof of concept.
        :type auto_horizontal_scrolling: bool, optional

        :param has_search_bar: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_search_bar: HasSearchBar, optional

        :param num_sticky_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type num_sticky_columns: float, optional

        :param autoscale: Test-only generated schema for the dashboard versioning proof of concept.
        :type autoscale: bool, optional

        :param custom_unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_unit: str, optional

        :param precision: Test-only generated schema for the dashboard versioning proof of concept.
        :type precision: float, optional

        :param text_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_align: WidgetTextAlign, optional

        :param timeseries_background: Test-only generated schema for the dashboard versioning proof of concept.
        :type timeseries_background: TimeseriesBackground, optional

        :param color_by_groups: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_by_groups: [str], optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional

        :param hide_total: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_total: bool, optional

        :param anomaly_detection: Test-only generated schema for the dashboard versioning proof of concept.
        :type anomaly_detection: AnomalyDetectionConfig, optional

        :param events: Test-only generated schema for the dashboard versioning proof of concept.
        :type events: [LegacyEventOverlayQuery], optional

        :param right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type right_yaxis: BackendTimeseriesAxisDefinition, optional

        :param color_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_by: TreemapBackendDefinitionColorBy, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: TreemapBackendDefinitionGroupBy, optional

        :param size_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type size_by: TreemapBackendDefinitionSizeBy, optional

        :param specification: Test-only generated schema for the dashboard versioning proof of concept.
        :type specification: WildcardBackendDefinitionSpecification
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
        from datadog_api_client.v1.model.bar_chart_backend_definition import BarChartBackendDefinition
        from datadog_api_client.v1.model.change_backend_definition import ChangeBackendDefinition
        from datadog_api_client.v1.model.distribution_backend_definition import DistributionBackendDefinition
        from datadog_api_client.v1.model.geomap_backend_definition import GeomapBackendDefinition
        from datadog_api_client.v1.model.heatgrid_definition import HeatgridDefinition
        from datadog_api_client.v1.model.query_table_backend_definition import QueryTableBackendDefinition
        from datadog_api_client.v1.model.query_value_backend_definition import QueryValueBackendDefinition
        from datadog_api_client.v1.model.scatterplot_backend_definition import ScatterplotBackendDefinition
        from datadog_api_client.v1.model.sunburst_backend_definition import SunburstBackendDefinition
        from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
        from datadog_api_client.v1.model.toplist_backend_definition import ToplistBackendDefinition
        from datadog_api_client.v1.model.treemap_backend_definition import TreemapBackendDefinition
        from datadog_api_client.v1.model.wildcard_backend_definition import WildcardBackendDefinition

        return {
            "oneOf": [
                BarChartBackendDefinition,
                ChangeBackendDefinition,
                DistributionBackendDefinition,
                GeomapBackendDefinition,
                HeatgridDefinition,
                QueryTableBackendDefinition,
                QueryValueBackendDefinition,
                ScatterplotBackendDefinition,
                SunburstBackendDefinition,
                TimeseriesWidgetDefinition,
                ToplistBackendDefinition,
                TreemapBackendDefinition,
                WildcardBackendDefinition,
            ],
        }
