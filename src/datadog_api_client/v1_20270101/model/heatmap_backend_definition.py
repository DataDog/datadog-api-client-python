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
    from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1_20270101.model.legacy_event_overlay_query import LegacyEventOverlayQuery
    from datadog_api_client.v1_20270101.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
    from datadog_api_client.v1_20270101.model.heatmap_backend_definition_legend_layout import (
        HeatmapBackendDefinitionLegendLayout,
    )
    from datadog_api_client.v1_20270101.model.widget_marker import WidgetMarker
    from datadog_api_client.v1_20270101.model.heatmap_backend_request import HeatmapBackendRequest
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.heatmap_backend_definition_type import HeatmapBackendDefinitionType
    from datadog_api_client.v1_20270101.model.heatmap_x_axis import HeatmapXAxis
    from datadog_api_client.v1_20270101.model.heatmap_backend_definition_yaxis import HeatmapBackendDefinitionYaxis
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of import (
        HeatmapBackendRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of4458138496 import (
        HeatmapBackendRequest20270101OneOf4458138496,
    )
    from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of4458139936 import (
        HeatmapBackendRequest20270101OneOf4458139936,
    )
    from datadog_api_client.v1_20270101.model.heatmap_backend_request20270101_one_of4458140576 import (
        HeatmapBackendRequest20270101OneOf4458140576,
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


class HeatmapBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.legacy_event_overlay_query import LegacyEventOverlayQuery
        from datadog_api_client.v1_20270101.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
        from datadog_api_client.v1_20270101.model.heatmap_backend_definition_legend_layout import (
            HeatmapBackendDefinitionLegendLayout,
        )
        from datadog_api_client.v1_20270101.model.widget_marker import WidgetMarker
        from datadog_api_client.v1_20270101.model.heatmap_backend_request import HeatmapBackendRequest
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.heatmap_backend_definition_type import HeatmapBackendDefinitionType
        from datadog_api_client.v1_20270101.model.heatmap_x_axis import HeatmapXAxis
        from datadog_api_client.v1_20270101.model.heatmap_backend_definition_yaxis import HeatmapBackendDefinitionYaxis

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "events": ([LegacyEventOverlayQuery],),
            "legend_columns": ([TimeseriesWidgetLegendColumn],),
            "legend_layout": (HeatmapBackendDefinitionLegendLayout,),
            "legend_size": (str,),
            "markers": ([WidgetMarker],),
            "notes": (str,),
            "requests": ([HeatmapBackendRequest],),
            "show_legend": (bool,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (HeatmapBackendDefinitionType,),
            "xaxis": (HeatmapXAxis,),
            "yaxis": (HeatmapBackendDefinitionYaxis,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "description": "description",
        "events": "events",
        "legend_columns": "legend_columns",
        "legend_layout": "legend_layout",
        "legend_size": "legend_size",
        "markers": "markers",
        "notes": "notes",
        "requests": "requests",
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
                HeatmapBackendRequest,
                HeatmapBackendRequest20270101OneOf,
                HeatmapBackendRequest20270101OneOf4458138496,
                HeatmapBackendRequest20270101OneOf4458139936,
                HeatmapBackendRequest20270101OneOf4458140576,
            ]
        ],
        type: HeatmapBackendDefinitionType,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        events: Union[List[LegacyEventOverlayQuery], UnsetType] = unset,
        legend_columns: Union[List[TimeseriesWidgetLegendColumn], UnsetType] = unset,
        legend_layout: Union[HeatmapBackendDefinitionLegendLayout, UnsetType] = unset,
        legend_size: Union[str, UnsetType] = unset,
        markers: Union[List[WidgetMarker], UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
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
        xaxis: Union[HeatmapXAxis, UnsetType] = unset,
        yaxis: Union[HeatmapBackendDefinitionYaxis, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param events: Test-only generated schema for the dashboard versioning proof of concept.
        :type events: [LegacyEventOverlayQuery], optional

        :param legend_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_columns: [TimeseriesWidgetLegendColumn], optional

        :param legend_layout: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_layout: HeatmapBackendDefinitionLegendLayout, optional

        :param legend_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_size: str, optional

        :param markers: Test-only generated schema for the dashboard versioning proof of concept.
        :type markers: [WidgetMarker], optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [HeatmapBackendRequest]

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
        :type type: HeatmapBackendDefinitionType

        :param xaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type xaxis: HeatmapXAxis, optional

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: HeatmapBackendDefinitionYaxis, optional
        """
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
