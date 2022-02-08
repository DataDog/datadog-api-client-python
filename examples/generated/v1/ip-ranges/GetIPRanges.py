import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import ip_ranges_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ip_ranges_api.IPRangesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List IP Ranges
        api_response = api_instance.get_ip_ranges()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPRangesApi->get_ip_ranges: %s\n" % e)
