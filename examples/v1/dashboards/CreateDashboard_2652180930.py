"""
Create a new dashboard with topology_map widget
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.topology_map_widget_definition_service_map import TopologyMapWidgetDefinitionServiceMap
from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType
from datadog_api_client.v1.model.topology_query_service_map import TopologyQueryServiceMap
from datadog_api_client.v1.model.topology_query_service_map_data_source import TopologyQueryServiceMapDataSource
from datadog_api_client.v1.model.topology_request_service_map import TopologyRequestServiceMap
from datadog_api_client.v1.model.topology_request_type import TopologyRequestType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=15,
            ),
            definition=TopologyMapWidgetDefinitionServiceMap(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TopologyMapWidgetDefinitionType.TOPOLOGY_MAP,
                requests=[
                    TopologyRequestServiceMap(
                        request_type=TopologyRequestType.TOPOLOGY,
                        query=TopologyQueryServiceMap(
                            data_source=TopologyQueryServiceMapDataSource.SERVICE_MAP,
                            service="",
                            filters=[
                                "env:none",
                                "environment:*",
                            ],
                        ),
                    ),
                ],
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    notify_list=[],
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
