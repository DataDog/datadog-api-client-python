"""
Create a dashboard list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v1.model.dashboard_list import DashboardList

body = DashboardList(
    name="Example-Create_a_dashboard_list_returns_OK_response",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.create_dashboard_list(body=body)

    print(response)
