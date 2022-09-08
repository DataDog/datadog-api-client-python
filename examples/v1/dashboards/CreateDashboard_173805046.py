"""
Create a new dashboard with slo widget
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.slo_widget_definition import SLOWidgetDefinition
from datadog_api_client.v1.model.slo_widget_definition_type import SLOWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time_windows import WidgetTimeWindows
from datadog_api_client.v1.model.widget_view_mode import WidgetViewMode

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_slo_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=60,
                height=21,
            ),
            definition=SLOWidgetDefinition(
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=SLOWidgetDefinitionType.SLO,
                view_type="detail",
                time_windows=[
                    WidgetTimeWindows.SEVEN_DAYS,
                ],
                slo_id=SLO_DATA_0_ID,
                show_error_budget=True,
                view_mode=WidgetViewMode.OVERALL,
                global_time_target="0",
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
