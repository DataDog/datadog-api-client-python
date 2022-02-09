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
    location_id = "location_id_example"  # str | The ID of the private location.
    body = SyntheticsPrivateLocation(
        description="Description of private location",
        name="New private location",
        tags=["team:front"],
    )  # SyntheticsPrivateLocation | Details of the private location to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Edit a private location
        api_response = api_instance.update_private_location(location_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->update_private_location: %s\n" % e)
