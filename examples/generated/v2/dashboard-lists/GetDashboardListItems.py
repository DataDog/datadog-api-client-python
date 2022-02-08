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
    dashboard_list_id = 1  # int | ID of the dashboard list to get items from.

    # example passing only required values which don't have defaults set
    try:
        # Get items of a Dashboard List
        api_response = api_instance.get_dashboard_list_items(dashboard_list_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->get_dashboard_list_items: %s\n" % e)
