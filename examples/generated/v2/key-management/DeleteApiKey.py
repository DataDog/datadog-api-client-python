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

    # example passing only required values which don't have defaults set
    try:
        # Delete an API key
        api_instance.delete_api_key(api_key_id)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->delete_api_key: %s\n" % e)
