# datadog_api_client.v1.LogsIndexesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logs_index**](LogsIndexesApi.md#get_logs_index) | **GET** /api/v1/logs/config/indexes/{name} | Get an index
[**get_logs_index_order**](LogsIndexesApi.md#get_logs_index_order) | **GET** /api/v1/logs/config/index-order | Get indexes order
[**list_log_indexes**](LogsIndexesApi.md#list_log_indexes) | **GET** /api/v1/logs/config/indexes | Get all indexes
[**update_logs_index**](LogsIndexesApi.md#update_logs_index) | **PUT** /api/v1/logs/config/indexes/{name} | Update an index
[**update_logs_index_order**](LogsIndexesApi.md#update_logs_index_order) | **PUT** /api/v1/logs/config/index-order | Update indexes order


# **get_logs_index**
> LogsIndex get_logs_index(name)

Get an index

Get one log index from your organization. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_indexes_api
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
    api_instance = logs_indexes_api.LogsIndexesApi(api_client)
    name = "name_example" # str | Name of the log index.

    # example passing only required values which don't have defaults set
    try:
        # Get an index
        api_response = api_instance.get_logs_index(name)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsIndexesApi->get_logs_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the log index. |

### Return type

[**LogsIndex**](LogsIndex.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_logs_index_order**
> LogsIndexesOrder get_logs_index_order()

Get indexes order

Get the current order of your log indexes. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_indexes_api
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
    api_instance = logs_indexes_api.LogsIndexesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get indexes order
        api_response = api_instance.get_logs_index_order()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsIndexesApi->get_logs_index_order: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsIndexesOrder**](LogsIndexesOrder.md)

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

# **list_log_indexes**
> LogsIndexListResponse list_log_indexes()

Get all indexes

The Index object describes the configuration of a log index. This endpoint returns an array of the `LogIndex` objects of your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_indexes_api
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
    api_instance = logs_indexes_api.LogsIndexesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all indexes
        api_response = api_instance.list_log_indexes()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsIndexesApi->list_log_indexes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsIndexListResponse**](LogsIndexListResponse.md)

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

# **update_logs_index**
> LogsIndex update_logs_index(name)

Update an index

Update an index as identified by its name. Returns the Index object passed in the request body when the request is successful.  Using the `PUT` method updates your index’s configuration by **replacing** your current configuration with the new one sent to your Datadog organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_indexes_api
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
    api_instance = logs_indexes_api.LogsIndexesApi(api_client)
    name = "name_example" # str | Name of the log index.
    body = LogsIndex(
        daily_limit=1,
        exclusion_filters=[
            LogsExclusion(
                filter=LogsExclusionFilter(
                    query="*",
                    sample_rate=1,
                ),
                is_enabled=True,
                name="payment",
            ),
        ],
        filter=LogsFilter(
            query="source:python",
        ),
        is_rate_limited=True,
        name="name_example",
        num_retention_days=1,
    ) # LogsIndex | Object containing the new `LogsIndex`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an index
        api_response = api_instance.update_logs_index(name)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsIndexesApi->update_logs_index: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an index
        api_response = api_instance.update_logs_index(name, body=body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsIndexesApi->update_logs_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the log index. |
 **body** | [**LogsIndex**](LogsIndex.md)| Object containing the new &#x60;LogsIndex&#x60;. | [optional]

### Return type

[**LogsIndex**](LogsIndex.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid Parameter Error |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_logs_index_order**
> LogsIndexesOrder update_logs_index_order()

Update indexes order

This endpoint updates the index order of your organization. It returns the index order object passed in the request body when the request is successful.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_indexes_api
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
    api_instance = logs_indexes_api.LogsIndexesApi(api_client)
    body = LogsIndexesOrder(
        index_names=[
            "["main","payments","web"]",
        ],
    ) # LogsIndexesOrder | Object containing the new ordered list of index names (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update indexes order
        api_response = api_instance.update_logs_index_order(body=body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsIndexesApi->update_logs_index_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsIndexesOrder**](LogsIndexesOrder.md)| Object containing the new ordered list of index names | [optional]

### Return type

[**LogsIndexesOrder**](LogsIndexesOrder.md)

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

