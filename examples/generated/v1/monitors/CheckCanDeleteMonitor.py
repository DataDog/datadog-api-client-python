import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    monitor_ids = [
        1,
    ]  # [int] | The IDs of the monitor to check.

    # example passing only required values which don't have defaults set
    try:
        # Check if a monitor can be deleted
        api_response = api_instance.check_can_delete_monitor(monitor_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->check_can_delete_monitor: %s\n" % e)
