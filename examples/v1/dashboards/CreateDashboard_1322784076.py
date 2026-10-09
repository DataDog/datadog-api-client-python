"""
Create a heatgrid widget with custom discrete thresholds
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.heatgrid_color_bin import HeatgridColorBin
from datadog_api_client.v1.model.heatgrid_custom_color_source import HeatgridCustomColorSource
from datadog_api_client.v1.model.heatgrid_discrete_custom_color import HeatgridDiscreteCustomColor
from datadog_api_client.v1.model.heatgrid_discrete_mode import HeatgridDiscreteMode
from datadog_api_client.v1.model.heatgrid_label_column import HeatgridLabelColumn
from datadog_api_client.v1.model.heatgrid_label_column_width import HeatgridLabelColumnWidth
from datadog_api_client.v1.model.heatgrid_legend import HeatgridLegend
from datadog_api_client.v1.model.heatgrid_nesting_display import HeatgridNestingDisplay
from datadog_api_client.v1.model.heatgrid_sort import HeatgridSort
from datadog_api_client.v1.model.heatgrid_sort_by_label import HeatgridSortByLabel
from datadog_api_client.v1.model.heatgrid_sort_by_label_property import HeatgridSortByLabelProperty
from datadog_api_client.v1.model.heatgrid_sort_order import HeatgridSortOrder
from datadog_api_client.v1.model.heatgrid_widget_definition import HeatgridWidgetDefinition
from datadog_api_client.v1.model.heatgrid_widget_definition_type import HeatgridWidgetDefinitionType
from datadog_api_client.v1.model.heatgrid_widget_formula import HeatgridWidgetFormula
from datadog_api_client.v1.model.heatgrid_widget_request import HeatgridWidgetRequest
from datadog_api_client.v1.model.heatgrid_widget_response_format import HeatgridWidgetResponseFormat
from datadog_api_client.v1.model.widget import Widget

body = Dashboard(
    title="Example-Dashboard",
    layout_type=DashboardLayoutType.ORDERED,
    widgets=[
        Widget(
            definition=HeatgridWidgetDefinition(
                type=HeatgridWidgetDefinitionType.HEATGRID,
                requests=[
                    HeatgridWidgetRequest(
                        response_format=HeatgridWidgetResponseFormat.TIMESERIES,
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:system.cpu.user{*} by {host}",
                            ),
                        ],
                        formulas=[
                            HeatgridWidgetFormula(
                                formula="query1",
                            ),
                        ],
                    ),
                ],
                sort=HeatgridSort(
                    nesting_display=HeatgridNestingDisplay.FLAT,
                    sort_by=HeatgridSortByLabel(
                        _property=HeatgridSortByLabelProperty.LABEL,
                        order=HeatgridSortOrder.ASC,
                    ),
                ),
                color=HeatgridDiscreteCustomColor(
                    mode=HeatgridDiscreteMode.DISCRETE,
                    source=HeatgridCustomColorSource.CUSTOM,
                    bins=[
                        HeatgridColorBin(
                            color="#00FF00",
                        ),
                        HeatgridColorBin(
                            color="#FF0000",
                            lower_bound=80.0,
                        ),
                    ],
                ),
                legend=HeatgridLegend(
                    show_caption=True,
                ),
                label_column=HeatgridLabelColumn(
                    width=HeatgridLabelColumnWidth.M,
                ),
            ),
        ),
    ],
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
