"""
Create a new timeseries widget with ci_tests data source
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
from datadog_api_client.v1.model.formula_and_function_event_aggregation import FormulaAndFunctionEventAggregation
from datadog_api_client.v1.model.formula_and_function_event_query_definition import (
    FormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_compute import (
    FormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_search import (
    FormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.formula_and_function_events_data_source import FormulaAndFunctionEventsDataSource
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_legend_column import TimeseriesWidgetLegendColumn
from datadog_api_client.v1.model.timeseries_widget_legend_layout import TimeseriesWidgetLegendLayout
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    title="Example-Create_a_new_timeseries_widget_with_ci_tests_data_source with ci_tests datasource",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                title="",
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
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionEventQueryDefinition(
                                data_source=FormulaAndFunctionEventsDataSource.CI_TESTS,
                                name="query1",
                                search=FormulaAndFunctionEventQueryDefinitionSearch(
                                    query="test_level:test",
                                ),
                                indexes=[
                                    "*",
                                ],
                                compute=FormulaAndFunctionEventQueryDefinitionCompute(
                                    aggregation=FormulaAndFunctionEventAggregation.COUNT,
                                ),
                                group_by=[],
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
