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
    from datadog_api_client.v1_20270101.model.anomaly_detection_config import AnomalyDetectionConfig
    from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1_20270101.model.legacy_event_overlay_query import LegacyEventOverlayQuery
    from datadog_api_client.v1_20270101.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
    from datadog_api_client.v1_20270101.model.timeseries_widget_legend_layout import TimeseriesWidgetLegendLayout
    from datadog_api_client.v1_20270101.model.widget_marker import WidgetMarker
    from datadog_api_client.v1_20270101.model.timeseries_widget_request import TimeseriesWidgetRequest
    from datadog_api_client.v1_20270101.model.backend_timeseries_axis_definition import BackendTimeseriesAxisDefinition
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
    from datadog_api_client.v1_20270101.model.timeseries_x_axis import TimeseriesXAxis
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.timeseries_widget_formula_request import TimeseriesWidgetFormulaRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_metric_request import TimeseriesWidgetMetricRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_log_request import TimeseriesWidgetLogRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_apm_request import TimeseriesWidgetApmRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_network_request import TimeseriesWidgetNetworkRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_rum_request import TimeseriesWidgetRumRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_security_request import TimeseriesWidgetSecurityRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_compliance_findings_request import (
        TimeseriesWidgetComplianceFindingsRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_event_request import TimeseriesWidgetEventRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_profiling_metrics_request import (
        TimeseriesWidgetProfilingMetricsRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_ci_pipeline_request import (
        TimeseriesWidgetCiPipelineRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_ci_test_request import TimeseriesWidgetCiTestRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_audit_request import TimeseriesWidgetAuditRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_appsec_span_request import (
        TimeseriesWidgetAppsecSpanRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_synthetics_batches_request import (
        TimeseriesWidgetSyntheticsBatchesRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_synthetics_test_runs_request import (
        TimeseriesWidgetSyntheticsTestRunsRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_process_request import TimeseriesWidgetProcessRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_legacy_profile_metrics_request import (
        TimeseriesWidgetLegacyProfileMetricsRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_legacy_event_request import (
        TimeseriesWidgetLegacyEventRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_ddsql_request import TimeseriesWidgetDdsqlRequest
    from datadog_api_client.v1_20270101.model.timeseries_widget_advanced_query_request import (
        TimeseriesWidgetAdvancedQueryRequest,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_local_dataset_request import (
        TimeseriesWidgetLocalDatasetRequest,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of import WidgetTime20270101OneOf
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464103552 import (
        WidgetTime20270101OneOf4464103552,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464104512 import (
        WidgetTime20270101OneOf4464104512,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464105312 import (
        WidgetTime20270101OneOf4464105312,
    )
    from datadog_api_client.v1.model.widget_time20270101_one_of4464105952 import WidgetTime20270101OneOf4464105952


class TimeseriesWidgetDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.anomaly_detection_config import AnomalyDetectionConfig
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.legacy_event_overlay_query import LegacyEventOverlayQuery
        from datadog_api_client.v1_20270101.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
        from datadog_api_client.v1_20270101.model.timeseries_widget_legend_layout import TimeseriesWidgetLegendLayout
        from datadog_api_client.v1_20270101.model.widget_marker import WidgetMarker
        from datadog_api_client.v1_20270101.model.timeseries_widget_request import TimeseriesWidgetRequest
        from datadog_api_client.v1_20270101.model.backend_timeseries_axis_definition import (
            BackendTimeseriesAxisDefinition,
        )
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.timeseries_widget_definition_type import (
            TimeseriesWidgetDefinitionType,
        )
        from datadog_api_client.v1_20270101.model.timeseries_x_axis import TimeseriesXAxis

        return {
            "anomaly_detection": (AnomalyDetectionConfig,),
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "events": ([LegacyEventOverlayQuery],),
            "legend_columns": ([TimeseriesWidgetLegendColumn],),
            "legend_layout": (TimeseriesWidgetLegendLayout,),
            "legend_size": (str,),
            "markers": ([WidgetMarker],),
            "notes": (str,),
            "requests": ([TimeseriesWidgetRequest],),
            "right_yaxis": (BackendTimeseriesAxisDefinition,),
            "show_legend": (bool,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (TimeseriesWidgetDefinitionType,),
            "xaxis": (TimeseriesXAxis,),
            "yaxis": (BackendTimeseriesAxisDefinition,),
        }

    attribute_map = {
        "anomaly_detection": "anomaly_detection",
        "custom_links": "custom_links",
        "description": "description",
        "events": "events",
        "legend_columns": "legend_columns",
        "legend_layout": "legend_layout",
        "legend_size": "legend_size",
        "markers": "markers",
        "notes": "notes",
        "requests": "requests",
        "right_yaxis": "right_yaxis",
        "show_legend": "show_legend",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "xaxis": "xaxis",
        "yaxis": "yaxis",
    }

    def __init__(
        self_,
        requests: List[
            Union[
                TimeseriesWidgetRequest,
                TimeseriesWidgetFormulaRequest,
                TimeseriesWidgetMetricRequest,
                TimeseriesWidgetLogRequest,
                TimeseriesWidgetApmRequest,
                TimeseriesWidgetNetworkRequest,
                TimeseriesWidgetRumRequest,
                TimeseriesWidgetSecurityRequest,
                TimeseriesWidgetComplianceFindingsRequest,
                TimeseriesWidgetEventRequest,
                TimeseriesWidgetProfilingMetricsRequest,
                TimeseriesWidgetCiPipelineRequest,
                TimeseriesWidgetCiTestRequest,
                TimeseriesWidgetAuditRequest,
                TimeseriesWidgetAppsecSpanRequest,
                TimeseriesWidgetSyntheticsBatchesRequest,
                TimeseriesWidgetSyntheticsTestRunsRequest,
                TimeseriesWidgetProcessRequest,
                TimeseriesWidgetLegacyProfileMetricsRequest,
                TimeseriesWidgetLegacyEventRequest,
                TimeseriesWidgetDdsqlRequest,
                TimeseriesWidgetAdvancedQueryRequest,
                TimeseriesWidgetLocalDatasetRequest,
            ]
        ],
        type: TimeseriesWidgetDefinitionType,
        anomaly_detection: Union[AnomalyDetectionConfig, UnsetType] = unset,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        events: Union[List[LegacyEventOverlayQuery], UnsetType] = unset,
        legend_columns: Union[List[TimeseriesWidgetLegendColumn], UnsetType] = unset,
        legend_layout: Union[TimeseriesWidgetLegendLayout, UnsetType] = unset,
        legend_size: Union[str, UnsetType] = unset,
        markers: Union[List[WidgetMarker], UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        right_yaxis: Union[BackendTimeseriesAxisDefinition, UnsetType] = unset,
        show_legend: Union[bool, UnsetType] = unset,
        time: Union[
            WidgetTime,
            WidgetTime20270101OneOf,
            WidgetTime20270101OneOf4464103552,
            WidgetTime20270101OneOf4464104512,
            WidgetTime20270101OneOf4464105312,
            WidgetTime20270101OneOf4464105952,
            EmptyObject,
            UnsetType,
        ] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        xaxis: Union[TimeseriesXAxis, UnsetType] = unset,
        yaxis: Union[BackendTimeseriesAxisDefinition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param anomaly_detection: Test-only generated schema for the dashboard versioning proof of concept.
        :type anomaly_detection: AnomalyDetectionConfig, optional

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param events: Test-only generated schema for the dashboard versioning proof of concept.
        :type events: [LegacyEventOverlayQuery], optional

        :param legend_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_columns: [TimeseriesWidgetLegendColumn], optional

        :param legend_layout: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_layout: TimeseriesWidgetLegendLayout, optional

        :param legend_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_size: str, optional

        :param markers: Test-only generated schema for the dashboard versioning proof of concept.
        :type markers: [WidgetMarker], optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [TimeseriesWidgetRequest]

        :param right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type right_yaxis: BackendTimeseriesAxisDefinition, optional

        :param show_legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_legend: bool, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TimeseriesWidgetDefinitionType

        :param xaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type xaxis: TimeseriesXAxis, optional

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: BackendTimeseriesAxisDefinition, optional
        """
        if anomaly_detection is not unset:
            kwargs["anomaly_detection"] = anomaly_detection
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if events is not unset:
            kwargs["events"] = events
        if legend_columns is not unset:
            kwargs["legend_columns"] = legend_columns
        if legend_layout is not unset:
            kwargs["legend_layout"] = legend_layout
        if legend_size is not unset:
            kwargs["legend_size"] = legend_size
        if markers is not unset:
            kwargs["markers"] = markers
        if notes is not unset:
            kwargs["notes"] = notes
        if right_yaxis is not unset:
            kwargs["right_yaxis"] = right_yaxis
        if show_legend is not unset:
            kwargs["show_legend"] = show_legend
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        if xaxis is not unset:
            kwargs["xaxis"] = xaxis
        if yaxis is not unset:
            kwargs["yaxis"] = yaxis
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
