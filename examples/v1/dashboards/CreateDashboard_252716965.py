"""
Create a distribution widget using a histogram request containing a formulas and functions metrics query
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
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_style import WidgetStyle
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_distribution_widget_using_a_histogram_request_containing_a_formulas_and_functions_metrics_q",
    widgets=[
        Widget(
            definition=DistributionWidgetDefinition(
                title="Metrics HOP",
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
                        query=FormulaAndFunctionMetricQueryDefinition(
                            query="histogram:trace.Load{*}",
                            data_source=FormulaAndFunctionMetricDataSource.METRICS,
                            name="query1",
                        ),
                        request_type=DistributionWidgetHistogramRequestType.HISTOGRAM,
                        style=WidgetStyle(
                            palette="dog_classic",
                        ),
                    ),
                ],
            ),
            layout=WidgetLayout(
                x=0,
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
