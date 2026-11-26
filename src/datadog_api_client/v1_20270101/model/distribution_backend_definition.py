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
    from datadog_api_client.v1_20270101.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
    from datadog_api_client.v1_20270101.model.distribution_backend_definition_legend_layout import (
        DistributionBackendDefinitionLegendLayout,
    )
    from datadog_api_client.v1_20270101.model.widget_marker import WidgetMarker
    from datadog_api_client.v1_20270101.model.distribution_backend_request import DistributionBackendRequest
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.distribution_backend_definition_type import (
        DistributionBackendDefinitionType,
    )
    from datadog_api_client.v1_20270101.model.distribution_x_axis import DistributionXAxis
    from datadog_api_client.v1_20270101.model.backend_distribution_y_axis import BackendDistributionYAxis
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of import (
        DistributionBackendRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455761856 import (
        DistributionBackendRequest20270101OneOf4455761856,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455763296 import (
        DistributionBackendRequest20270101OneOf4455763296,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455763936 import (
        DistributionBackendRequest20270101OneOf4455763936,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455764576 import (
        DistributionBackendRequest20270101OneOf4455764576,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455765216 import (
        DistributionBackendRequest20270101OneOf4455765216,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455765856 import (
        DistributionBackendRequest20270101OneOf4455765856,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455766496 import (
        DistributionBackendRequest20270101OneOf4455766496,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455767136 import (
        DistributionBackendRequest20270101OneOf4455767136,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455767776 import (
        DistributionBackendRequest20270101OneOf4455767776,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455768416 import (
        DistributionBackendRequest20270101OneOf4455768416,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455769056 import (
        DistributionBackendRequest20270101OneOf4455769056,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455769696 import (
        DistributionBackendRequest20270101OneOf4455769696,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455770336 import (
        DistributionBackendRequest20270101OneOf4455770336,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455770976 import (
        DistributionBackendRequest20270101OneOf4455770976,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455771616 import (
        DistributionBackendRequest20270101OneOf4455771616,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455772256 import (
        DistributionBackendRequest20270101OneOf4455772256,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455772896 import (
        DistributionBackendRequest20270101OneOf4455772896,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455773536 import (
        DistributionBackendRequest20270101OneOf4455773536,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455774496 import (
        DistributionBackendRequest20270101OneOf4455774496,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455775456 import (
        DistributionBackendRequest20270101OneOf4455775456,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455989472 import (
        DistributionBackendRequest20270101OneOf4455989472,
    )
    from datadog_api_client.v1_20270101.model.distribution_backend_request20270101_one_of4455990432 import (
        DistributionBackendRequest20270101OneOf4455990432,
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


class DistributionBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
        from datadog_api_client.v1_20270101.model.distribution_backend_definition_legend_layout import (
            DistributionBackendDefinitionLegendLayout,
        )
        from datadog_api_client.v1_20270101.model.widget_marker import WidgetMarker
        from datadog_api_client.v1_20270101.model.distribution_backend_request import DistributionBackendRequest
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.distribution_backend_definition_type import (
            DistributionBackendDefinitionType,
        )
        from datadog_api_client.v1_20270101.model.distribution_x_axis import DistributionXAxis
        from datadog_api_client.v1_20270101.model.backend_distribution_y_axis import BackendDistributionYAxis

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "legend_columns": ([TimeseriesWidgetLegendColumn],),
            "legend_layout": (DistributionBackendDefinitionLegendLayout,),
            "legend_size": (str,),
            "markers": ([WidgetMarker],),
            "notes": (str,),
            "requests": ([DistributionBackendRequest],),
            "show_legend": (bool,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (DistributionBackendDefinitionType,),
            "xaxis": (DistributionXAxis,),
            "yaxis": (BackendDistributionYAxis,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "description": "description",
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
                DistributionBackendRequest,
                DistributionBackendRequest20270101OneOf,
                DistributionBackendRequest20270101OneOf4455761856,
                DistributionBackendRequest20270101OneOf4455763296,
                DistributionBackendRequest20270101OneOf4455763936,
                DistributionBackendRequest20270101OneOf4455764576,
                DistributionBackendRequest20270101OneOf4455765216,
                DistributionBackendRequest20270101OneOf4455765856,
                DistributionBackendRequest20270101OneOf4455766496,
                DistributionBackendRequest20270101OneOf4455767136,
                DistributionBackendRequest20270101OneOf4455767776,
                DistributionBackendRequest20270101OneOf4455768416,
                DistributionBackendRequest20270101OneOf4455769056,
                DistributionBackendRequest20270101OneOf4455769696,
                DistributionBackendRequest20270101OneOf4455770336,
                DistributionBackendRequest20270101OneOf4455770976,
                DistributionBackendRequest20270101OneOf4455771616,
                DistributionBackendRequest20270101OneOf4455772256,
                DistributionBackendRequest20270101OneOf4455772896,
                DistributionBackendRequest20270101OneOf4455773536,
                DistributionBackendRequest20270101OneOf4455774496,
                DistributionBackendRequest20270101OneOf4455775456,
                DistributionBackendRequest20270101OneOf4455989472,
                DistributionBackendRequest20270101OneOf4455990432,
            ]
        ],
        type: DistributionBackendDefinitionType,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        legend_columns: Union[List[TimeseriesWidgetLegendColumn], UnsetType] = unset,
        legend_layout: Union[DistributionBackendDefinitionLegendLayout, UnsetType] = unset,
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
        xaxis: Union[DistributionXAxis, UnsetType] = unset,
        yaxis: Union[BackendDistributionYAxis, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param legend_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_columns: [TimeseriesWidgetLegendColumn], optional

        :param legend_layout: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_layout: DistributionBackendDefinitionLegendLayout, optional

        :param legend_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend_size: str, optional

        :param markers: Test-only generated schema for the dashboard versioning proof of concept.
        :type markers: [WidgetMarker], optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [DistributionBackendRequest]

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
        :type type: DistributionBackendDefinitionType

        :param xaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type xaxis: DistributionXAxis, optional

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: BackendDistributionYAxis, optional
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
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
