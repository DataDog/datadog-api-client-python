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
    from datadog_api_client.v1_20270101.model.scatter_plot_legend_type import ScatterPlotLegendType
    from datadog_api_client.v1_20270101.model.marker import Marker
    from datadog_api_client.v1_20270101.model.point_plot_data_projection_request import PointPlotDataProjectionRequest
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.point_plot_backend_definition_type import PointPlotBackendDefinitionType
    from datadog_api_client.v1_20270101.model.axis import Axis
    from datadog_api_client.v1_20270101.model.scatter_plot_legend_type20270101_one_of import (
        ScatterPlotLegendType20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.scatter_plot_legend_type20270101_one_of4461516160 import (
        ScatterPlotLegendType20270101OneOf4461516160,
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


class PointPlotBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scatter_plot_legend_type import ScatterPlotLegendType
        from datadog_api_client.v1_20270101.model.marker import Marker
        from datadog_api_client.v1_20270101.model.point_plot_data_projection_request import (
            PointPlotDataProjectionRequest,
        )
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.point_plot_backend_definition_type import (
            PointPlotBackendDefinitionType,
        )
        from datadog_api_client.v1_20270101.model.axis import Axis

        return {
            "description": (str,),
            "legend": (ScatterPlotLegendType,),
            "markers": ([Marker],),
            "notes": (str,),
            "requests": ([PointPlotDataProjectionRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (PointPlotBackendDefinitionType,),
            "yaxis": (Axis,),
        }

    attribute_map = {
        "description": "description",
        "legend": "legend",
        "markers": "markers",
        "notes": "notes",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "yaxis": "yaxis",
    }

    def __init__(
        self_,
        requests: List[PointPlotDataProjectionRequest],
        type: PointPlotBackendDefinitionType,
        description: Union[str, UnsetType] = unset,
        legend: Union[
            ScatterPlotLegendType,
            ScatterPlotLegendType20270101OneOf,
            ScatterPlotLegendType20270101OneOf4461516160,
            UnsetType,
        ] = unset,
        markers: Union[List[Marker], UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
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
        yaxis: Union[Axis, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend: ScatterPlotLegendType, optional

        :param markers: Test-only generated schema for the dashboard versioning proof of concept.
        :type markers: [Marker], optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [PointPlotDataProjectionRequest]

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: PointPlotBackendDefinitionType

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: Axis, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if legend is not unset:
            kwargs["legend"] = legend
        if markers is not unset:
            kwargs["markers"] = markers
        if notes is not unset:
            kwargs["notes"] = notes
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        if yaxis is not unset:
            kwargs["yaxis"] = yaxis
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
