import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import key_management_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    key = "key_example"  # str | The specific APP key you are working with.
    body = ApplicationKey(
        name="example user",
    )  # ApplicationKey | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an application key
        api_response = api_instance.update_application_key(key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->update_application_key: %s\n" % e)
