"""
Create a new dashboard with llm_observability_stream list_stream widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.list_stream_column import ListStreamColumn
from datadog_api_client.v1.model.list_stream_column_width import ListStreamColumnWidth
from datadog_api_client.v1.model.list_stream_query import ListStreamQuery
from datadog_api_client.v1.model.list_stream_response_format import ListStreamResponseFormat
from datadog_api_client.v1.model.list_stream_source import ListStreamSource
from datadog_api_client.v1.model.list_stream_widget_definition import ListStreamWidgetDefinition
from datadog_api_client.v1.model.list_stream_widget_definition_type import ListStreamWidgetDefinitionType
from datadog_api_client.v1.model.list_stream_widget_request import ListStreamWidgetRequest
from datadog_api_client.v1.model.widget import Widget

body = Dashboard(
    layout_type=DashboardLayoutType.ORDERED,
    title="Example-Dashboard with list_stream widget",
    widgets=[
        Widget(
            definition=ListStreamWidgetDefinition(
                type=ListStreamWidgetDefinitionType.LIST_STREAM,
                requests=[
                    ListStreamWidgetRequest(
                        response_format=ListStreamResponseFormat.EVENT_LIST,
                        query=ListStreamQuery(
                            data_source=ListStreamSource.LLM_OBSERVABILITY_STREAM,
                            query_string="@event_type:span @parent_id:undefined",
                            indexes=[],
                        ),
                        columns=[
                            ListStreamColumn(
                                field="@status",
                                width=ListStreamColumnWidth.COMPACT,
                            ),
                            ListStreamColumn(
                                field="@content.prompt",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@content.response.content",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="timestamp",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@ml_app",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="service",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@meta.evaluations.quality",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@meta.evaluations.security",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@duration",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                        ],
                    ),
                ],
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
