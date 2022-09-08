"""
Create a new dashboard with formulas and functions scatterplot widget
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
from datadog_api_client.v1.model.scatter_plot_widget_definition import ScatterPlotWidgetDefinition
from datadog_api_client.v1.model.scatter_plot_widget_definition_requests import ScatterPlotWidgetDefinitionRequests
from datadog_api_client.v1.model.scatter_plot_widget_definition_type import ScatterPlotWidgetDefinitionType
from datadog_api_client.v1.model.scatterplot_dimension import ScatterplotDimension
from datadog_api_client.v1.model.scatterplot_table_request import ScatterplotTableRequest
from datadog_api_client.v1.model.scatterplot_widget_formula import ScatterplotWidgetFormula
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_formulas_and_functions_scatterplot_widget",
    widgets=[
        Widget(
            id=5346764334358972,
            definition=ScatterPlotWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=ScatterPlotWidgetDefinitionType.SCATTERPLOT,
                requests=ScatterPlotWidgetDefinitionRequests(
                    table=ScatterplotTableRequest(
                        formulas=[
                            ScatterplotWidgetFormula(
                                formula="query1",
                                dimension=ScatterplotDimension.X,
                                alias="my-query1",
                            ),
                            ScatterplotWidgetFormula(
                                formula="query2",
                                dimension=ScatterplotDimension.Y,
                                alias="my-query2",
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:system.cpu.user{*} by {service}",
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                            ),
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query2",
                                query="avg:system.mem.used{*} by {service}",
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                    ),
                ),
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
