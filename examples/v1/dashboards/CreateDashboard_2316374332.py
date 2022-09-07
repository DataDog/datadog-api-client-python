"""
Create a new dashboard with alert_value widget
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.alert_value_widget_definition import AlertValueWidgetDefinition
from datadog_api_client.v1.model.alert_value_widget_definition_type import AlertValueWidgetDefinitionType
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_alert_value_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=15,
                height=8,
            ),
            definition=AlertValueWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=AlertValueWidgetDefinitionType.ALERT_VALUE,
                alert_id="7",
                unit="auto",
                text_align=WidgetTextAlign.LEFT,
                precision=2,
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
