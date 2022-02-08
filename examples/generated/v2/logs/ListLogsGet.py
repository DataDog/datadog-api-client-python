import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    filter_query = "@datacenter:us @role:db"  # str | Search query following logs syntax. (optional)
    filter_index = "main"  # str | For customers with multiple indexes, the indexes to search Defaults to '*' which means all indexes (optional)
    filter_from = dateutil_parser('2019-01-02T09:42:36.320Z')  # datetime | Minimum timestamp for requested logs. (optional)
    filter_to = dateutil_parser('2019-01-03T09:42:36.320Z')  # datetime | Maximum timestamp for requested logs. (optional)
    sort = LogsSort("timestamp")  # LogsSort | Order of logs in results. (optional)
    page_cursor = "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="  # str | List following results with a cursor provided in the previous query. (optional)
    page_limit = 25  # int | Maximum number of logs in the response. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of logs
        api_response = api_instance.list_logs_get(filter_query=filter_query, filter_index=filter_index, filter_from=filter_from, filter_to=filter_to, sort=sort, page_cursor=page_cursor, page_limit=page_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->list_logs_get: %s\n" % e)
