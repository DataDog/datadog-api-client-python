"""
Create a new dashboard with a toplist widget with stacked type and no legend specified
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
from datadog_api_client.v1.model.group_type import GroupType
from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition
from datadog_api_client.v1.model.toplist_widget_definition_type import ToplistWidgetDefinitionType
from datadog_api_client.v1.model.toplist_widget_request import ToplistWidgetRequest
from datadog_api_client.v1.model.toplist_widget_scaling import ToplistWidgetScaling
from datadog_api_client.v1.model.toplist_widget_stacked import ToplistWidgetStacked
from datadog_api_client.v1.model.toplist_widget_stacked_type import ToplistWidgetStackedType
from datadog_api_client.v1.model.toplist_widget_style import ToplistWidgetStyle
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_group_sort import WidgetGroupSort
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
                width=47,
                height=15,
            ),
            definition=ToplistWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetLegacyLiveSpan(),
                style=ToplistWidgetStyle(
                    display=ToplistWidgetStacked(
                        type=ToplistWidgetStackedType.STACKED,
                    ),
                    scaling=ToplistWidgetScaling.RELATIVE,
                    palette="dog_classic",
                ),
                type=ToplistWidgetDefinitionType.TOPLIST,
                requests=[
                    ToplistWidgetRequest(
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:system.cpu.user{*} by {service}",
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                            ),
                        ],
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                            ),
                        ],
                        sort=WidgetSortBy(
                            count=10,
                            order_by=[
                                WidgetGroupSort(
                                    type=GroupType.GROUP,
                                    name="service",
                                    order=WidgetSort.ASCENDING,
                                ),
                            ],
                        ),
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                    ),
                ],
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
