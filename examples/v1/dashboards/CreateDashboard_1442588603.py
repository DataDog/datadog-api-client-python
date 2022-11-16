"""
Create a distribution widget using a histogram request containing a formulas and functions APM Stats query
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.distribution_widget_definition_type import DistributionWidgetDefinitionType
from datadog_api_client.v1.model.distribution_widget_histogram_request_type import (
    DistributionWidgetHistogramRequestType,
)
from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest
from datadog_api_client.v1.model.distribution_widget_x_axis import DistributionWidgetXAxis
from datadog_api_client.v1.model.distribution_widget_y_axis import DistributionWidgetYAxis
from datadog_api_client.v1.model.formula_and_function_apm_resource_stat_name import (
    FormulaAndFunctionApmResourceStatName,
)
from datadog_api_client.v1.model.formula_and_function_apm_resource_stats_data_source import (
    FormulaAndFunctionApmResourceStatsDataSource,
)
from datadog_api_client.v1.model.formula_and_function_apm_resource_stats_query_definition import (
    FormulaAndFunctionApmResourceStatsQueryDefinition,
)
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_style import WidgetStyle
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_distribution_widget_using_a_histogram_request_containing_a_formulas_and_functions_APM_Stats",
    description="",
    widgets=[
        Widget(
            definition=DistributionWidgetDefinition(
                title="APM Stats - Request latency HOP",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                show_legend=False,
                type=DistributionWidgetDefinitionType.DISTRIBUTION,
                xaxis=DistributionWidgetXAxis(
                    max="auto",
                    include_zero=True,
                    scale="linear",
                    min="auto",
                ),
                yaxis=DistributionWidgetYAxis(
                    max="auto",
                    include_zero=True,
                    scale="linear",
                    min="auto",
                ),
                requests=[
                    DistributionWidgetRequest(
                        query=FormulaAndFunctionApmResourceStatsQueryDefinition(
                            primary_tag_value="*",
                            stat=FormulaAndFunctionApmResourceStatName.LATENCY_DISTRIBUTION,
                            data_source=FormulaAndFunctionApmResourceStatsDataSource.APM_RESOURCE_STATS,
                            name="query1",
                            service="azure-bill-import",
                            group_by=[
                                "resource_name",
                            ],
                            env="staging",
                            primary_tag_name="datacenter",
                            operation_name="universal.http.client",
                        ),
                        request_type=DistributionWidgetHistogramRequestType.HISTOGRAM,
                        style=WidgetStyle(
                            palette="dog_classic",
                        ),
                    ),
                ],
            ),
            layout=WidgetLayout(
                x=8,
                y=0,
                width=4,
                height=2,
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
