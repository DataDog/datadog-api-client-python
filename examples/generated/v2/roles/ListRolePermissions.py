import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.

    # example passing only required values which don't have defaults set
    try:
        # List permissions for a role
        api_response = api_instance.list_role_permissions(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_role_permissions: %s\n" % e)
