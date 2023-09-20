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
    from datadog_api_client.v1.model.split_graph_viz_size import SplitGraphVizSize
    from datadog_api_client.v1.model.split_graph_source_widget_definition import SplitGraphSourceWidgetDefinition
    from datadog_api_client.v1.model.split_config import SplitConfig
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.split_graph_widget_definition_type import SplitGraphWidgetDefinitionType
    from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
    from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
    from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition
    from datadog_api_client.v1.model.scatter_plot_widget_definition import ScatterPlotWidgetDefinition
    from datadog_api_client.v1.model.sunburst_widget_definition import SunburstWidgetDefinition
    from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
    from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
    from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition
    from datadog_api_client.v1.model.tree_map_widget_definition import TreeMapWidgetDefinition


class SplitGraphWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.split_graph_viz_size import SplitGraphVizSize
        from datadog_api_client.v1.model.split_graph_source_widget_definition import SplitGraphSourceWidgetDefinition
        from datadog_api_client.v1.model.split_config import SplitConfig
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.split_graph_widget_definition_type import SplitGraphWidgetDefinitionType

        return {
            "has_uniform_y_axes": (bool,),
            "size": (SplitGraphVizSize,),
            "source_widget_definition": (SplitGraphSourceWidgetDefinition,),
            "split_config": (SplitConfig,),
            "time": (WidgetTime,),
            "title": (str,),
            "type": (SplitGraphWidgetDefinitionType,),
        }

    attribute_map = {
        "has_uniform_y_axes": "has_uniform_y_axes",
        "size": "size",
        "source_widget_definition": "source_widget_definition",
        "split_config": "split_config",
        "time": "time",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        size: SplitGraphVizSize,
        source_widget_definition: Union[
            SplitGraphSourceWidgetDefinition,
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
        split_config: SplitConfig,
        type: SplitGraphWidgetDefinitionType,
        has_uniform_y_axes: Union[bool, UnsetType] = unset,
        time: Union[WidgetTime, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The split graph widget allows you to create repeating units of a graph - one for each value in a group (for example: one per service)

        :param has_uniform_y_axes: Normalize y axes across graphs
        :type has_uniform_y_axes: bool, optional

        :param size: Size of the individual graphs in the split.
        :type size: SplitGraphVizSize

        :param source_widget_definition: The original widget we are splitting on.
        :type source_widget_definition: SplitGraphSourceWidgetDefinition

        :param split_config: Encapsulates all user choices about how to split a graph.
        :type split_config: SplitConfig

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param type: Type of the split graph widget
        :type type: SplitGraphWidgetDefinitionType
        """
        if has_uniform_y_axes is not unset:
            kwargs["has_uniform_y_axes"] = has_uniform_y_axes
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.size = size
        self_.source_widget_definition = source_widget_definition
        self_.split_config = split_config
        self_.type = type
