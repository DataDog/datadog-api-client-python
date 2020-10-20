# datadog_api_client.v1.DowntimesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_downtime**](DowntimesApi.md#cancel_downtime) | **DELETE** /api/v1/downtime/{downtime_id} | Cancel a downtime
[**cancel_downtimes_by_scope**](DowntimesApi.md#cancel_downtimes_by_scope) | **POST** /api/v1/downtime/cancel/by_scope | Cancel downtimes by scope
[**create_downtime**](DowntimesApi.md#create_downtime) | **POST** /api/v1/downtime | Schedule a downtime
[**get_downtime**](DowntimesApi.md#get_downtime) | **GET** /api/v1/downtime/{downtime_id} | Get a downtime
[**list_downtimes**](DowntimesApi.md#list_downtimes) | **GET** /api/v1/downtime | Get all downtimes
[**update_downtime**](DowntimesApi.md#update_downtime) | **PUT** /api/v1/downtime/{downtime_id} | Update a downtime


# **cancel_downtime**
> cancel_downtime(downtime_id)

Cancel a downtime

Cancel a downtime.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import downtimes_api
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
    api_instance = downtimes_api.DowntimesApi(api_client)
    downtime_id = 123456 # int | ID of the downtime to cancel.

    # example passing only required values which don't have defaults set
    try:
        # Cancel a downtime
        api_instance.cancel_downtime(downtime_id)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DowntimesApi->cancel_downtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **downtime_id** | **int**| ID of the downtime to cancel. |

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Downtime not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **cancel_downtimes_by_scope**
> CanceledDowntimesIds cancel_downtimes_by_scope(body)

Cancel downtimes by scope

Delete all downtimes that match the scope of `X`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import downtimes_api
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
    api_instance = downtimes_api.DowntimesApi(api_client)
    body = CancelDowntimesByScopeRequest(
        scope="host:myserver",
    ) # CancelDowntimesByScopeRequest | Scope to cancel downtimes for.

    # example passing only required values which don't have defaults set
    try:
        # Cancel downtimes by scope
        api_response = api_instance.cancel_downtimes_by_scope(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DowntimesApi->cancel_downtimes_by_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelDowntimesByScopeRequest**](CancelDowntimesByScopeRequest.md)| Scope to cancel downtimes for. |

### Return type

[**CanceledDowntimesIds**](CanceledDowntimesIds.md)

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
**403** | Forbidden |  -  |
**404** | Downtimes not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_downtime**
> Downtime create_downtime(body)

Schedule a downtime

Schedule a downtime.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import downtimes_api
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
    api_instance = downtimes_api.DowntimesApi(api_client)
    body = Downtime(
        active=True,
        canceled=1412799983,
        creator_id=123456,
        disabled=False,
        downtime_type=2,
        end=1412793983,
        id=1625,
        message="Message on the downtime",
        monitor_id=123456,
        monitor_tags=[
            "["*"]",
        ],
        parent_id=123,
        recurrence=DowntimeRecurrence(
            period=1,
            rrule="FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
            type="weeks",
            until_date=1447786293,
            until_occurrences=2,
            week_days=[
                "["Mon","Tue"]",
            ],
        ),
        scope=[
            "["env:staging"]",
        ],
        start=1412792983,
        timezone="America/New_York",
        updater_id=123456,
    ) # Downtime | Schedule a downtime request body.

    # example passing only required values which don't have defaults set
    try:
        # Schedule a downtime
        api_response = api_instance.create_downtime(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DowntimesApi->create_downtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Downtime**](Downtime.md)| Schedule a downtime request body. |

### Return type

[**Downtime**](Downtime.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_downtime**
> Downtime get_downtime(downtime_id)

Get a downtime

Get downtime detail by `downtime_id`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import downtimes_api
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
    api_instance = downtimes_api.DowntimesApi(api_client)
    downtime_id = 123456 # int | ID of the downtime to fetch.

    # example passing only required values which don't have defaults set
    try:
        # Get a downtime
        api_response = api_instance.get_downtime(downtime_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DowntimesApi->get_downtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **downtime_id** | **int**| ID of the downtime to fetch. |

### Return type

[**Downtime**](Downtime.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Downtime not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_downtimes**
> [Downtime] list_downtimes()

Get all downtimes

Get all scheduled downtimes.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import downtimes_api
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
    api_instance = downtimes_api.DowntimesApi(api_client)
    current_only = True # bool | Only return downtimes that are active when the request is made. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all downtimes
        api_response = api_instance.list_downtimes(current_only=current_only)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DowntimesApi->list_downtimes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_only** | **bool**| Only return downtimes that are active when the request is made. | [optional]

### Return type

[**[Downtime]**](Downtime.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_downtime**
> Downtime update_downtime(downtime_id, body)

Update a downtime

Update a single downtime by `downtime_id`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import downtimes_api
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
    api_instance = downtimes_api.DowntimesApi(api_client)
    downtime_id = 123456 # int | ID of the downtime to update.
    body = Downtime(
        active=True,
        canceled=1412799983,
        creator_id=123456,
        disabled=False,
        downtime_type=2,
        end=1412793983,
        id=1625,
        message="Message on the downtime",
        monitor_id=123456,
        monitor_tags=[
            "["*"]",
        ],
        parent_id=123,
        recurrence=DowntimeRecurrence(
            period=1,
            rrule="FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
            type="weeks",
            until_date=1447786293,
            until_occurrences=2,
            week_days=[
                "["Mon","Tue"]",
            ],
        ),
        scope=[
            "["env:staging"]",
        ],
        start=1412792983,
        timezone="America/New_York",
        updater_id=123456,
    ) # Downtime | Update a downtime request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a downtime
        api_response = api_instance.update_downtime(downtime_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DowntimesApi->update_downtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **downtime_id** | **int**| ID of the downtime to update. |
 **body** | [**Downtime**](Downtime.md)| Update a downtime request body. |

### Return type

[**Downtime**](Downtime.md)

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
**403** | Forbidden |  -  |
**404** | Downtime not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

