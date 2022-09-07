"""
Create a new dashboard with log_stream widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
from datadog_api_client.v1.model.log_stream_widget_definition_type import LogStreamWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_message_display import WidgetMessageDisplay
from datadog_api_client.v1.model.widget_sort import WidgetSort
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_log_stream_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=36,
            ),
            definition=LogStreamWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=LogStreamWidgetDefinitionType.LOG_STREAM,
                indexes=[
                    "main",
                ],
                query="",
                sort=WidgetFieldSort(
                    column="time",
                    order=WidgetSort.DESCENDING,
                ),
                columns=[
                    "host",
                    "service",
                ],
                show_date_column=True,
                show_message_column=True,
                message_display=WidgetMessageDisplay.EXPANDED_MEDIUM,
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
