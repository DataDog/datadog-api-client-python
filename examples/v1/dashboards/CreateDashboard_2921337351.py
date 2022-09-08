"""
Create a new dashboard with trace_service widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.service_summary_widget_definition import ServiceSummaryWidgetDefinition
from datadog_api_client.v1.model.service_summary_widget_definition_type import ServiceSummaryWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_service_summary_display_format import WidgetServiceSummaryDisplayFormat
from datadog_api_client.v1.model.widget_size_format import WidgetSizeFormat
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_trace_service_widget",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=72,
                height=72,
            ),
            definition=ServiceSummaryWidgetDefinition(
                title="Service Summary",
                time=WidgetTime(),
                type=ServiceSummaryWidgetDefinitionType.TRACE_SERVICE,
                env="none",
                service="",
                span_name="",
                show_hits=True,
                show_errors=True,
                show_latency=True,
                show_breakdown=True,
                show_distribution=True,
                show_resource_list=False,
                size_format=WidgetSizeFormat.MEDIUM,
                display_format=WidgetServiceSummaryDisplayFormat.TWO_COLUMN,
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
