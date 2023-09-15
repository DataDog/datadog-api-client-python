"""
Create a new dashboard with split graph widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
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
from datadog_api_client.v1.model.split_vector_entry_item import SplitVectorEntryItem
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle
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
                source_widget_definition=TimeseriesWidgetDefinition(
                    title="",
                    title_size="16",
                    title_align=WidgetTextAlign.LEFT,
                    type=TimeseriesWidgetDefinitionType.TIMESERIES,
                    requests=[
                        TimeseriesWidgetRequest(
                            response_format=FormulaAndFunctionResponseFormat.TIMESERIES,
                            queries=[
                                FormulaAndFunctionMetricQueryDefinition(
                                    name="query1",
                                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                    query="avg:system.cpu.user{*}",
                                ),
                            ],
                            style=WidgetRequestStyle(
                                palette="dog_classic",
                                line_type=WidgetLineType.SOLID,
                                line_width=WidgetLineWidth.NORMAL,
                            ),
                            display_type=WidgetDisplayType.LINE,
                        ),
                    ],
                ),
                split_config=SplitConfig(
                    split_dimensions=[
                        SplitDimension(
                            one_graph_per="service",
                        ),
                    ],
                    limit=24,
                    sort=SplitSort(
                        compute=SplitConfigSortCompute(
                            aggregation="sum",
                            metric="system.cpu.user",
                        ),
                        order=WidgetSort.DESCENDING,
                    ),
                    static_splits=[
                        [
                            SplitVectorEntryItem(
                                tag_key="service",
                                tag_values=[
                                    "cassandra",
                                ],
                            ),
                            SplitVectorEntryItem(
                                tag_key="datacenter",
                                tag_values=[],
                            ),
                        ],
                        [
                            SplitVectorEntryItem(
                                tag_key="demo",
                                tag_values=[
                                    "env",
                                ],
                            ),
                        ],
                    ],
                ),
                size=SplitGraphVizSize.MD,
                has_uniform_y_axes=True,
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
