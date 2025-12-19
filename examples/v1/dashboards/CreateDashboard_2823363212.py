"""
Create a new dashboard with heatmap widget with markers and num_buckets
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.heat_map_widget_definition import HeatMapWidgetDefinition
from datadog_api_client.v1.model.heat_map_widget_definition_type import HeatMapWidgetDefinitionType
from datadog_api_client.v1.model.heat_map_widget_request import HeatMapWidgetRequest
from datadog_api_client.v1.model.heat_map_widget_x_axis import HeatMapWidgetXAxis
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_histogram_request_type import WidgetHistogramRequestType
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_marker import WidgetMarker
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    widgets=[
        Widget(
            definition=HeatMapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=HeatMapWidgetDefinitionType.HEATMAP,
                xaxis=HeatMapWidgetXAxis(
                    num_buckets=75,
                ),
                yaxis=WidgetAxis(
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
                ],
                requests=[
                    HeatMapWidgetRequest(
                        request_type=WidgetHistogramRequestType.HISTOGRAM,
                        query=FormulaAndFunctionMetricQueryDefinition(
                            data_source=FormulaAndFunctionMetricDataSource.METRICS,
                            name="query1",
                            query="histogram:trace.servlet.request{*}",
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
