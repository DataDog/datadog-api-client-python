"""
Create a new dashboard with distribution widget with markers and num_buckets
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.distribution_widget_definition_type import DistributionWidgetDefinitionType
from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest
from datadog_api_client.v1.model.distribution_widget_x_axis import DistributionWidgetXAxis
from datadog_api_client.v1.model.distribution_widget_y_axis import DistributionWidgetYAxis
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_marker import WidgetMarker
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    widgets=[
        Widget(
            definition=DistributionWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=DistributionWidgetDefinitionType.DISTRIBUTION,
                xaxis=DistributionWidgetXAxis(
                    scale="linear",
                    min="auto",
                    max="auto",
                    include_zero=True,
                    num_buckets=55,
                ),
                yaxis=DistributionWidgetYAxis(
                    scale="linear",
                    min="auto",
                    max="auto",
                    include_zero=True,
                ),
                markers=[
                    WidgetMarker(
                        display_type="percentile",
                        value="50",
                    ),
                    WidgetMarker(
                        display_type="percentile",
                        value="99",
                    ),
                    WidgetMarker(
                        display_type="percentile",
                        value="90",
                    ),
                ],
                requests=[
                    DistributionWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:system.cpu.user{*} by {service}",
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                            ),
                        ],
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
