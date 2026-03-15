"""
Create a new dashboard with apm metrics widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_apm_metric_stat_name import FormulaAndFunctionApmMetricStatName
from datadog_api_client.v1.model.formula_and_function_apm_metrics_data_source import (
    FormulaAndFunctionApmMetricsDataSource,
)
from datadog_api_client.v1.model.formula_and_function_apm_metrics_query_definition import (
    FormulaAndFunctionApmMetricsQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    widgets=[
        Widget(
            definition=TableWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TableWidgetDefinitionType.QUERY_TABLE,
                requests=[
                    TableWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        queries=[
                            FormulaAndFunctionApmMetricsQueryDefinition(
                                stat=FormulaAndFunctionApmMetricStatName.HITS,
                                name="query1",
                                service="web-store",
                                data_source=FormulaAndFunctionApmMetricsDataSource.APM_METRICS,
                                query_filter="env:prod",
                                group_by=[
                                    "resource_name",
                                ],
                            ),
                        ],
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
    layout_type=DashboardLayoutType.ORDERED,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
