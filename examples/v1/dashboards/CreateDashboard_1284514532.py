"""
Create a new dashboard with a timeseries widget using formulas and functions cloud cost query
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_cloud_cost_data_source import (
    FormulaAndFunctionCloudCostDataSource,
)
from datadog_api_client.v1.model.formula_and_function_cloud_cost_query_definition import (
    FormulaAndFunctionCloudCostQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    title="Example-Dashboard",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                title="Example Cloud Cost Query",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TimeseriesWidgetDefinitionType.TIMESERIES,
                requests=[
                    TimeseriesWidgetRequest(
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionCloudCostQueryDefinition(
                                data_source=FormulaAndFunctionCloudCostDataSource.CLOUD_COST,
                                name="query1",
                                query="sum:aws.cost.amortized{*} by {aws_product}.rollup(sum, monthly)",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.TIMESERIES,
                        style=WidgetRequestStyle(
                            palette="dog_classic",
                            line_type=WidgetLineType.SOLID,
                            line_width=WidgetLineWidth.NORMAL,
                        ),
                        display_type=WidgetDisplayType.BARS,
                    ),
                ],
                time=WidgetTime(
                    live_span=WidgetLiveSpan.WEEK_TO_DATE,
                ),
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
