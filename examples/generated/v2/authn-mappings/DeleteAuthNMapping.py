import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import auth_n_mappings_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_n_mappings_api.AuthNMappingsApi(api_client)
    authn_mapping_id = "authn_mapping_id_example"  # str | The UUID of the AuthN Mapping.

    # example passing only required values which don't have defaults set
    try:
        # Delete an AuthN Mapping
        api_instance.delete_auth_n_mapping(authn_mapping_id)
    except ApiException as e:
        print("Exception when calling AuthNMappingsApi->delete_auth_n_mapping: %s\n" % e)
