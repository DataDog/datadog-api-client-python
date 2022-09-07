"""
Update items of a dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_list_update_items_request import DashboardListUpdateItemsRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = environ["SCREENBOARD_DASHBOARD_ID"]

body = DashboardListUpdateItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id=SCREENBOARD_DASHBOARD_ID,
            type=DashboardType.CUSTOM_SCREENBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.update_dashboard_list_items(dashboard_list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
