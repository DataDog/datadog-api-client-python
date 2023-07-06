"""
Create a new dashboard with a change widget using formulas and functions slo query
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
from datadog_api_client.v1.model.change_widget_definition_type import ChangeWidgetDefinitionType
from datadog_api_client.v1.model.change_widget_request import ChangeWidgetRequest
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.formula_and_function_slo_data_source import FormulaAndFunctionSLODataSource
from datadog_api_client.v1.model.formula_and_function_slo_group_mode import FormulaAndFunctionSLOGroupMode
from datadog_api_client.v1.model.formula_and_function_slo_measure import FormulaAndFunctionSLOMeasure
from datadog_api_client.v1.model.formula_and_function_slo_query_definition import FormulaAndFunctionSLOQueryDefinition
from datadog_api_client.v1.model.formula_and_function_slo_query_type import FormulaAndFunctionSLOQueryType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_change_type import WidgetChangeType
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_order_by import WidgetOrderBy
from datadog_api_client.v1.model.widget_sort import WidgetSort
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

body = Dashboard(
    title="Example-Dashboard",
    widgets=[
        Widget(
            definition=ChangeWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetTime(),
                type=ChangeWidgetDefinitionType.CHANGE,
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
                            FormulaAndFunctionSLOQueryDefinition(
                                name="query1",
                                data_source=FormulaAndFunctionSLODataSource.SLO,
                                slo_id=SLO_DATA_0_ID,
                                measure=FormulaAndFunctionSLOMeasure.SLO_STATUS,
                                group_mode=FormulaAndFunctionSLOGroupMode.OVERALL,
                                slo_query_type=FormulaAndFunctionSLOQueryType.METRIC,
                                additional_query_filters="*",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        order_by=WidgetOrderBy.CHANGE,
                        change_type=WidgetChangeType.ABSOLUTE,
                        increase_good=True,
                        order_dir=WidgetSort.ASCENDING,
                    ),
                ],
            ),
            layout=WidgetLayout(
                x=0,
                y=0,
                width=4,
                height=2,
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
