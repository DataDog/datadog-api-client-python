# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
    from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
    from datadog_api_client.v1.model.notebook_toplist_cell_attributes import NotebookToplistCellAttributes
    from datadog_api_client.v1.model.notebook_heat_map_cell_attributes import NotebookHeatMapCellAttributes
    from datadog_api_client.v1.model.notebook_distribution_cell_attributes import NotebookDistributionCellAttributes
    from datadog_api_client.v1.model.notebook_log_stream_cell_attributes import NotebookLogStreamCellAttributes

    globals()["NotebookMarkdownCellAttributes"] = NotebookMarkdownCellAttributes
    globals()["NotebookTimeseriesCellAttributes"] = NotebookTimeseriesCellAttributes
    globals()["NotebookToplistCellAttributes"] = NotebookToplistCellAttributes
    globals()["NotebookHeatMapCellAttributes"] = NotebookHeatMapCellAttributes
    globals()["NotebookDistributionCellAttributes"] = NotebookDistributionCellAttributes
    globals()["NotebookLogStreamCellAttributes"] = NotebookLogStreamCellAttributes


class NotebookCellUpdateRequestAttributes(ModelComposed):
    def __init__(self, *args, **kwargs):
        """
        The attributes of a notebook cell in update cell request. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`,
        `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)

        :param definition: Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
        :type definition: NotebookMarkdownCellDefinition

        :param graph_size: The size of the graph.
        :type graph_size: NotebookGraphSize, optional

        :param split_by: Object describing how to split the graph to display multiple visualizations per request.
        :type split_by: NotebookSplitBy, optional

        :param time: Timeframe for the notebook cell. When 'null', the notebook global time is used.
        :type time: NotebookCellTime, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCellUpdateRequestAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                NotebookMarkdownCellAttributes,
                NotebookTimeseriesCellAttributes,
                NotebookToplistCellAttributes,
                NotebookHeatMapCellAttributes,
                NotebookDistributionCellAttributes,
                NotebookLogStreamCellAttributes,
            ],
        }
