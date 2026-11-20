# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.group_backend_definition_default_state import (
        GroupBackendDefinitionDefaultState,
    )
    from datadog_api_client.v1_20270101.model.layout_type import LayoutType
    from datadog_api_client.v1_20270101.model.group_backend_definition_type import GroupBackendDefinitionType
    from datadog_api_client.v1_20270101.model.dashboard_backend_widget import DashboardBackendWidget
    from datadog_api_client.v1_20270101.model.alert_graph_backend_widget import AlertGraphBackendWidget
    from datadog_api_client.v1_20270101.model.alert_value_backend_widget import AlertValueBackendWidget
    from datadog_api_client.v1_20270101.model.bar_chart_backend_widget import BarChartBackendWidget
    from datadog_api_client.v1_20270101.model.change_backend_widget import ChangeBackendWidget
    from datadog_api_client.v1_20270101.model.check_status_backend_widget import CheckStatusBackendWidget
    from datadog_api_client.v1_20270101.model.cohort_backend_widget import CohortBackendWidget
    from datadog_api_client.v1_20270101.model.distribution_backend_widget import DistributionBackendWidget
    from datadog_api_client.v1_20270101.model.embedded_app_backend_widget import EmbeddedAppBackendWidget
    from datadog_api_client.v1_20270101.model.event_stream import EventStream
    from datadog_api_client.v1_20270101.model.event_timeline_backend_widget import EventTimelineBackendWidget
    from datadog_api_client.v1_20270101.model.free_text_backend_widget import FreeTextBackendWidget
    from datadog_api_client.v1_20270101.model.funnel_backend_widget import FunnelBackendWidget
    from datadog_api_client.v1_20270101.model.geomap_backend_widget import GeomapBackendWidget
    from datadog_api_client.v1_20270101.model.group_backend_widget import GroupBackendWidget
    from datadog_api_client.v1_20270101.model.heatgrid_backend_widget import HeatgridBackendWidget
    from datadog_api_client.v1_20270101.model.heatmap_backend_widget import HeatmapBackendWidget
    from datadog_api_client.v1_20270101.model.hostmap_backend_widget import HostmapBackendWidget
    from datadog_api_client.v1_20270101.model.iframe_backend_widget import IframeBackendWidget
    from datadog_api_client.v1_20270101.model.image_backend_widget import ImageBackendWidget
    from datadog_api_client.v1_20270101.model.journey_map_backend_widget import JourneyMapBackendWidget
    from datadog_api_client.v1_20270101.model.list_stream_backend_widget import ListStreamBackendWidget
    from datadog_api_client.v1_20270101.model.log_stream import LogStream
    from datadog_api_client.v1_20270101.model.manage_status_backend_widget import ManageStatusBackendWidget
    from datadog_api_client.v1_20270101.model.note_backend_widget import NoteBackendWidget
    from datadog_api_client.v1_20270101.model.point_plot_backend_widget import PointPlotBackendWidget
    from datadog_api_client.v1_20270101.model.powerpack_backend_widget import PowerpackBackendWidget
    from datadog_api_client.v1_20270101.model.query_table_backend_widget import QueryTableBackendWidget
    from datadog_api_client.v1_20270101.model.query_value_backend_widget import QueryValueBackendWidget
    from datadog_api_client.v1_20270101.model.retention_curve_backend_widget import RetentionCurveBackendWidget
    from datadog_api_client.v1_20270101.model.run_workflow_backend_widget import RunWorkflowBackendWidget
    from datadog_api_client.v1_20270101.model.sankey_backend_widget import SankeyBackendWidget
    from datadog_api_client.v1_20270101.model.scatterplot_backend_widget import ScatterplotBackendWidget
    from datadog_api_client.v1_20270101.model.service_map_backend_widget import ServiceMapBackendWidget
    from datadog_api_client.v1_20270101.model.slo_backend_widget import SloBackendWidget
    from datadog_api_client.v1_20270101.model.slo_list_backend_widget import SloListBackendWidget
    from datadog_api_client.v1_20270101.model.split_group_backend_widget import SplitGroupBackendWidget
    from datadog_api_client.v1_20270101.model.sunburst_backend_widget import SunburstBackendWidget
    from datadog_api_client.v1_20270101.model.timeseries_backend_widget import TimeseriesBackendWidget
    from datadog_api_client.v1_20270101.model.toplist_backend_widget import ToplistBackendWidget
    from datadog_api_client.v1_20270101.model.topology_map_backend_widget import TopologyMapBackendWidget
    from datadog_api_client.v1_20270101.model.service_summary_backend_widget import ServiceSummaryBackendWidget
    from datadog_api_client.v1_20270101.model.treemap_backend_widget import TreemapBackendWidget
    from datadog_api_client.v1_20270101.model.wildcard_backend_widget import WildcardBackendWidget


class GroupBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.group_backend_definition_default_state import (
            GroupBackendDefinitionDefaultState,
        )
        from datadog_api_client.v1_20270101.model.layout_type import LayoutType
        from datadog_api_client.v1_20270101.model.group_backend_definition_type import GroupBackendDefinitionType
        from datadog_api_client.v1_20270101.model.dashboard_backend_widget import DashboardBackendWidget

        return {
            "background_color": (str,),
            "banner_img": (str,),
            "default_state": (GroupBackendDefinitionDefaultState,),
            "description": (str,),
            "layout_type": (LayoutType,),
            "show_title": (bool,),
            "title": (str,),
            "type": (GroupBackendDefinitionType,),
            "widgets": ([DashboardBackendWidget],),
        }

    attribute_map = {
        "background_color": "background_color",
        "banner_img": "banner_img",
        "default_state": "default_state",
        "description": "description",
        "layout_type": "layout_type",
        "show_title": "show_title",
        "title": "title",
        "type": "type",
        "widgets": "widgets",
    }

    def __init__(
        self_,
        layout_type: LayoutType,
        type: GroupBackendDefinitionType,
        widgets: List[
            Union[
                DashboardBackendWidget,
                AlertGraphBackendWidget,
                AlertValueBackendWidget,
                BarChartBackendWidget,
                ChangeBackendWidget,
                CheckStatusBackendWidget,
                CohortBackendWidget,
                DistributionBackendWidget,
                EmbeddedAppBackendWidget,
                EventStream,
                EventTimelineBackendWidget,
                FreeTextBackendWidget,
                FunnelBackendWidget,
                GeomapBackendWidget,
                GroupBackendWidget,
                HeatgridBackendWidget,
                HeatmapBackendWidget,
                HostmapBackendWidget,
                IframeBackendWidget,
                ImageBackendWidget,
                JourneyMapBackendWidget,
                ListStreamBackendWidget,
                LogStream,
                ManageStatusBackendWidget,
                NoteBackendWidget,
                PointPlotBackendWidget,
                PowerpackBackendWidget,
                QueryTableBackendWidget,
                QueryValueBackendWidget,
                RetentionCurveBackendWidget,
                RunWorkflowBackendWidget,
                SankeyBackendWidget,
                ScatterplotBackendWidget,
                ServiceMapBackendWidget,
                SloBackendWidget,
                SloListBackendWidget,
                SplitGroupBackendWidget,
                SunburstBackendWidget,
                TimeseriesBackendWidget,
                ToplistBackendWidget,
                TopologyMapBackendWidget,
                ServiceSummaryBackendWidget,
                TreemapBackendWidget,
                WildcardBackendWidget,
            ]
        ],
        background_color: Union[str, UnsetType] = unset,
        banner_img: Union[str, UnsetType] = unset,
        default_state: Union[GroupBackendDefinitionDefaultState, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        show_title: Union[bool, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param background_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type background_color: str, optional

        :param banner_img: Test-only generated schema for the dashboard versioning proof of concept.
        :type banner_img: str, optional

        :param default_state: Test-only generated schema for the dashboard versioning proof of concept.
        :type default_state: GroupBackendDefinitionDefaultState, optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param layout_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type layout_type: LayoutType

        :param show_title: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_title: bool, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: GroupBackendDefinitionType

        :param widgets: Test-only generated schema for the dashboard versioning proof of concept.
        :type widgets: [DashboardBackendWidget]
        """
        if background_color is not unset:
            kwargs["background_color"] = background_color
        if banner_img is not unset:
            kwargs["banner_img"] = banner_img
        if default_state is not unset:
            kwargs["default_state"] = default_state
        if description is not unset:
            kwargs["description"] = description
        if show_title is not unset:
            kwargs["show_title"] = show_title
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.layout_type = layout_type
        self_.type = type
        self_.widgets = widgets
