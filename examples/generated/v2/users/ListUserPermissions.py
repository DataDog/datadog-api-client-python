import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the user.

    # example passing only required values which don't have defaults set
    try:
        # Get a user permissions
        api_response = api_instance.list_user_permissions(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_user_permissions: %s\n" % e)
