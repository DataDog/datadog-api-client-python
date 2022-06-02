"""
Create a new dashboard with a formulas and functions change widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
from datadog_api_client.v1.model.change_widget_definition_type import ChangeWidgetDefinitionType
from datadog_api_client.v1.model.change_widget_request import ChangeWidgetRequest
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
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_change_type import WidgetChangeType
from datadog_api_client.v1.model.widget_compare_to import WidgetCompareTo
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_order_by import WidgetOrderBy
from datadog_api_client.v1.model.widget_sort import WidgetSort
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_a_formulas_and_functions_change_widget",
    widgets=[
        Widget(
            definition=ChangeWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign("left"),
                time=WidgetTime(),
                type=ChangeWidgetDefinitionType("change"),
                requests=[
                    ChangeWidgetRequest(
                        formulas=[
                            WidgetFormula(
                                formula="hour_before(query1)",
                            ),
                            WidgetFormula(
                                formula="query1",
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionEventQueryDefinition(
                                data_source=FormulaAndFunctionEventsDataSource("logs"),
                                name="query1",
                                search=FormulaAndFunctionEventQueryDefinitionSearch(
                                    query="",
                                ),
                                indexes=[
                                    "*",
                                ],
                                compute=FormulaAndFunctionEventQueryDefinitionCompute(
                                    aggregation=FormulaAndFunctionEventAggregation("count"),
                                ),
                                group_by=[],
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat("scalar"),
                        compare_to=WidgetCompareTo("hour_before"),
                        increase_good=True,
                        order_by=WidgetOrderBy("change"),
                        change_type=WidgetChangeType("absolute"),
                        order_dir=WidgetSort("desc"),
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
    layout_type=DashboardLayoutType("ordered"),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
