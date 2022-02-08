import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import hosts_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hosts_api.HostsApi(api_client)
    _from = 1  # int | Number of seconds from which you want to get total number of active hosts. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the total number of active hosts
        api_response = api_instance.get_host_totals(_from=_from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->get_host_totals: %s\n" % e)
