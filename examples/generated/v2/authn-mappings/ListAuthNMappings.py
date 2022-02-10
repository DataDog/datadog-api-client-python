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
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = AuthNMappingsSort("created_at")  # AuthNMappingsSort | Sort AuthN Mappings depending on the given field. (optional)
    include = [
        "include_example",
    ]  # [str] |  (optional)
    filter = "filter_example"  # str | Filter all mappings by the given string. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all AuthN Mappings
        api_response = api_instance.list_auth_n_mappings(page_size=page_size, page_number=page_number, sort=sort, include=include, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthNMappingsApi->list_auth_n_mappings: %s\n" % e)
