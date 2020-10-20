# datadog_api_client.v2.LogsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_logs**](LogsApi.md#aggregate_logs) | **POST** /api/v2/logs/analytics/aggregate | Aggregate events
[**list_logs**](LogsApi.md#list_logs) | **POST** /api/v2/logs/events/search | Get a list of logs
[**list_logs_get**](LogsApi.md#list_logs_get) | **GET** /api/v2/logs/events | Get a quick list of logs


# **aggregate_logs**
> LogsAggregateResponse aggregate_logs()

Aggregate events

The API endpoint to aggregate events into buckets and compute metrics and timeseries.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
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
            indexes=[
                "["main","web"]",
            ],
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
        paging=LogsAggregateRequestPaging(
            after="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
        ),
    ) # LogsAggregateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Aggregate events
        api_response = api_instance.aggregate_logs(body=body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsApi->aggregate_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsAggregateRequest**](LogsAggregateRequest.md)|  | [optional]

### Return type

[**LogsAggregateResponse**](LogsAggregateResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs**
> LogsListResponse list_logs()

Get a list of logs

List endpoint returns logs that match a log search query. [Results are paginated][1].  Both this endpoint and the GET endpoint can be used interchangeably when listing logs.  **If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation][2].**  [1]: /logs/guide/collect-multiple-logs-with-pagination [2]: https://docs.datadoghq.com/logs/archives

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    body = LogsListRequest(
        filter=LogsQueryFilter(
            _from="now-15m",
            indexes=[
                "["main","web"]",
            ],
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
    ) # LogsListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of logs
        api_response = api_instance.list_logs(body=body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsListRequest**](LogsListRequest.md)|  | [optional]

### Return type

[**LogsListResponse**](LogsListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs_get**
> LogsListResponse list_logs_get()

Get a quick list of logs

List endpoint returns logs that match a log search query. [Results are paginated][1].  Both this endpoint and the POST endpoint can be used interchangeably when listing logs.  **If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation][2].**  [1]: /logs/guide/collect-multiple-logs-with-pagination [2]: https://docs.datadoghq.com/logs/archives

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    filter_query = "@datacenter:us @role:db" # str | Search query following logs syntax. (optional)
    filter_index = "main" # str | For customers with multiple indexes, the indexes to search Defaults to '*' which means all indexes (optional)
    filter_from = dateutil_parser('2019-01-02T09:42:36.320Z') # datetime | Minimum timestamp for requested logs. (optional)
    filter_to = dateutil_parser('2019-01-03T09:42:36.320Z') # datetime | Maximum timestamp for requested logs. (optional)
    sort = LogsSort("timestamp") # LogsSort | Order of logs in results. (optional)
    page_cursor = "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==" # str | List following results with a cursor provided in the previous query. (optional)
    page_limit = 25 # int | Maximum number of logs in the response. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a quick list of logs
        api_response = api_instance.list_logs_get(filter_query=filter_query, filter_index=filter_index, filter_from=filter_from, filter_to=filter_to, sort=sort, page_cursor=page_cursor, page_limit=page_limit)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsApi->list_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_query** | **str**| Search query following logs syntax. | [optional]
 **filter_index** | **str**| For customers with multiple indexes, the indexes to search Defaults to &#39;*&#39; which means all indexes | [optional]
 **filter_from** | **datetime**| Minimum timestamp for requested logs. | [optional]
 **filter_to** | **datetime**| Maximum timestamp for requested logs. | [optional]
 **sort** | **LogsSort**| Order of logs in results. | [optional]
 **page_cursor** | **str**| List following results with a cursor provided in the previous query. | [optional]
 **page_limit** | **int**| Maximum number of logs in the response. | [optional] if omitted the server will use the default value of 10

### Return type

[**LogsListResponse**](LogsListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

