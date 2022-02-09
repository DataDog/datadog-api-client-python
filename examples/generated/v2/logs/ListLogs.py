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
    body = LogsListRequest(
        filter=LogsQueryFilter(
            _from="now-15m",
            indexes=["main","web"],
            query="service:web* AND @http.status_code:[200 TO 299]",
            to="now",
        ),
        options=LogsQueryOptions(
            time_offset=1,
            timezone="GMT",
        ),
        page=LogsListRequestPage(
            cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
            limit=25,
        ),
        sort=LogsSort("timestamp"),
    )  # LogsListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search logs
        api_response = api_instance.list_logs(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)
