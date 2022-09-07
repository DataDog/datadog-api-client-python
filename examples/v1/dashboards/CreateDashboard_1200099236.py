"""
Create a new dashboard with hostmap widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.host_map_request import HostMapRequest
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition
from datadog_api_client.v1.model.host_map_widget_definition_requests import HostMapWidgetDefinitionRequests
from datadog_api_client.v1.model.host_map_widget_definition_style import HostMapWidgetDefinitionStyle
from datadog_api_client.v1.model.host_map_widget_definition_type import HostMapWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_node_type import WidgetNodeType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_hostmap_widget",
    description=None,
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=22,
            ),
            definition=HostMapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=HostMapWidgetDefinitionType.HOSTMAP,
                requests=HostMapWidgetDefinitionRequests(
                    fill=HostMapRequest(
                        q="avg:system.cpu.user{*} by {host}",
                    ),
                ),
                node_type=WidgetNodeType.HOST,
                no_metric_hosts=True,
                no_group_hosts=True,
                style=HostMapWidgetDefinitionStyle(
                    palette="green_to_orange",
                    palette_flip=False,
                ),
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
