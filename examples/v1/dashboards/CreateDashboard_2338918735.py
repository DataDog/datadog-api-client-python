"""
Create a new dashboard with list_stream widget
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
    title="Example-Create_a_new_dashboard_with_list_stream_widget with list_stream widget",
    widgets=[
        Widget(
            definition=ListStreamWidgetDefinition(
                type=ListStreamWidgetDefinitionType.LIST_STREAM,
                requests=[
                    ListStreamWidgetRequest(
                        columns=[
                            ListStreamColumn(
                                width=ListStreamColumnWidth.AUTO,
                                field="timestamp",
                            ),
                        ],
                        query=ListStreamQuery(
                            data_source=ListStreamSource.APM_ISSUE_STREAM,
                            query_string="",
                        ),
                        response_format=ListStreamResponseFormat.EVENT_LIST,
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
