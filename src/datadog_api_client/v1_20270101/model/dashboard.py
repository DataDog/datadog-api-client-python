# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.dashboard_default_timeframe_setting import DashboardDefaultTimeframeSetting
    from datadog_api_client.v1.model.dashboard_experience_type import DashboardExperienceType
    from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
    from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
    from datadog_api_client.v1.model.dashboard20270101_schema_version import Dashboard20270101SchemaVersion
    from datadog_api_client.v1.model.dashboard_tab import DashboardTab
    from datadog_api_client.v1.model.dashboard_template_variable_preset import DashboardTemplateVariablePreset
    from datadog_api_client.v1.model.dashboard_template_variable import DashboardTemplateVariable
    from datadog_api_client.v1_20270101.model.dashboard_backend_widget import DashboardBackendWidget
    from datadog_api_client.v1.model.dashboard_live_timeframe import DashboardLiveTimeframe
    from datadog_api_client.v1.model.dashboard_fixed_timeframe import DashboardFixedTimeframe
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


class Dashboard(ModelNormal):
    validations = {
        "tabs": {
            "max_items": 100,
        },
        "tags": {
            "max_items": 5,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_default_timeframe_setting import DashboardDefaultTimeframeSetting
        from datadog_api_client.v1.model.dashboard_experience_type import DashboardExperienceType
        from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
        from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
        from datadog_api_client.v1.model.dashboard20270101_schema_version import Dashboard20270101SchemaVersion
        from datadog_api_client.v1.model.dashboard_tab import DashboardTab
        from datadog_api_client.v1.model.dashboard_template_variable_preset import DashboardTemplateVariablePreset
        from datadog_api_client.v1.model.dashboard_template_variable import DashboardTemplateVariable
        from datadog_api_client.v1_20270101.model.dashboard_backend_widget import DashboardBackendWidget

        return {
            "author_handle": (str,),
            "author_name": (str, none_type),
            "created_at": (datetime,),
            "default_timeframe": (DashboardDefaultTimeframeSetting,),
            "description": (str, none_type),
            "experience_type": (DashboardExperienceType,),
            "id": (str,),
            "is_read_only": (bool,),
            "layout_type": (DashboardLayoutType,),
            "modified_at": (datetime,),
            "notify_list": ([str], none_type),
            "reflow_type": (DashboardReflowType,),
            "restricted_roles": ([str],),
            "schema_version": (Dashboard20270101SchemaVersion,),
            "tabs": ([DashboardTab], none_type),
            "tags": ([str], none_type),
            "template_variable_presets": ([DashboardTemplateVariablePreset], none_type),
            "template_variables": ([DashboardTemplateVariable], none_type),
            "title": (str,),
            "url": (str,),
            "widgets": ([DashboardBackendWidget],),
        }

    attribute_map = {
        "author_handle": "author_handle",
        "author_name": "author_name",
        "created_at": "created_at",
        "default_timeframe": "default_timeframe",
        "description": "description",
        "experience_type": "experience_type",
        "id": "id",
        "is_read_only": "is_read_only",
        "layout_type": "layout_type",
        "modified_at": "modified_at",
        "notify_list": "notify_list",
        "reflow_type": "reflow_type",
        "restricted_roles": "restricted_roles",
        "schema_version": "schema_version",
        "tabs": "tabs",
        "tags": "tags",
        "template_variable_presets": "template_variable_presets",
        "template_variables": "template_variables",
        "title": "title",
        "url": "url",
        "widgets": "widgets",
    }
    read_only_vars = {
        "author_handle",
        "author_name",
        "created_at",
        "experience_type",
        "id",
        "modified_at",
        "url",
    }

    def __init__(
        self_,
        layout_type: DashboardLayoutType,
        schema_version: Dashboard20270101SchemaVersion,
        title: str,
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
        author_handle: Union[str, UnsetType] = unset,
        author_name: Union[str, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        default_timeframe: Union[
            DashboardDefaultTimeframeSetting, DashboardLiveTimeframe, DashboardFixedTimeframe, UnsetType
        ] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        experience_type: Union[DashboardExperienceType, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_read_only: Union[bool, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        notify_list: Union[List[str], none_type, UnsetType] = unset,
        reflow_type: Union[DashboardReflowType, UnsetType] = unset,
        restricted_roles: Union[List[str], UnsetType] = unset,
        tabs: Union[List[DashboardTab], none_type, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        template_variable_presets: Union[List[DashboardTemplateVariablePreset], none_type, UnsetType] = unset,
        template_variables: Union[List[DashboardTemplateVariable], none_type, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A dashboard is Datadog’s tool for visually tracking, analyzing, and displaying
        key performance metrics, which enable you to monitor the health of your infrastructure.

        :param author_handle: Identifier of the dashboard author.
        :type author_handle: str, optional

        :param author_name: Name of the dashboard author.
        :type author_name: str, none_type, optional

        :param created_at: Creation date of the dashboard.
        :type created_at: datetime, optional

        :param default_timeframe: The default timeframe applied when opening the dashboard. Set to ``null`` to clear the dashboard's default timeframe.
        :type default_timeframe: DashboardDefaultTimeframeSetting, optional

        :param description: Description of the dashboard.
        :type description: str, none_type, optional

        :param experience_type: The experience type of the dashboard.
        :type experience_type: DashboardExperienceType, optional

        :param id: ID of the dashboard.
        :type id: str, optional

        :param is_read_only: Whether this dashboard is read-only. If True, only the author and admins can make changes to it.

            This property is deprecated; please use the `Restriction Policies API <https://docs.datadoghq.com/api/latest/restriction-policies/>`_ instead to manage write authorization for individual dashboards. **Deprecated**.
        :type is_read_only: bool, optional

        :param layout_type: Layout type of the dashboard.
        :type layout_type: DashboardLayoutType

        :param modified_at: Modification date of the dashboard.
        :type modified_at: datetime, optional

        :param notify_list: List of handles of users to notify when changes are made to this dashboard.
        :type notify_list: [str], none_type, optional

        :param reflow_type: Reflow type for a **new dashboard layout** dashboard. Set this only when layout type is 'ordered'.
            If set to 'fixed', the dashboard expects all widgets to have a layout, and if it's set to 'auto',
            widgets should not have layouts.
        :type reflow_type: DashboardReflowType, optional

        :param restricted_roles: A list of role identifiers. Only the author and users associated with at least one of these roles can edit this dashboard.
        :type restricted_roles: [str], optional

        :param schema_version: Test-only request-body discriminator for the dashboard schema-versioning proof of concept.
        :type schema_version: Dashboard20270101SchemaVersion

        :param tabs: List of tabs for organizing dashboard widgets into groups.
        :type tabs: [DashboardTab], none_type, optional

        :param tags: List of team names representing ownership of a dashboard.
        :type tags: [str], none_type, optional

        :param template_variable_presets: Array of template variables saved views.
        :type template_variable_presets: [DashboardTemplateVariablePreset], none_type, optional

        :param template_variables: List of template variables for this dashboard.
        :type template_variables: [DashboardTemplateVariable], none_type, optional

        :param title: Title of the dashboard.
        :type title: str

        :param url: The URL of the dashboard.
        :type url: str, optional

        :param widgets: List of widgets to display on the dashboard.
        :type widgets: [DashboardBackendWidget]
        """
        if author_handle is not unset:
            kwargs["author_handle"] = author_handle
        if author_name is not unset:
            kwargs["author_name"] = author_name
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if default_timeframe is not unset:
            kwargs["default_timeframe"] = default_timeframe
        if description is not unset:
            kwargs["description"] = description
        if experience_type is not unset:
            kwargs["experience_type"] = experience_type
        if id is not unset:
            kwargs["id"] = id
        if is_read_only is not unset:
            kwargs["is_read_only"] = is_read_only
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if notify_list is not unset:
            kwargs["notify_list"] = notify_list
        if reflow_type is not unset:
            kwargs["reflow_type"] = reflow_type
        if restricted_roles is not unset:
            kwargs["restricted_roles"] = restricted_roles
        if tabs is not unset:
            kwargs["tabs"] = tabs
        if tags is not unset:
            kwargs["tags"] = tags
        if template_variable_presets is not unset:
            kwargs["template_variable_presets"] = template_variable_presets
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)

        self_.layout_type = layout_type
        self_.schema_version = schema_version
        self_.title = title
        self_.widgets = widgets
