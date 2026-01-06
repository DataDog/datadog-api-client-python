"""
Create a new dashboard with sankey widget and product analytics data source
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.sankey_rum_data_source import SankeyRumDataSource
from datadog_api_client.v1.model.sankey_rum_query import SankeyRumQuery
from datadog_api_client.v1.model.sankey_rum_query_mode import SankeyRumQueryMode
from datadog_api_client.v1.model.sankey_rum_request import SankeyRumRequest
from datadog_api_client.v1.model.sankey_widget_definition import SankeyWidgetDefinition
from datadog_api_client.v1.model.sankey_widget_definition_type import SankeyWidgetDefinitionType
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
            definition=SankeyWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=SankeyWidgetDefinitionType.SANKEY,
                requests=[
                    SankeyRumRequest(
                        query=SankeyRumQuery(
                            data_source=SankeyRumDataSource.PRODUCT_ANALYTICS,
                            query_string="@type:session",
                            mode=SankeyRumQueryMode.SOURCE,
                        ),
                        request_type=SankeyWidgetDefinitionType.SANKEY,
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
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
