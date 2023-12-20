"""
Create a new dashboard with split graph widget from distribution widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.distribution_widget_definition_type import DistributionWidgetDefinitionType
from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest
from datadog_api_client.v1.model.distribution_widget_x_axis import DistributionWidgetXAxis
from datadog_api_client.v1.model.distribution_widget_y_axis import DistributionWidgetYAxis
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.split_config import SplitConfig
from datadog_api_client.v1.model.split_config_sort_compute import SplitConfigSortCompute
from datadog_api_client.v1.model.split_dimension import SplitDimension
from datadog_api_client.v1.model.split_graph_viz_size import SplitGraphVizSize
from datadog_api_client.v1.model.split_graph_widget_definition import SplitGraphWidgetDefinition
from datadog_api_client.v1.model.split_graph_widget_definition_type import SplitGraphWidgetDefinitionType
from datadog_api_client.v1.model.split_sort import SplitSort
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_sort import WidgetSort
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=12,
                height=8,
            ),
            definition=SplitGraphWidgetDefinition(
                title="",
                type=SplitGraphWidgetDefinitionType.SPLIT_GROUP,
                source_widget_definition=DistributionWidgetDefinition(
                    title="",
                    title_size="16",
                    title_align=WidgetTextAlign.LEFT,
                    type=DistributionWidgetDefinitionType.DISTRIBUTION,
                    requests=[
                        DistributionWidgetRequest(
                            response_format=FormulaAndFunctionResponseFormat.SCALAR,
                            queries=[
                                FormulaAndFunctionMetricQueryDefinition(
                                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                    name="query1",
                                    query="avg:system.cpu.user{*} by {service}",
                                    aggregator=FormulaAndFunctionMetricAggregation.AVG,
                                ),
                            ],
                        ),
                    ],
                    xaxis=DistributionWidgetXAxis(
                        scale="linear",
                        include_zero=True,
                        min="auto",
                        max="auto",
                    ),
                    yaxis=DistributionWidgetYAxis(
                        scale="linear",
                        include_zero=True,
                        min="auto",
                        max="auto",
                    ),
                ),
                split_config=SplitConfig(
                    split_dimensions=[
                        SplitDimension(
                            one_graph_per="service",
                        ),
                    ],
                    limit=6,
                    sort=SplitSort(
                        compute=SplitConfigSortCompute(
                            aggregation="sum",
                            metric="system.cpu.user",
                        ),
                        order=WidgetSort.DESCENDING,
                    ),
                ),
                size=SplitGraphVizSize.MD,
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.ORDERED,
    is_read_only=False,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
