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
    body = APIKeyCreateRequest(
        data=APIKeyCreateData(
            attributes=APIKeyCreateAttributes(
                name="API Key for submitting metrics",
            ),
            type=APIKeysType("api_keys"),
        ),
    )  # APIKeyCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an API key
        api_response = api_instance.create_api_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->create_api_key: %s\n" % e)
