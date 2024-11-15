"""
Create a new dashboard with heatmap widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.heat_map_widget_definition import HeatMapWidgetDefinition
from datadog_api_client.v1.model.heat_map_widget_definition_type import HeatMapWidgetDefinitionType
from datadog_api_client.v1.model.heat_map_widget_request import HeatMapWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
from datadog_api_client.v1.model.widget_style import WidgetStyle
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description=None,
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=15,
            ),
            definition=HeatMapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetLegacyLiveSpan(),
                type=HeatMapWidgetDefinitionType.HEATMAP,
                requests=[
                    HeatMapWidgetRequest(
                        q="avg:system.cpu.user{*} by {service}",
                        style=WidgetStyle(
                            palette="dog_classic",
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
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
