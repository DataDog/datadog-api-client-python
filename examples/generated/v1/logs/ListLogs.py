import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    body = LogsListRequest(
        index="retention-3,retention-15",
        limit=1,
        query="service:web* AND @http.status_code:[200 TO 299]",
        sort=LogsSort("asc"),
        start_at="start_at_example",
        time=LogsListRequestTime(
            _from=dateutil_parser('2020-02-02T02:02:02Z'),
            timezone="timezone_example",
            to=dateutil_parser('2020-02-02T20:20:20Z'),
        ),
    )  # LogsListRequest | Logs filter

    # example passing only required values which don't have defaults set
    try:
        # Search logs
        api_response = api_instance.list_logs(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)
