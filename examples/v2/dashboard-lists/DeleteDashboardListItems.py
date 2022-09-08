"""
Delete items from a dashboard list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_delete_items_request import DashboardListDeleteItemsRequest
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

body = DashboardListDeleteItemsRequest(
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
    response = api_instance.delete_dashboard_list_items(dashboard_list_id=9223372036854775807, body=body)

    print(response)
