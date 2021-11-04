# datadog_api_client.v2.LogsApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                          | HTTP request                              | Description        |
| ----------------------------------------------- | ----------------------------------------- | ------------------ |
| [**aggregate_logs**](LogsApi.md#aggregate_logs) | **POST** /api/v2/logs/analytics/aggregate | Aggregate events   |
| [**list_logs**](LogsApi.md#list_logs)           | **POST** /api/v2/logs/events/search       | Search logs        |
| [**list_logs_get**](LogsApi.md#list_logs_get)   | **GET** /api/v2/logs/events               | Get a list of logs |
| [**submit_log**](LogsApi.md#submit_log)         | **POST** /api/v2/logs                     | Send logs          |

# **aggregate_logs**

> LogsAggregateResponse aggregate_logs(body)

The API endpoint to aggregate events into buckets and compute metrics and timeseries.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
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
```

### Parameters

| Name     | Type                                                | Description | Notes |
| -------- | --------------------------------------------------- | ----------- | ----- |
| **body** | [**LogsAggregateRequest**](LogsAggregateRequest.md) |             |

### Return type

[**LogsAggregateResponse**](LogsAggregateResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description    | Response headers |
| ----------- | -------------- | ---------------- |
| **200**     | OK             | -                |
| **400**     | Bad Request    | -                |
| **403**     | Not Authorized | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs**

> LogsListResponse list_logs()

List endpoint returns logs that match a log search query.
[Results are paginated][1].

Use this endpoint to build complex logs filtering and search.

**If you are considering archiving logs for your organization,
consider use of the Datadog archive capabilities instead of the log list API.
See [Datadog Logs Archive documentation][2].**

[1]: /logs/guide/collect-multiple-logs-with-pagination
[2]: https://docs.datadoghq.com/logs/archives

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
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
```

### Parameters

| Name     | Type                                      | Description | Notes      |
| -------- | ----------------------------------------- | ----------- | ---------- |
| **body** | [**LogsListRequest**](LogsListRequest.md) |             | [optional] |

### Return type

[**LogsListResponse**](LogsListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description    | Response headers |
| ----------- | -------------- | ---------------- |
| **200**     | OK             | -                |
| **400**     | Bad Request    | -                |
| **403**     | Not Authorized | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs_get**

> LogsListResponse list_logs_get()

List endpoint returns logs that match a log search query.
[Results are paginated][1].

Use this endpoint to see your latest logs.

**If you are considering archiving logs for your organization,
consider use of the Datadog archive capabilities instead of the log list API.
See [Datadog Logs Archive documentation][2].**

[1]: /logs/guide/collect-multiple-logs-with-pagination
[2]: https://docs.datadoghq.com/logs/archives

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
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
```

### Parameters

| Name             | Type         | Description                                                                                                 | Notes                                                             |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **filter_query** | **str**      | Search query following logs syntax.                                                                         | [optional]                                                        |
| **filter_index** | **str**      | For customers with multiple indexes, the indexes to search Defaults to &#39;\*&#39; which means all indexes | [optional]                                                        |
| **filter_from**  | **datetime** | Minimum timestamp for requested logs.                                                                       | [optional]                                                        |
| **filter_to**    | **datetime** | Maximum timestamp for requested logs.                                                                       | [optional]                                                        |
| **sort**         | **LogsSort** | Order of logs in results.                                                                                   | [optional]                                                        |
| **page_cursor**  | **str**      | List following results with a cursor provided in the previous query.                                        | [optional]                                                        |
| **page_limit**   | **int**      | Maximum number of logs in the response.                                                                     | [optional] if omitted the server will use the default value of 10 |

### Return type

[**LogsListResponse**](LogsListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description    | Response headers |
| ----------- | -------------- | ---------------- |
| **200**     | OK             | -                |
| **400**     | Bad Request    | -                |
| **403**     | Not Authorized | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **submit_log**

> dict submit_log(body)

Send your logs to your Datadog platform over HTTP. Limits per HTTP request are:

- Maximum content size per payload (uncompressed): 5MB
- Maximum size for a single log: 1MB
- Maximum array size if sending multiple logs in an array: 1000 entries

Any log exceeding 1MB is accepted and truncated by Datadog:

- For a single log request, the API truncates the log at 1MB and returns a 2xx.
- For a multi-logs request, the API processes all logs, truncates only logs larger than 1MB, and returns a 2xx.

Datadog recommends sending your logs compressed.
Add the `Content-Encoding: gzip` header to the request when sending compressed logs.

The status codes answered by the HTTP API are:

- 202: Accepted: the request has been accepted for processing
- 400: Bad request (likely an issue in the payload formatting)
- 401: Unauthorized (likely a missing API Key)
- 403: Permission issue (likely using an invalid API Key)
- 408: Request Timeout, request should be retried after some time
- 413: Payload too large (batch is above 5MB uncompressed)
- 429: Too Many Requests, request should be retried after some time
- 500: Internal Server Error, the server encountered an unexpected condition that prevented it from fulfilling the request, request should be retried after some time
- 503: Service Unavailable, the server is not ready to handle the request probably because it is overloaded, request should be retried after some time

### Example

- Api Key Authentication (apiKeyAuth):

```python
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
    body = HTTPLog([
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
            service="payment",
        ),
    ])  # HTTPLog | Log to send (JSON format).
    content_encoding = ContentEncoding("gzip")  # ContentEncoding | HTTP header used to compress the media-type. (optional)
    ddtags = "env:prod,user:my-user"  # str | Log tags can be passed as query parameters with `text/plain` content type. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send logs
        api_response = api_instance.submit_log(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->submit_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send logs
        api_response = api_instance.submit_log(body, content_encoding=content_encoding, ddtags=ddtags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->submit_log: %s\n" % e)
```

### Parameters

| Name                 | Type                      | Description                                                                          | Notes      |
| -------------------- | ------------------------- | ------------------------------------------------------------------------------------ | ---------- |
| **body**             | [**HTTPLog**](HTTPLog.md) | Log to send (JSON format).                                                           |
| **content_encoding** | **ContentEncoding**       | HTTP header used to compress the media-type.                                         | [optional] |
| **ddtags**           | **str**                   | Log tags can be passed as query parameters with &#x60;text/plain&#x60; content type. | [optional] |

### Return type

**dict**

### Authorization

[apiKeyAuth](README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/logplex-1, text/plain
- **Accept**: application/json

### HTTP response details

| Status code | Description                                              | Response headers |
| ----------- | -------------------------------------------------------- | ---------------- |
| **202**     | Request accepted for processing (always 202 empty JSON). | -                |
| **400**     | Bad Request                                              | -                |
| **401**     | Unauthorized                                             | -                |
| **403**     | Forbidden                                                | -                |
| **408**     | Request Timeout                                          | -                |
| **413**     | Payload Too Large                                        | -                |
| **429**     | Too Many Requests                                        | -                |
| **500**     | Internal Server Error                                    | -                |
| **503**     | Service Unavailable                                      | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
