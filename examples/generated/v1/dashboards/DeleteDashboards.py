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
    body = DashboardBulkDeleteRequest(
        data=DashboardBulkActionDataList([
            DashboardBulkActionData(
                id="123-abc-456",
                type=DashboardResourceType("dashboard"),
            ),
        ]),
    )  # DashboardBulkDeleteRequest | Delete dashboards request body.

    # example passing only required values which don't have defaults set
    try:
        # Delete dashboards
        api_instance.delete_dashboards(body)
    except ApiException as e:
        print("Exception when calling DashboardsApi->delete_dashboards: %s\n" % e)
