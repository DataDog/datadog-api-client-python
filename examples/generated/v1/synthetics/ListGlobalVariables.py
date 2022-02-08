import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all global variables
        api_response = api_instance.list_global_variables()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->list_global_variables: %s\n" % e)
