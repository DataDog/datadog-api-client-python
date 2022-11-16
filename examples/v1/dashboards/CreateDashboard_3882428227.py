"""
Create a distribution widget using a histogram request containing a formulas and functions events query
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.distribution_widget_definition_type import DistributionWidgetDefinitionType
from datadog_api_client.v1.model.distribution_widget_histogram_request_type import (
    DistributionWidgetHistogramRequestType,
)
from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest
from datadog_api_client.v1.model.distribution_widget_x_axis import DistributionWidgetXAxis
from datadog_api_client.v1.model.distribution_widget_y_axis import DistributionWidgetYAxis
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
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_distribution_widget_using_a_histogram_request_containing_a_formulas_and_functions_events_qu",
    description="Example-Create_a_distribution_widget_using_a_histogram_request_containing_a_formulas_and_functions_events_qu",
    widgets=[
        Widget(
            definition=DistributionWidgetDefinition(
                title="Events Platform - Request latency HOP",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                show_legend=False,
                type=DistributionWidgetDefinitionType.DISTRIBUTION,
                xaxis=DistributionWidgetXAxis(
                    max="auto",
                    include_zero=True,
                    scale="linear",
                    min="auto",
                ),
                yaxis=DistributionWidgetYAxis(
                    max="auto",
                    include_zero=True,
                    scale="linear",
                    min="auto",
                ),
                requests=[
                    DistributionWidgetRequest(
                        query=FormulaAndFunctionEventQueryDefinition(
                            search=FormulaAndFunctionEventQueryDefinitionSearch(
                                query="",
                            ),
                            data_source=FormulaAndFunctionEventsDataSource.EVENTS,
                            compute=FormulaAndFunctionEventQueryDefinitionCompute(
                                metric="@duration",
                                aggregation=FormulaAndFunctionEventAggregation.MIN,
                            ),
                            name="query1",
                            indexes=[
                                "*",
                            ],
                            group_by=[],
                        ),
                        request_type=DistributionWidgetHistogramRequestType.HISTOGRAM,
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
