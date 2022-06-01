# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookLogStreamCellAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
        from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
        from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime

        return {
            "definition": (LogStreamWidgetDefinition,),
            "graph_size": (NotebookGraphSize,),
            "time": (NotebookCellTime,),
        }

    attribute_map = {
        "definition": "definition",
        "graph_size": "graph_size",
        "time": "time",
    }

    def __init__(self, definition, *args, **kwargs):
        """
        The attributes of a notebook ``log_stream`` cell.

        :param definition: The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
        :type definition: LogStreamWidgetDefinition

        :param graph_size: The size of the graph.
        :type graph_size: NotebookGraphSize, optional

        :param time: Timeframe for the notebook cell. When 'null', the notebook global time is used.
        :type time: NotebookCellTime, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.definition = definition

    @classmethod
    def _from_openapi_data(cls, definition, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookLogStreamCellAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.definition = definition
        return self
