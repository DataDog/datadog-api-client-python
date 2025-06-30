"""
Create a shared dashboard with a group template variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard_global_time import DashboardGlobalTime
from datadog_api_client.v1.model.dashboard_global_time_live_span import DashboardGlobalTimeLiveSpan
from datadog_api_client.v1.model.dashboard_share_type import DashboardShareType
from datadog_api_client.v1.model.dashboard_type import DashboardType
from datadog_api_client.v1.model.selectable_template_variable_items import SelectableTemplateVariableItems
from datadog_api_client.v1.model.shared_dashboard import SharedDashboard

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

body = SharedDashboard(
    dashboard_id=DASHBOARD_ID,
    dashboard_type=DashboardType.CUSTOM_TIMEBOARD,
    share_type=DashboardShareType.OPEN,
    global_time=DashboardGlobalTime(
        live_span=DashboardGlobalTimeLiveSpan.PAST_ONE_HOUR,
    ),
    selectable_template_vars=[
        SelectableTemplateVariableItems(
            default_value="*",
            name="group_by_var",
            type="group",
            visible_tags=[
                "selectableValue1",
                "selectableValue2",
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_public_dashboard(body=body)

    print(response)
