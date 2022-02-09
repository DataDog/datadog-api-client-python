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
    public_id = "public_id_example"  # str | The public ID of the API test to which the target result belongs.
    result_id = "result_id_example"  # str | The ID of the result to get.

    # example passing only required values which don't have defaults set
    try:
        # Get an API test result
        api_response = api_instance.get_api_test_result(public_id, result_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_api_test_result: %s\n" % e)
