"""
Create a new dashboard with alert_graph widget
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.alert_graph_widget_definition import AlertGraphWidgetDefinition
from datadog_api_client.v1.model.alert_graph_widget_definition_type import AlertGraphWidgetDefinitionType
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime
from datadog_api_client.v1.model.widget_viz_type import WidgetVizType

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_alert_graph_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=15,
            ),
            definition=AlertGraphWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetTime(),
                type=AlertGraphWidgetDefinitionType.ALERT_GRAPH,
                alert_id="7",
                viz_type=WidgetVizType.TIMESERIES,
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
