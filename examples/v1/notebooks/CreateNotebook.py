"""
Create a notebook returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
from datadog_api_client.v1.model.notebook_create_data import NotebookCreateData
from datadog_api_client.v1.model.notebook_create_data_attributes import NotebookCreateDataAttributes
from datadog_api_client.v1.model.notebook_create_request import NotebookCreateRequest
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
from datadog_api_client.v1.model.notebook_markdown_cell_definition import NotebookMarkdownCellDefinition
from datadog_api_client.v1.model.notebook_markdown_cell_definition_type import NotebookMarkdownCellDefinitionType
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

body = NotebookCreateRequest(
    data=NotebookCreateData(
        attributes=NotebookCreateDataAttributes(
            cells=[
                NotebookCellCreateRequest(
                    attributes=NotebookMarkdownCellAttributes(
                        definition=NotebookMarkdownCellDefinition(
                            text="## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```",
                            type=NotebookMarkdownCellDefinitionType("markdown"),
                        ),
                    ),
                    type=NotebookCellResourceType("notebook_cells"),
                ),
                NotebookCellCreateRequest(
                    attributes=NotebookTimeseriesCellAttributes(
                        definition=TimeseriesWidgetDefinition(
                            requests=[
                                TimeseriesWidgetRequest(
                                    display_type=WidgetDisplayType("line"),
                                    q="avg:system.load.1{*}",
                                    style=WidgetRequestStyle(
                                        line_type=WidgetLineType("solid"),
                                        line_width=WidgetLineWidth("normal"),
                                        palette="dog_classic",
                                    ),
                                ),
                            ],
                            show_legend=True,
                            type=TimeseriesWidgetDefinitionType("timeseries"),
                            yaxis=WidgetAxis(
                                scale="linear",
                            ),
                        ),
                        graph_size=NotebookGraphSize("m"),
                        split_by=NotebookSplitBy(
                            keys=[],
                            tags=[],
                        ),
                        time=NotebookCellTime(None),
                    ),
                    type=NotebookCellResourceType("notebook_cells"),
                ),
            ],
            name="Example-Create_a_notebook_returns_OK_response",
            status=NotebookStatus("published"),
            time=NotebookRelativeTime(
                live_span=WidgetLiveSpan("1h"),
            ),
        ),
        type=NotebookResourceType("notebooks"),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.create_notebook(body=body)

    print(response)
