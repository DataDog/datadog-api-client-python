import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = "dashboard_id_example"  # str | The ID of the dashboard.

    # example passing only required values which don't have defaults set
    try:
        # Get a dashboard
        api_response = api_instance.get_dashboard(dashboard_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
