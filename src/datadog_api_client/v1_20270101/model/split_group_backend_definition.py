# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.formsizes import FORMSIZES
    from datadog_api_client.v1_20270101.model.split_group_backend_definition20270101_source_widget_definition import (
        SplitGroupBackendDefinition20270101SourceWidgetDefinition,
    )
    from datadog_api_client.v1_20270101.model.split_config import SplitConfig
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.split_group_backend_definition_type import SplitGroupBackendDefinitionType
    from datadog_api_client.v1_20270101.model.bar_chart_backend_definition import BarChartBackendDefinition
    from datadog_api_client.v1_20270101.model.change_backend_definition import ChangeBackendDefinition
    from datadog_api_client.v1_20270101.model.distribution_backend_definition import DistributionBackendDefinition
    from datadog_api_client.v1_20270101.model.geomap_backend_definition import GeomapBackendDefinition
    from datadog_api_client.v1_20270101.model.heatgrid_definition import HeatgridDefinition
    from datadog_api_client.v1_20270101.model.query_table_backend_definition import QueryTableBackendDefinition
    from datadog_api_client.v1_20270101.model.query_value_backend_definition import QueryValueBackendDefinition
    from datadog_api_client.v1_20270101.model.scatterplot_backend_definition import ScatterplotBackendDefinition
    from datadog_api_client.v1_20270101.model.sunburst_backend_definition import SunburstBackendDefinition
    from datadog_api_client.v1_20270101.model.timeseries_widget_definition import TimeseriesWidgetDefinition
    from datadog_api_client.v1_20270101.model.toplist_backend_definition import ToplistBackendDefinition
    from datadog_api_client.v1_20270101.model.treemap_backend_definition import TreemapBackendDefinition
    from datadog_api_client.v1_20270101.model.wildcard_backend_definition import WildcardBackendDefinition
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


class SplitGroupBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formsizes import FORMSIZES
        from datadog_api_client.v1_20270101.model.split_group_backend_definition20270101_source_widget_definition import (
            SplitGroupBackendDefinition20270101SourceWidgetDefinition,
        )
        from datadog_api_client.v1_20270101.model.split_config import SplitConfig
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.split_group_backend_definition_type import (
            SplitGroupBackendDefinitionType,
        )

        return {
            "description": (str,),
            "has_uniform_y_axes": (bool,),
            "notes": (str,),
            "size": (FORMSIZES,),
            "source_widget_definition": (SplitGroupBackendDefinition20270101SourceWidgetDefinition,),
            "split_config": (SplitConfig,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SplitGroupBackendDefinitionType,),
        }

    attribute_map = {
        "description": "description",
        "has_uniform_y_axes": "has_uniform_y_axes",
        "notes": "notes",
        "size": "size",
        "source_widget_definition": "source_widget_definition",
        "split_config": "split_config",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        size: FORMSIZES,
        source_widget_definition: Union[
            SplitGroupBackendDefinition20270101SourceWidgetDefinition,
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
        split_config: SplitConfig,
        type: SplitGroupBackendDefinitionType,
        description: Union[str, UnsetType] = unset,
        has_uniform_y_axes: Union[bool, UnsetType] = unset,
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
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param has_uniform_y_axes: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_uniform_y_axes: bool, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param size: Test-only generated schema for the dashboard versioning proof of concept.
        :type size: FORMSIZES

        :param source_widget_definition: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_widget_definition: SplitGroupBackendDefinition20270101SourceWidgetDefinition

        :param split_config: Test-only generated schema for the dashboard versioning proof of concept.
        :type split_config: SplitConfig

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: SplitGroupBackendDefinitionType
        """
        if description is not unset:
            kwargs["description"] = description
        if has_uniform_y_axes is not unset:
            kwargs["has_uniform_y_axes"] = has_uniform_y_axes
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
        super().__init__(kwargs)

        self_.size = size
        self_.source_widget_definition = source_widget_definition
        self_.split_config = split_config
        self_.type = type
