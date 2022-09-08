"""
Add Items to a Dashboard List returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_add_items_request import DashboardListAddItemsRequest
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

body = DashboardListAddItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id="q5j-nti-fv6",
            type=DashboardType.HOST_TIMEBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.create_dashboard_list_items(dashboard_list_id=9223372036854775807, body=body)

    print(response)
