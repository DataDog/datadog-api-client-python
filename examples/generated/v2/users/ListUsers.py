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
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = "name"  # str | User attribute to order results by. Sort order is ascending by default. Sort order is descending if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `modified_at`, `user_count`. (optional) if omitted the server will use the default value of "name"
    sort_dir = QuerySortOrder("desc")  # QuerySortOrder | Direction of sort. Options: `asc`, `desc`. (optional)
    filter = "filter_example"  # str | Filter all users by the given string. Defaults to no filtering. (optional)
    filter_status = "Active"  # str | Filter on status attribute. Comma separated list, with possible values `Active`, `Pending`, and `Disabled`. Defaults to no filtering. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all users
        api_response = api_instance.list_users(page_size=page_size, page_number=page_number, sort=sort, sort_dir=sort_dir, filter=filter, filter_status=filter_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
