# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
    from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
    from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
    from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime

    globals()["DistributionWidgetDefinition"] = DistributionWidgetDefinition
    globals()["NotebookGraphSize"] = NotebookGraphSize
    globals()["NotebookSplitBy"] = NotebookSplitBy
    globals()["NotebookCellTime"] = NotebookCellTime


class NotebookDistributionCellAttributes(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "definition": (DistributionWidgetDefinition,),
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

    read_only_vars = {}

    def __init__(self, definition, *args, **kwargs):
        """
        The attributes of a notebook `distribution` cell.

        :param definition: The Distribution visualization is another way of showing metrics
            aggregated across one or several tags, such as hosts.
            Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
        :type definition: DistributionWidgetDefinition

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

        self = super(NotebookDistributionCellAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.definition = definition
        return self
