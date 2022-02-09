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
    body = APIKeyUpdateRequest(
        data=APIKeyUpdateData(
            attributes=APIKeyUpdateAttributes(
                name="API Key for submitting metrics",
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=APIKeysType("api_keys"),
        ),
    )  # APIKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an API key
        api_response = api_instance.update_api_key(api_key_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->update_api_key: %s\n" % e)
