"""
Create a new dashboard with powerpack widget
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.powerpack_template_variable_contents import PowerpackTemplateVariableContents
from datadog_api_client.v1.model.powerpack_template_variables import PowerpackTemplateVariables
from datadog_api_client.v1.model.powerpack_widget_definition import PowerpackWidgetDefinition
from datadog_api_client.v1.model.powerpack_widget_definition_type import PowerpackWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = environ["POWERPACK_DATA_ID"]

body = Dashboard(
    title="Example-Dashboard with powerpack widget",
    layout_type=DashboardLayoutType.ORDERED,
    widgets=[
        Widget(
            definition=PowerpackWidgetDefinition(
                type=PowerpackWidgetDefinitionType.POWERPACK,
                powerpack_id=POWERPACK_DATA_ID,
                template_variables=PowerpackTemplateVariables(
                    controlled_externally=[],
                    controlled_by_powerpack=[
                        PowerpackTemplateVariableContents(
                            name="foo",
                            prefix="bar",
                            values=[
                                "baz",
                                "qux",
                                "quuz",
                            ],
                        ),
                    ],
                ),
            ),
            layout=WidgetLayout(
                x=1,
                y=1,
                width=2,
                height=2,
                is_column_break=False,
            ),
        ),
    ],
    description="description",
    is_read_only=False,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
