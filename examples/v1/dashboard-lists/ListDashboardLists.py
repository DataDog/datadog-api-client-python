"""
Get all dashboard lists returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

with ApiClient(Configuration()) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.list_dashboard_lists()

    print(response)
