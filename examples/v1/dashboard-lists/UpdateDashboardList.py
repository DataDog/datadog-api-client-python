"""
Update a dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v1.model.dashboard_list import DashboardList

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

body = DashboardList(
    name="updated Example-Update_a_dashboard_list_returns_OK_response",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.update_dashboard_list(list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
