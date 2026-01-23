"""
Create a new dashboard with timeseries widget using order_by values
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle
from datadog_api_client.v1.model.widget_style_order_by import WidgetStyleOrderBy

body = Dashboard(
    layout_type=DashboardLayoutType.ORDERED,
    title="Example-Dashboard with order_by values",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                type=TimeseriesWidgetDefinitionType.TIMESERIES,
                requests=[
                    TimeseriesWidgetRequest(
                        q="avg:system.cpu.user{*} by {host}",
                        style=WidgetRequestStyle(
                            palette="warm",
                            order_by=WidgetStyleOrderBy.VALUES,
                        ),
                        display_type=WidgetDisplayType.LINE,
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
