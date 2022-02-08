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
    filter_shared = True  # bool | When `true`, this query only returns shared custom created or cloned dashboards. (optional)
    filter_deleted = True  # bool | When `true`, this query returns only deleted custom-created or cloned dashboards. This parameter is incompatible with `filter[shared]`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all dashboards
        api_response = api_instance.list_dashboards(filter_shared=filter_shared, filter_deleted=filter_deleted)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->list_dashboards: %s\n" % e)
