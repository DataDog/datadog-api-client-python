"""
Create a new dashboard with rum_issue_stream list_stream widget
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
    layout_type=DashboardLayoutType("ordered"),
    title="Example-Create_a_new_dashboard_with_rum_issue_stream_list_stream_widget with list_stream widget",
    widgets=[
        Widget(
            definition=ListStreamWidgetDefinition(
                type=ListStreamWidgetDefinitionType("list_stream"),
                requests=[
                    ListStreamWidgetRequest(
                        columns=[
                            ListStreamColumn(
                                width=ListStreamColumnWidth("auto"),
                                field="timestamp",
                            ),
                        ],
                        query=ListStreamQuery(
                            data_source=ListStreamSource("rum_issue_stream"),
                            query_string="",
                        ),
                        response_format=ListStreamResponseFormat("event_list"),
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
