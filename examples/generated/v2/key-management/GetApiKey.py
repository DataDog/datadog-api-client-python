import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example"  # str | The ID of the API key.
    include = "created_by,modified_by"  # str | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get API key
        api_response = api_instance.get_api_key(api_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->get_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get API key
        api_response = api_instance.get_api_key(api_key_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->get_api_key: %s\n" % e)
