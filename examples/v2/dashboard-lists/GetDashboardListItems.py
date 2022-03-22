"""
Get items of a Dashboard List returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.get_dashboard_list_items(dashboard_list_id=9223372036854775807)

    print(response)
