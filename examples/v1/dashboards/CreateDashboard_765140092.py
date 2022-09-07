"""
Create a new dashboard with a query value widget using timeseries background
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
from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition
from datadog_api_client.v1.model.query_value_widget_definition_type import QueryValueWidgetDefinitionType
from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest
from datadog_api_client.v1.model.timeseries_background import TimeseriesBackground
from datadog_api_client.v1.model.timeseries_background_type import TimeseriesBackgroundType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    layout_type=DashboardLayoutType.ORDERED,
    title="Example-Create_a_new_dashboard_with_a_query_value_widget_using_timeseries_background with QVW Timeseries Background",
    widgets=[
        Widget(
            definition=QueryValueWidgetDefinition(
                title_size="16",
                title="",
                title_align=WidgetTextAlign.LEFT,
                precision=2,
                time=WidgetTime(),
                autoscale=True,
                requests=[
                    QueryValueWidgetRequest(
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                query="sum:my.cool.count.metric{*}",
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                aggregator=FormulaAndFunctionMetricAggregation.PERCENTILE,
                            ),
                        ],
                    ),
                ],
                type=QueryValueWidgetDefinitionType.QUERY_VALUE,
                timeseries_background=TimeseriesBackground(
                    type=TimeseriesBackgroundType.AREA,
                    yaxis=WidgetAxis(
                        include_zero=True,
                    ),
                ),
            ),
            layout=WidgetLayout(
                y=0,
                x=0,
                height=2,
                width=2,
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
