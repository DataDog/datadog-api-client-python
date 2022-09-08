"""
Create a new dashboard with check_status widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.check_status_widget_definition import CheckStatusWidgetDefinition
from datadog_api_client.v1.model.check_status_widget_definition_type import CheckStatusWidgetDefinitionType
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_grouping import WidgetGrouping
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_check_status_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=15,
                height=8,
            ),
            definition=CheckStatusWidgetDefinition(
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=CheckStatusWidgetDefinitionType.CHECK_STATUS,
                check="datadog.agent.up",
                grouping=WidgetGrouping.CHECK,
                tags=[
                    "*",
                ],
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
