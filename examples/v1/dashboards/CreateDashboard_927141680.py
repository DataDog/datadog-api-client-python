"""
Create a new dashboard with funnel widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.funnel_query import FunnelQuery
from datadog_api_client.v1.model.funnel_request_type import FunnelRequestType
from datadog_api_client.v1.model.funnel_source import FunnelSource
from datadog_api_client.v1.model.funnel_widget_definition import FunnelWidgetDefinition
from datadog_api_client.v1.model.funnel_widget_definition_type import FunnelWidgetDefinitionType
from datadog_api_client.v1.model.funnel_widget_request import FunnelWidgetRequest
from datadog_api_client.v1.model.widget import Widget

body = Dashboard(
    layout_type=DashboardLayoutType.ORDERED,
    title="Example-Create_a_new_dashboard_with_funnel_widget with funnel widget",
    widgets=[
        Widget(
            definition=FunnelWidgetDefinition(
                type=FunnelWidgetDefinitionType.FUNNEL,
                requests=[
                    FunnelWidgetRequest(
                        query=FunnelQuery(
                            data_source=FunnelSource.RUM,
                            query_string="",
                            steps=[],
                        ),
                        request_type=FunnelRequestType.FUNNEL,
                    ),
                ],
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
