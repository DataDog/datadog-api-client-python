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
    body = LogsAggregateRequest(
        compute=[
            LogsCompute(
                aggregation=LogsAggregationFunction("pc90"),
                interval="5m",
                metric="@duration",
                type=LogsComputeType("total"),
            ),
        ],
        filter=LogsQueryFilter(
            _from="now-15m",
            indexes=["main","web"],
            query="service:web* AND @http.status_code:[200 TO 299]",
            to="now",
        ),
        group_by=[
            LogsGroupBy(
                facet="host",
                histogram=LogsGroupByHistogram(
                    interval=10,
                    max=100,
                    min=50,
                ),
                limit=10,
                missing=LogsGroupByMissing(),
                sort=LogsAggregateSort(
                    aggregation=LogsAggregationFunction("pc90"),
                    metric="@duration",
                    order=LogsSortOrder("asc"),
                    type=LogsAggregateSortType("alphabetical"),
                ),
                total=LogsGroupByTotal(),
            ),
        ],
        options=LogsQueryOptions(
            time_offset=1,
            timezone="GMT",
        ),
        page=LogsAggregateRequestPage(
            cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
        ),
    )  # LogsAggregateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Aggregate events
        api_response = api_instance.aggregate_logs(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->aggregate_logs: %s\n" % e)
