"""
Create a new dashboard with template variable presets using values returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
from datadog_api_client.v1.model.dashboard_template_variable import DashboardTemplateVariable
from datadog_api_client.v1.model.dashboard_template_variable_preset import DashboardTemplateVariablePreset
from datadog_api_client.v1.model.dashboard_template_variable_preset_value import DashboardTemplateVariablePresetValue
from datadog_api_client.v1.model.host_map_request import HostMapRequest
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition
from datadog_api_client.v1.model.host_map_widget_definition_requests import HostMapWidgetDefinitionRequests
from datadog_api_client.v1.model.host_map_widget_definition_type import HostMapWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget

body = Dashboard(
    description=None,
    is_read_only=False,
    layout_type=DashboardLayoutType.ORDERED,
    notify_list=[],
    reflow_type=DashboardReflowType.AUTO,
    restricted_roles=[],
    template_variable_presets=[
        DashboardTemplateVariablePreset(
            name="my saved view",
            template_variables=[
                DashboardTemplateVariablePresetValue(
                    name="datacenter",
                    values=[
                        "*",
                        "my-host",
                    ],
                ),
            ],
        ),
    ],
    template_variables=[
        DashboardTemplateVariable(
            available_values=[
                "my-host",
                "host1",
                "host2",
            ],
            defaults=[
                "my-host",
            ],
            name="host1",
            prefix="host",
        ),
    ],
    title="",
    widgets=[
        Widget(
            definition=HostMapWidgetDefinition(
                requests=HostMapWidgetDefinitionRequests(
                    fill=HostMapRequest(
                        q="avg:system.cpu.user{*}",
                    ),
                ),
                type=HostMapWidgetDefinitionType.HOSTMAP,
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
