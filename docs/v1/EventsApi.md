# datadog_api_client.v1.EventsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](EventsApi.md#create_event) | **POST** /api/v1/events | Post an event
[**get_event**](EventsApi.md#get_event) | **GET** /api/v1/events/{event_id} | Get an event
[**list_events**](EventsApi.md#list_events) | **GET** /api/v1/events | Query the event stream


# **create_event**
> EventCreateResponse create_event(body)

Post an event

This endpoint allows you to post events to the stream. Tag them, set priority and event aggregate them with other events.

### Example

* Api Key Authentication (apiKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import events_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    body = EventCreateRequest(
        aggregation_key="aggregation_key_example",
        alert_type=EventAlertType("info"),
        date_happened=1,
        device_name="device_name_example",
        host="host_example",
        id=1,
        payload="{}",
        priority=EventPriority("normal"),
        related_event_id=1,
        source_type_name="source_type_name_example",
        tags=["environment:test"],
        text="Oh boy!",
        title="Did you hear the news today?",
        url="url_example",
    )  # EventCreateRequest | Event request object

    # example passing only required values which don't have defaults set
    try:
        # Post an event
        api_response = api_instance.create_event(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->create_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventCreateRequest**](EventCreateRequest.md)| Event request object |

### Return type

[**EventCreateResponse**](EventCreateResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_event**
> EventResponse get_event(event_id)

Get an event

This endpoint allows you to query for event details.  **Note**: If the event you’re querying contains markdown formatting of any kind, you may see characters such as `%`,`\\`,`n` in your output.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import events_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_id = 1  # int | The ID of the event.

    # example passing only required values which don't have defaults set
    try:
        # Get an event
        api_response = api_instance.get_event(event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| The ID of the event. |

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication Error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_events**
> EventListResponse list_events(start, end)

Query the event stream

The event stream can be queried and filtered by time, priority, sources and tags.  **Notes**: - If the event you’re querying contains markdown formatting of any kind, you may see characters such as `%`,`\\`,`n` in your output.  - This endpoint returns a maximum of `1000` most recent results. To return additional results, identify the last timestamp of the last result and set that as the `end` query time to paginate the results.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import events_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    start = 1  # int | POSIX timestamp.
    end = 1  # int | POSIX timestamp.
    priority = EventPriority("normal")  # EventPriority | Priority of your events, either `low` or `normal`. (optional)
    sources = "sources_example"  # str | A comma separated string of sources. (optional)
    tags = "host:host0"  # str | A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. (optional)
    unaggregated = True  # bool | Set unaggregated to `true` to return all events within the specified [`start`,`end`] timeframe. Otherwise if an event is aggregated to a parent event with a timestamp outside of the timeframe, it won't be available in the output. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query the event stream
        api_response = api_instance.list_events(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query the event stream
        api_response = api_instance.list_events(start, end, priority=priority, sources=sources, tags=tags, unaggregated=unaggregated)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| POSIX timestamp. |
 **end** | **int**| POSIX timestamp. |
 **priority** | **EventPriority**| Priority of your events, either &#x60;low&#x60; or &#x60;normal&#x60;. | [optional]
 **sources** | **str**| A comma separated string of sources. | [optional]
 **tags** | **str**| A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. | [optional]
 **unaggregated** | **bool**| Set unaggregated to &#x60;true&#x60; to return all events within the specified [&#x60;start&#x60;,&#x60;end&#x60;] timeframe. Otherwise if an event is aggregated to a parent event with a timestamp outside of the timeframe, it won&#39;t be available in the output. | [optional]

### Return type

[**EventListResponse**](EventListResponse.md)

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

