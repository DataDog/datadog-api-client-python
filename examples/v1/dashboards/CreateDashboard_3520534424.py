"""
Create a new dashboard with timeseries widget with custom_unit
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.number_format_unit_canonical import NumberFormatUnitCanonical
from datadog_api_client.v1.model.number_format_unit_scale import NumberFormatUnitScale
from datadog_api_client.v1.model.number_format_unit_scale_type import NumberFormatUnitScaleType
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_legend_layout import TimeseriesWidgetLegendLayout
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
from datadog_api_client.v1.model.widget_number_format import WidgetNumberFormat
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                show_legend=True,
                legend_layout=TimeseriesWidgetLegendLayout.AUTO,
                time=WidgetLegacyLiveSpan(),
                type=TimeseriesWidgetDefinitionType.TIMESERIES,
                requests=[
                    TimeseriesWidgetRequest(
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                                number_format=WidgetNumberFormat(
                                    unit_scale=NumberFormatUnitScale(
                                        type=NumberFormatUnitScaleType.CANONICAL_UNIT,
                                        unit_name="apdex",
                                    ),
                                    unit=NumberFormatUnitCanonical(
                                        type=NumberFormatUnitScaleType.CANONICAL_UNIT,
                                        unit_name="fraction",
                                    ),
                                ),
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:system.cpu.user{*}",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.TIMESERIES,
                        display_type=WidgetDisplayType.LINE,
                    ),
                ],
            ),
            layout=WidgetLayout(
                x=0,
                y=0,
                width=12,
                height=5,
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.ORDERED,
    notify_list=[],
    reflow_type=DashboardReflowType.FIXED,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
