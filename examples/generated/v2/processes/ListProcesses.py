import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import processes_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = processes_api.ProcessesApi(api_client)
    search = "search_example"  # str | String to search processes by. (optional)
    tags = "account:prod,user:admin"  # str | Comma-separated list of tags to filter processes by. (optional)
    _from = 1  # int | Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window will be 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`. (optional)
    to = 1  # int | Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window will be 15 minutes after the `from` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`. (optional)
    page_limit = 1000  # int | Maximum number of results returned. (optional) if omitted the server will use the default value of 1000
    page_cursor = "page[cursor]_example"  # str | String to query the next page of results. This key is provided with each valid response from the API in `meta.page.after`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all processes
        api_response = api_instance.list_processes(search=search, tags=tags, _from=_from, to=to, page_limit=page_limit, page_cursor=page_cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessesApi->list_processes: %s\n" % e)
