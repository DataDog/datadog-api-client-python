"""
Create a new dashboard with apm resource stats widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_apm_resource_stat_name import (
    FormulaAndFunctionApmResourceStatName,
)
from datadog_api_client.v1.model.formula_and_function_apm_resource_stats_data_source import (
    FormulaAndFunctionApmResourceStatsDataSource,
)
from datadog_api_client.v1.model.formula_and_function_apm_resource_stats_query_definition import (
    FormulaAndFunctionApmResourceStatsQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_apm_resource_stats_widget",
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
                            FormulaAndFunctionApmResourceStatsQueryDefinition(
                                primary_tag_value="edge-eu1.prod.dog",
                                stat=FormulaAndFunctionApmResourceStatName.HITS,
                                name="query1",
                                service="cassandra",
                                data_source=FormulaAndFunctionApmResourceStatsDataSource.APM_RESOURCE_STATS,
                                env="ci",
                                primary_tag_name="datacenter",
                                operation_name="cassandra.query",
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
