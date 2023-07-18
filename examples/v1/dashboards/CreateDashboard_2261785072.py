"""
Create a new dashboard with a timeseries widget and an overlay request
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

body = Dashboard(
    layout_type=DashboardLayoutType.ORDERED,
    title="Example-Dashboard",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                type=TimeseriesWidgetDefinitionType.TIMESERIES,
                requests=[
                    TimeseriesWidgetRequest(
                        on_right_yaxis=False,
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="mymetric",
                                query="avg:system.cpu.user{*}",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.TIMESERIES,
                        display_type=WidgetDisplayType.LINE,
                    ),
                    TimeseriesWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.TIMESERIES,
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="mymetricoverlay",
                                query="avg:system.cpu.user{*}",
                            ),
                        ],
                        style=WidgetRequestStyle(
                            palette="purple",
                            line_type=WidgetLineType.SOLID,
                            line_width=WidgetLineWidth.NORMAL,
                        ),
                        display_type=WidgetDisplayType.OVERLAY,
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
