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
    monitor_id = 1  # int | The ID of the monitor
    group_states = "group_states_example"  # str | When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a monitor's details
        api_response = api_instance.get_monitor(monitor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->get_monitor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a monitor's details
        api_response = api_instance.get_monitor(monitor_id, group_states=group_states)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->get_monitor: %s\n" % e)
