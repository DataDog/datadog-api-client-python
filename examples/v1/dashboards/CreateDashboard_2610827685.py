"""
Create a new dashboard with run-workflow widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.run_workflow_widget_definition import RunWorkflowWidgetDefinition
from datadog_api_client.v1.model.run_workflow_widget_definition_type import RunWorkflowWidgetDefinitionType
from datadog_api_client.v1.model.run_workflow_widget_input import RunWorkflowWidgetInput
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

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
            definition=RunWorkflowWidgetDefinition(
                title="Run workflow title",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetTime(),
                type=RunWorkflowWidgetDefinitionType.RUN_WORKFLOW,
                workflow_id="2e055f16-8b6a-4cdd-b452-17a34c44b160",
                inputs=[
                    RunWorkflowWidgetInput(
                        name="environment",
                        value="$env.value",
                    ),
                ],
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    is_read_only=False,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
