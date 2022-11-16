"""
Create a new dashboard with free_text widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.free_text_widget_definition import FreeTextWidgetDefinition
from datadog_api_client.v1.model.free_text_widget_definition_type import FreeTextWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_free_text_widget",
    description=None,
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=24,
                height=6,
            ),
            definition=FreeTextWidgetDefinition(
                type=FreeTextWidgetDefinitionType.FREE_TEXT,
                text="Example free text",
                color="#4d4d4d",
                font_size="auto",
                text_align=WidgetTextAlign.LEFT,
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
