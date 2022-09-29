"""
Create a new dashboard with slo list widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.slo_list_widget_definition import SLOListWidgetDefinition
from datadog_api_client.v1.model.slo_list_widget_definition_type import SLOListWidgetDefinitionType
from datadog_api_client.v1.model.slo_list_widget_query import SLOListWidgetQuery
from datadog_api_client.v1.model.slo_list_widget_request import SLOListWidgetRequest
from datadog_api_client.v1.model.slo_list_widget_request_type import SLOListWidgetRequestType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_slo_list_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=60,
                height=21,
            ),
            definition=SLOListWidgetDefinition(
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=SLOListWidgetDefinitionType.SLO_LIST,
                requests=[
                    SLOListWidgetRequest(
                        query=SLOListWidgetQuery(
                            query_string="env:prod AND service:my-app",
                            limit=75,
                        ),
                        request_type=SLOListWidgetRequestType.SLO_LIST,
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
