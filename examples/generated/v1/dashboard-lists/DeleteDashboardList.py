import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboard_lists_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    list_id = 1  # int | ID of the dashboard list to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a dashboard list
        api_response = api_instance.delete_dashboard_list(list_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->delete_dashboard_list: %s\n" % e)
