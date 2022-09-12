"""
Create a new dashboard with topology_map widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.topology_map_widget_definition import TopologyMapWidgetDefinition
from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType
from datadog_api_client.v1.model.topology_query import TopologyQuery
from datadog_api_client.v1.model.topology_query_data_source import TopologyQueryDataSource
from datadog_api_client.v1.model.topology_request import TopologyRequest
from datadog_api_client.v1.model.topology_request_type import TopologyRequestType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_topology_map_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=15,
            ),
            definition=TopologyMapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TopologyMapWidgetDefinitionType.TOPOLOGY_MAP,
                requests=[
                    TopologyRequest(
                        request_type=TopologyRequestType.TOPOLOGY,
                        query=TopologyQuery(
                            data_source=TopologyQueryDataSource.SERVICE_MAP,
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
    is_read_only=False,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
