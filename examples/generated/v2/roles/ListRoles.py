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
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = RolesSort("name")  # RolesSort | Sort roles depending on the given field. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example: `sort=-name`. (optional)
    filter = "filter_example"  # str | Filter all roles by the given string. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List roles
        api_response = api_instance.list_roles(page_size=page_size, page_number=page_number, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
