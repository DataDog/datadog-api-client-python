"""
Create a new dashboard with iframe widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.i_frame_widget_definition import IFrameWidgetDefinition
from datadog_api_client.v1.model.i_frame_widget_definition_type import IFrameWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_iframe_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=12,
                height=12,
            ),
            definition=IFrameWidgetDefinition(
                type=IFrameWidgetDefinitionType.IFRAME,
                url="https://docs.datadoghq.com/api/latest/",
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
