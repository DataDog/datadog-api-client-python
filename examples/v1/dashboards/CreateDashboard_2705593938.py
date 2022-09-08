"""
Create a new dashboard with sunburst widget and metrics data
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.sunburst_widget_definition import SunburstWidgetDefinition
from datadog_api_client.v1.model.sunburst_widget_definition_type import SunburstWidgetDefinitionType
from datadog_api_client.v1.model.sunburst_widget_request import SunburstWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_sunburst_widget_and_metrics_data",
    widgets=[
        Widget(
            definition=SunburstWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=SunburstWidgetDefinitionType.SUNBURST,
                requests=[
                    SunburstWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                query="sum:system.mem.used{*} by {service}",
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                aggregator=FormulaAndFunctionMetricAggregation.SUM,
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
