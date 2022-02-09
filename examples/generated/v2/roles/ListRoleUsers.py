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
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = "name"  # str | User attribute to order results by. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `email`, `status`. (optional) if omitted the server will use the default value of "name"
    filter = "filter_example"  # str | Filter all users by the given string. Defaults to no filtering. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all users of a role
        api_response = api_instance.list_role_users(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_role_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all users of a role
        api_response = api_instance.list_role_users(role_id, page_size=page_size, page_number=page_number, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_role_users: %s\n" % e)
