# datadog_api_client.v1.SnapshotsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_graph_snapshot**](SnapshotsApi.md#get_graph_snapshot) | **GET** /api/v1/graph/snapshot | Take graph snapshots


# **get_graph_snapshot**
> GraphSnapshot get_graph_snapshot(start, end)

Take graph snapshots

Take graph snapshots. **Note**: When a snapshot is created, there is some delay before it is available.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import snapshots_api
from datadog_api_client.v1.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v1.Configuration(
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
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snapshots_api.SnapshotsApi(api_client)
    start = 1 # int | The POSIX timestamp of the start of the query.
    end = 1 # int | The POSIX timestamp of the end of the query.
    metric_query = "metric_query_example" # str | The metric query. (optional)
    event_query = "event_query_example" # str | A query that adds event bands to the graph. (optional)
    graph_def = "graph_def_example" # str | A JSON document defining the graph. `graph_def` can be used instead of `metric_query`. The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar) and should be formatted to a single line then URL encoded. (optional)
    title = "title_example" # str | A title for the graph. If no title is specified, the graph does not have a title. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Take graph snapshots
        api_response = api_instance.get_graph_snapshot(start, end)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SnapshotsApi->get_graph_snapshot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Take graph snapshots
        api_response = api_instance.get_graph_snapshot(start, end, metric_query=metric_query, event_query=event_query, graph_def=graph_def, title=title)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SnapshotsApi->get_graph_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| The POSIX timestamp of the start of the query. |
 **end** | **int**| The POSIX timestamp of the end of the query. |
 **metric_query** | **str**| The metric query. | [optional]
 **event_query** | **str**| A query that adds event bands to the graph. | [optional]
 **graph_def** | **str**| A JSON document defining the graph. &#x60;graph_def&#x60; can be used instead of &#x60;metric_query&#x60;. The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar) and should be formatted to a single line then URL encoded. | [optional]
 **title** | **str**| A title for the graph. If no title is specified, the graph does not have a title. | [optional]

### Return type

[**GraphSnapshot**](GraphSnapshot.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

