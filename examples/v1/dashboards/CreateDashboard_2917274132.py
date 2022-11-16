"""
Create a new dashboard with manage_status widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.monitor_summary_widget_definition import MonitorSummaryWidgetDefinition
from datadog_api_client.v1.model.monitor_summary_widget_definition_type import MonitorSummaryWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_color_preference import WidgetColorPreference
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_monitor_summary_display_format import WidgetMonitorSummaryDisplayFormat
from datadog_api_client.v1.model.widget_monitor_summary_sort import WidgetMonitorSummarySort
from datadog_api_client.v1.model.widget_summary_type import WidgetSummaryType

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_manage_status_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=50,
                height=25,
            ),
            definition=MonitorSummaryWidgetDefinition(
                type=MonitorSummaryWidgetDefinitionType.MANAGE_STATUS,
                summary_type=WidgetSummaryType.MONITORS,
                display_format=WidgetMonitorSummaryDisplayFormat.COUNTS_AND_LIST,
                color_preference=WidgetColorPreference.TEXT,
                hide_zero_counts=True,
                show_last_triggered=False,
                query="",
                sort=WidgetMonitorSummarySort.STATUS_ASCENDING,
                count=50,
                start=0,
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
