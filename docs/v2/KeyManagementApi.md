# datadog_api_client.v2.KeyManagementApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](KeyManagementApi.md#create_api_key) | **POST** /api/v2/api_keys | Create an API key
[**delete_api_key**](KeyManagementApi.md#delete_api_key) | **DELETE** /api/v2/api_keys/{api_key_id} | Delete an API key
[**get_api_key**](KeyManagementApi.md#get_api_key) | **GET** /api/v2/api_keys/{api_key_id} | Get API key
[**list_api_keys**](KeyManagementApi.md#list_api_keys) | **GET** /api/v2/api_keys | Get all API keys
[**update_api_key**](KeyManagementApi.md#update_api_key) | **PATCH** /api/v2/api_keys/{api_key_id} | Edit an API key


# **create_api_key**
> APIKeyResponse create_api_key(body)

Create an API key

Create an API key.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import key_management_api
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    body = APIKeyCreateRequest(
        data=APIKeyCreateData(
            attributes=APIKeyCreateAttributes(
                name="API Key for submitting metrics",
            ),
            type=APIKeysType("api_keys"),
        ),
    ) # APIKeyCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an API key
        api_response = api_instance.create_api_key(body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling KeyManagementApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIKeyCreateRequest**](APIKeyCreateRequest.md)|  |

### Return type

[**APIKeyResponse**](APIKeyResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_api_key**
> delete_api_key(api_key_id)

Delete an API key

Delete an API key.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import key_management_api
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example" # str | The ID of the API key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an API key
        api_instance.delete_api_key(api_key_id)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling KeyManagementApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**| The ID of the API key. |

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
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_key**
> APIKeyResponse get_api_key(api_key_id)

Get API key

Get an API key.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import key_management_api
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example" # str | The ID of the API key.
    include = "created_by,modified_by" # str | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get API key
        api_response = api_instance.get_api_key(api_key_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling KeyManagementApi->get_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get API key
        api_response = api_instance.get_api_key(api_key_id, include=include)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling KeyManagementApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**| The ID of the API key. |
 **include** | **str**| Comma separated list of resource paths for related resources to include in the response. Supported resource paths are &#x60;created_by&#x60; and &#x60;modified_by&#x60;. | [optional]

### Return type

[**APIKeyResponse**](APIKeyResponse.md)

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

# **list_api_keys**
> APIKeysResponse list_api_keys()

Get all API keys

List all API keys available for your account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import key_management_api
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    page_size = 10 # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0 # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = "name" # str | API key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. (optional) if omitted the server will use the default value of "name"
    filter = "filter_example" # str | Filter API keys by the specified string. (optional)
    filter_created_at_start = "2020-11-24T18:46:21+00:00" # str | Only include API keys created on or after the specified date. (optional)
    filter_created_at_end = "2020-11-24T18:46:21+00:00" # str | Only include API keys created on or before the specified date. (optional)
    filter_modified_at_start = "2020-11-24T18:46:21+00:00" # str | Only include API keys modified on or after the specified date. (optional)
    filter_modified_at_end = "2020-11-24T18:46:21+00:00" # str | Only include API keys modified on or before the specified date. (optional)
    include = "created_by,modified_by" # str | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all API keys
        api_response = api_instance.list_api_keys(page_size=page_size, page_number=page_number, sort=sort, filter=filter, filter_created_at_start=filter_created_at_start, filter_created_at_end=filter_created_at_end, filter_modified_at_start=filter_modified_at_start, filter_modified_at_end=filter_modified_at_end, include=include)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling KeyManagementApi->list_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| API key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. | [optional] if omitted the server will use the default value of "name"
 **filter** | **str**| Filter API keys by the specified string. | [optional]
 **filter_created_at_start** | **str**| Only include API keys created on or after the specified date. | [optional]
 **filter_created_at_end** | **str**| Only include API keys created on or before the specified date. | [optional]
 **filter_modified_at_start** | **str**| Only include API keys modified on or after the specified date. | [optional]
 **filter_modified_at_end** | **str**| Only include API keys modified on or before the specified date. | [optional]
 **include** | **str**| Comma separated list of resource paths for related resources to include in the response. Supported resource paths are &#x60;created_by&#x60; and &#x60;modified_by&#x60;. | [optional]

### Return type

[**APIKeysResponse**](APIKeysResponse.md)

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

# **update_api_key**
> APIKeyResponse update_api_key(api_key_id, body)

Edit an API key

Update an API key.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import key_management_api
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example" # str | The ID of the API key.
    body = APIKeyUpdateRequest(
        data=APIKeyUpdateData(
            attributes=APIKeyUpdateAttributes(
                name="API Key for submitting metrics",
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=APIKeysType("api_keys"),
        ),
    ) # APIKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an API key
        api_response = api_instance.update_api_key(api_key_id, body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling KeyManagementApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**| The ID of the API key. |
 **body** | [**APIKeyUpdateRequest**](APIKeyUpdateRequest.md)|  |

### Return type

[**APIKeyResponse**](APIKeyResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

