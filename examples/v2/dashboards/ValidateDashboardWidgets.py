"""
Validate dashboard widgets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi
from datadog_api_client.v2.model.dashboard_widget_validation_layout_type import DashboardWidgetValidationLayoutType
from datadog_api_client.v2.model.dashboard_widget_validation_reflow_type import DashboardWidgetValidationReflowType
from datadog_api_client.v2.model.dashboard_widget_validation_request import DashboardWidgetValidationRequest
from datadog_api_client.v2.model.dashboard_widget_validation_widget import DashboardWidgetValidationWidget

body = DashboardWidgetValidationRequest(
    layout_type=DashboardWidgetValidationLayoutType.ORDERED,
    reflow_type=DashboardWidgetValidationReflowType.AUTO,
    widgets=[
        DashboardWidgetValidationWidget([("definition", "{'content': 'Valid note', 'type': 'note'}")]),
    ],
)

configuration = Configuration()
configuration.unstable_operations["validate_dashboard_widgets"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.validate_dashboard_widgets(body=body)

    print(response)
