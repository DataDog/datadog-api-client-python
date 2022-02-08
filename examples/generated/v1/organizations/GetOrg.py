import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import organizations_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    public_id = "abc123"  # str | The `public_id` of the organization you are operating within.

    # example passing only required values which don't have defaults set
    try:
        # Get organization information
        api_response = api_instance.get_org(public_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationsApi->get_org: %s\n" % e)
