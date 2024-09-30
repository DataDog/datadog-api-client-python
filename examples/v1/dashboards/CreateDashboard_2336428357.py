"""
Create a new dashboard with query_table widget
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
from datadog_api_client.v1.model.formula_type import FormulaType
from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_formula_sort import WidgetFormulaSort
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
from datadog_api_client.v1.model.widget_sort import WidgetSort
from datadog_api_client.v1.model.widget_sort_by import WidgetSortBy
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=54,
                height=32,
            ),
            definition=TableWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetLegacyLiveSpan(),
                type=TableWidgetDefinitionType.QUERY_TABLE,
                requests=[
                    TableWidgetRequest(
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:system.cpu.user{*} by {host}",
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                            ),
                        ],
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                                conditional_formats=[],
                                cell_display_mode=TableWidgetCellDisplayMode.BAR,
                            ),
                        ],
                        sort=WidgetSortBy(
                            count=500,
                            order_by=[
                                WidgetFormulaSort(
                                    type=FormulaType.FORMULA,
                                    index=0,
                                    order=WidgetSort.DESCENDING,
                                ),
                            ],
                        ),
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                    ),
                ],
                has_search_bar=TableWidgetHasSearchBar.AUTO,
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    is_read_only=False,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
