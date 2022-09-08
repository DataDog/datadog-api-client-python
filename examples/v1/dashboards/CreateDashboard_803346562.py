"""
Create a new dashboard with distribution widget and apm stats data
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.apm_stats_query_definition import ApmStatsQueryDefinition
from datadog_api_client.v1.model.apm_stats_query_row_type import ApmStatsQueryRowType
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.distribution_widget_definition_type import DistributionWidgetDefinitionType
from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_distribution_widget_and_apm_stats_data",
    widgets=[
        Widget(
            definition=DistributionWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=DistributionWidgetDefinitionType.DISTRIBUTION,
                requests=[
                    DistributionWidgetRequest(
                        apm_stats_query=ApmStatsQueryDefinition(
                            env="prod",
                            service="cassandra",
                            name="cassandra.query",
                            primary_tag="datacenter:dc1",
                            row_type=ApmStatsQueryRowType.SERVICE,
                        ),
                    ),
                ],
            ),
            layout=WidgetLayout(
                x=0,
                y=0,
                width=4,
                height=4,
            ),
        ),
    ],
    layout_type=DashboardLayoutType.ORDERED,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
