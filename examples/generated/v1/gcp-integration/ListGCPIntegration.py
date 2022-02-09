import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import gcp_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gcp_integration_api.GCPIntegrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all GCP integrations
        api_response = api_instance.list_gcp_integration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GCPIntegrationApi->list_gcp_integration: %s\n" % e)
