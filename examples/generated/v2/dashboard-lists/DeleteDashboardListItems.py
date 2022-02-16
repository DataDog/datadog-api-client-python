import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import dashboard_lists_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    dashboard_list_id = 1  # int | ID of the dashboard list to delete items from.
    body = DashboardListDeleteItemsRequest(
        dashboards=[
            DashboardListItemRequest(
                id="q5j-nti-fv6",
                type=DashboardType("host_timeboard"),
            ),
        ],
    )  # DashboardListDeleteItemsRequest | Dashboards to delete from the dashboard list.

    # example passing only required values which don't have defaults set
    try:
        # Delete items from a dashboard list
        api_response = api_instance.delete_dashboard_list_items(dashboard_list_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->delete_dashboard_list_items: %s\n" % e)
