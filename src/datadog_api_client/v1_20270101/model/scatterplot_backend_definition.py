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
    from datadog_api_client.v1_20270101.model.scatter_plot_legend_type import ScatterPlotLegendType
    from datadog_api_client.v1_20270101.model.scatterplot_requests import ScatterplotRequests
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.scatterplot_backend_definition_type import (
        ScatterplotBackendDefinitionType,
    )
    from datadog_api_client.v1_20270101.model.widget_axis import WidgetAxis
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.scatter_plot_legend_type20270101_one_of import (
        ScatterPlotLegendType20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.scatter_plot_legend_type20270101_one_of4461516160 import (
        ScatterPlotLegendType20270101OneOf4461516160,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_requests20270101_one_of import (
        ScatterplotRequests20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_requests20270101_one_of4461761120 import (
        ScatterplotRequests20270101OneOf4461761120,
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


class ScatterplotBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.scatter_plot_legend_type import ScatterPlotLegendType
        from datadog_api_client.v1_20270101.model.scatterplot_requests import ScatterplotRequests
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.scatterplot_backend_definition_type import (
            ScatterplotBackendDefinitionType,
        )
        from datadog_api_client.v1_20270101.model.widget_axis import WidgetAxis

        return {
            "color_by_groups": ([str],),
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "legend": (ScatterPlotLegendType,),
            "notes": (str,),
            "palette": (str,),
            "requests": (ScatterplotRequests,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ScatterplotBackendDefinitionType,),
            "xaxis": (WidgetAxis,),
            "yaxis": (WidgetAxis,),
        }

    attribute_map = {
        "color_by_groups": "color_by_groups",
        "custom_links": "custom_links",
        "description": "description",
        "legend": "legend",
        "notes": "notes",
        "palette": "palette",
        "requests": "requests",
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
        requests: Union[
            ScatterplotRequests, ScatterplotRequests20270101OneOf, ScatterplotRequests20270101OneOf4461761120
        ],
        type: ScatterplotBackendDefinitionType,
        color_by_groups: Union[List[str], UnsetType] = unset,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        legend: Union[
            ScatterPlotLegendType,
            ScatterPlotLegendType20270101OneOf,
            ScatterPlotLegendType20270101OneOf4461516160,
            UnsetType,
        ] = unset,
        notes: Union[str, UnsetType] = unset,
        palette: Union[str, UnsetType] = unset,
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
        xaxis: Union[WidgetAxis, UnsetType] = unset,
        yaxis: Union[WidgetAxis, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color_by_groups: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_by_groups: [str], optional

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend: ScatterPlotLegendType, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: ScatterplotRequests

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ScatterplotBackendDefinitionType

        :param xaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type xaxis: WidgetAxis, optional

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: WidgetAxis, optional
        """
        if color_by_groups is not unset:
            kwargs["color_by_groups"] = color_by_groups
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if legend is not unset:
            kwargs["legend"] = legend
        if notes is not unset:
            kwargs["notes"] = notes
        if palette is not unset:
            kwargs["palette"] = palette
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
