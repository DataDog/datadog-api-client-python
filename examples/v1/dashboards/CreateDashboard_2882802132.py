"""
Create a new dashboard with hostmap infra widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition
from datadog_api_client.v1.model.host_map_widget_definition_requests import HostMapWidgetDefinitionRequests
from datadog_api_client.v1.model.host_map_widget_definition_type import HostMapWidgetDefinitionType
from datadog_api_client.v1.model.host_map_widget_dimension import HostMapWidgetDimension
from datadog_api_client.v1.model.host_map_widget_formula import HostMapWidgetFormula
from datadog_api_client.v1.model.host_map_widget_group_by import HostMapWidgetGroupBy
from datadog_api_client.v1.model.host_map_widget_infrastructure_request_request_type import (
    HostMapWidgetInfrastructureRequestRequestType,
)
from datadog_api_client.v1.model.host_map_widget_infrastructure_style import HostMapWidgetInfrastructureStyle
from datadog_api_client.v1.model.host_map_widget_node_type import HostMapWidgetNodeType
from datadog_api_client.v1.model.host_map_widget_scalar_request import HostMapWidgetScalarRequest
from datadog_api_client.v1.model.host_map_widget_scalar_request_response_format import (
    HostMapWidgetScalarRequestResponseFormat,
)
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description=None,
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=22,
            ),
            definition=HostMapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=HostMapWidgetDefinitionType.HOSTMAP,
                requests=HostMapWidgetDefinitionRequests(
                    request_type=HostMapWidgetInfrastructureRequestRequestType.INFRASTRUCTURE_HOSTMAP,
                    node_type=HostMapWidgetNodeType.HOST,
                    filter="env:prod",
                    group_by=[
                        HostMapWidgetGroupBy(
                            column="tags",
                            key="service",
                        ),
                    ],
                    enrichments=[
                        HostMapWidgetScalarRequest(
                            response_format=HostMapWidgetScalarRequestResponseFormat.SCALAR,
                            queries=[
                                FormulaAndFunctionMetricQueryDefinition(
                                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                    name="query1",
                                    query="avg:system.cpu.user{*} by {host}",
                                ),
                            ],
                            formulas=[
                                HostMapWidgetFormula(
                                    formula="query1",
                                    dimension=HostMapWidgetDimension.FILL,
                                ),
                            ],
                        ),
                    ],
                    style=HostMapWidgetInfrastructureStyle(
                        palette="green_to_orange",
                        palette_flip=False,
                    ),
                ),
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
