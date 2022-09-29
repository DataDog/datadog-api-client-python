"""
Create a new dashboard with logs query table widget and storage parameter
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
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
from datadog_api_client.v1.model.query_sort_order import QuerySortOrder
from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_formula_limit import WidgetFormulaLimit

body = Dashboard(
    layout_type=DashboardLayoutType.ORDERED,
    title="Example-Create_a_new_dashboard_with_logs_query_table_widget_and_storage_parameter with query table widget and storage parameter",
    widgets=[
        Widget(
            definition=TableWidgetDefinition(
                type=TableWidgetDefinitionType.QUERY_TABLE,
                requests=[
                    TableWidgetRequest(
                        queries=[
                            FormulaAndFunctionEventQueryDefinition(
                                data_source=FormulaAndFunctionEventsDataSource.LOGS,
                                name="query1",
                                search=FormulaAndFunctionEventQueryDefinitionSearch(
                                    query="",
                                ),
                                indexes=[
                                    "*",
                                ],
                                compute=FormulaAndFunctionEventQueryDefinitionCompute(
                                    aggregation=FormulaAndFunctionEventAggregation.COUNT,
                                ),
                                group_by=[],
                                storage="online_archives",
                            ),
                        ],
                        formulas=[
                            WidgetFormula(
                                conditional_formats=[],
                                cell_display_mode=TableWidgetCellDisplayMode.BAR,
                                formula="query1",
                                limit=WidgetFormulaLimit(
                                    count=50,
                                    order=QuerySortOrder.DESC,
                                ),
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
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
