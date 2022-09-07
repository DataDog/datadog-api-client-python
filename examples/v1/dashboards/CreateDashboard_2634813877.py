"""
Create a new dashboard with event_stream widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.event_stream_widget_definition import EventStreamWidgetDefinition
from datadog_api_client.v1.model.event_stream_widget_definition_type import EventStreamWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_event_stream_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=38,
            ),
            definition=EventStreamWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=EventStreamWidgetDefinitionType.EVENT_STREAM,
                query="example-query",
                tags_execution="and",
                event_size=WidgetEventSize.SMALL,
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    is_read_only=False,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
