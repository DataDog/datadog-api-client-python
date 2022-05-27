# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookHeatMapCellAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heat_map_widget_definition import HeatMapWidgetDefinition
        from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
        from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
        from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime

        return {
            "definition": (HeatMapWidgetDefinition,),
            "graph_size": (NotebookGraphSize,),
            "split_by": (NotebookSplitBy,),
            "time": (NotebookCellTime,),
        }

    attribute_map = {
        "definition": "definition",
        "graph_size": "graph_size",
        "split_by": "split_by",
        "time": "time",
    }

    def __init__(self, definition, *args, **kwargs):
        """
        The attributes of a notebook ``heatmap`` cell.

        :param definition: The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
        :type definition: HeatMapWidgetDefinition

        :param graph_size: The size of the graph.
        :type graph_size: NotebookGraphSize, optional

        :param split_by: Object describing how to split the graph to display multiple visualizations per request.
        :type split_by: NotebookSplitBy, optional

        :param time: Timeframe for the notebook cell. When 'null', the notebook global time is used.
        :type time: NotebookCellTime, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.definition = definition

    @classmethod
    def _from_openapi_data(cls, definition, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookHeatMapCellAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.definition = definition
        return self
