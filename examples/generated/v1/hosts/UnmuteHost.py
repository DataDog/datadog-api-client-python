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
    host_name = "host_name_example"  # str | Name of the host to unmute.

    # example passing only required values which don't have defaults set
    try:
        # Unmute a host
        api_response = api_instance.unmute_host(host_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->unmute_host: %s\n" % e)
