"""
Create a new dashboard with timeseries widget and formula style attributes
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
from datadog_api_client.v1.model.timeseries_widget_legend_layout import TimeseriesWidgetLegendLayout
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_formula_style import WidgetFormulaStyle
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_timeseries_widget_and_formula_style_attributes with formula style",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                title="styled timeseries",
                show_legend=True,
                legend_layout=TimeseriesWidgetLegendLayout.AUTO,
                legend_columns=[
                    TimeseriesWidgetLegendColumn.AVG,
                    TimeseriesWidgetLegendColumn.MIN,
                    TimeseriesWidgetLegendColumn.MAX,
                    TimeseriesWidgetLegendColumn.VALUE,
                    TimeseriesWidgetLegendColumn.SUM,
                ],
                time=WidgetTime(),
                type=TimeseriesWidgetDefinitionType.TIMESERIES,
                requests=[
                    TimeseriesWidgetRequest(
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                                style=WidgetFormulaStyle(
                                    palette_index=4,
                                    palette="classic",
                                ),
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                query="avg:system.cpu.user{*}",
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.TIMESERIES,
                        style=WidgetRequestStyle(
                            palette="dog_classic",
                            line_type=WidgetLineType.SOLID,
                            line_width=WidgetLineWidth.NORMAL,
                        ),
                        display_type=WidgetDisplayType.LINE,
                    ),
                ],
            ),
        ),
    ],
    layout_type=DashboardLayoutType.ORDERED,
    reflow_type=DashboardReflowType.AUTO,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
