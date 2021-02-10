# datadog_api_client.v2.KeyManagementApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](KeyManagementApi.md#create_api_key) | **POST** /api/v2/api_keys | Create an API key
[**create_current_user_application_key**](KeyManagementApi.md#create_current_user_application_key) | **POST** /api/v2/current_user/application_keys | Create an application key for current user
[**delete_api_key**](KeyManagementApi.md#delete_api_key) | **DELETE** /api/v2/api_keys/{api_key_id} | Delete an API key
[**delete_application_key**](KeyManagementApi.md#delete_application_key) | **DELETE** /api/v2/application_keys/{app_key_id} | Delete an application key
[**delete_current_user_application_key**](KeyManagementApi.md#delete_current_user_application_key) | **DELETE** /api/v2/current_user/application_keys/{app_key_id} | Delete an application key owned by current user
[**get_api_key**](KeyManagementApi.md#get_api_key) | **GET** /api/v2/api_keys/{api_key_id} | Get API key
[**get_current_user_application_key**](KeyManagementApi.md#get_current_user_application_key) | **GET** /api/v2/current_user/application_keys/{app_key_id} | Get one application key owned by current user
[**list_api_keys**](KeyManagementApi.md#list_api_keys) | **GET** /api/v2/api_keys | Get all API keys
[**list_application_keys**](KeyManagementApi.md#list_application_keys) | **GET** /api/v2/application_keys | Get all application keys
[**list_current_user_application_keys**](KeyManagementApi.md#list_current_user_application_keys) | **GET** /api/v2/current_user/application_keys | Get all application keys owned by current user
[**update_api_key**](KeyManagementApi.md#update_api_key) | **PATCH** /api/v2/api_keys/{api_key_id} | Edit an API key
[**update_application_key**](KeyManagementApi.md#update_application_key) | **PATCH** /api/v2/application_keys/{app_key_id} | Edit an application key
[**update_current_user_application_key**](KeyManagementApi.md#update_current_user_application_key) | **PATCH** /api/v2/current_user/application_keys/{app_key_id} | Edit an application key owned by current user


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
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    body = APIKeyCreateRequest(
        data=APIKeyCreateData(
            attributes=APIKeyCreateAttributes(
                name="API Key for submitting metrics",
            ),
            type=APIKeysType("api_keys"),
        ),
    )  # APIKeyCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an API key
        api_response = api_instance.create_api_key(body)
        pprint(api_response)
    except ApiException as e:
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

# **create_current_user_application_key**
> ApplicationKeyResponse create_current_user_application_key(body)

Create an application key for current user

Create an application key for current user

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    body = ApplicationKeyCreateRequest(
        data=ApplicationKeyCreateData(
            attributes=ApplicationKeyCreateAttributes(
                name="Application Key for submitting metrics",
            ),
            type=ApplicationKeysType("application_keys"),
        ),
    )  # ApplicationKeyCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an application key for current user
        api_response = api_instance.create_current_user_application_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->create_current_user_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationKeyCreateRequest**](ApplicationKeyCreateRequest.md)|  |

### Return type

[**ApplicationKeyResponse**](ApplicationKeyResponse.md)

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
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example"  # str | The ID of the API key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an API key
        api_instance.delete_api_key(api_key_id)
    except ApiException as e:
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

# **delete_application_key**
> delete_application_key(app_key_id)

Delete an application key

Delete an application key

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    app_key_id = "app_key_id_example"  # str | The ID of the application key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an application key
        api_instance.delete_application_key(app_key_id)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->delete_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key_id** | **str**| The ID of the application key. |

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

# **delete_current_user_application_key**
> delete_current_user_application_key(app_key_id)

Delete an application key owned by current user

Delete an application key owned by current user

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    app_key_id = "app_key_id_example"  # str | The ID of the application key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an application key owned by current user
        api_instance.delete_current_user_application_key(app_key_id)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->delete_current_user_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key_id** | **str**| The ID of the application key. |

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
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example"  # str | The ID of the API key.
    include = "created_by,modified_by"  # str | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get API key
        api_response = api_instance.get_api_key(api_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->get_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get API key
        api_response = api_instance.get_api_key(api_key_id, include=include)
        pprint(api_response)
    except ApiException as e:
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

# **get_current_user_application_key**
> ApplicationKeyResponse get_current_user_application_key(app_key_id)

Get one application key owned by current user

Get an application key owned by current user

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    app_key_id = "app_key_id_example"  # str | The ID of the application key.

    # example passing only required values which don't have defaults set
    try:
        # Get one application key owned by current user
        api_response = api_instance.get_current_user_application_key(app_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->get_current_user_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key_id** | **str**| The ID of the application key. |

### Return type

[**ApplicationKeyResponse**](ApplicationKeyResponse.md)

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
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = APIKeysSort("name")  # APIKeysSort | API key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. (optional)
    filter = "filter_example"  # str | Filter API keys by the specified string. (optional)
    filter_created_at_start = "2020-11-24T18:46:21+00:00"  # str | Only include API keys created on or after the specified date. (optional)
    filter_created_at_end = "2020-11-24T18:46:21+00:00"  # str | Only include API keys created on or before the specified date. (optional)
    filter_modified_at_start = "2020-11-24T18:46:21+00:00"  # str | Only include API keys modified on or after the specified date. (optional)
    filter_modified_at_end = "2020-11-24T18:46:21+00:00"  # str | Only include API keys modified on or before the specified date. (optional)
    include = "created_by,modified_by"  # str | Comma separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `modified_by`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all API keys
        api_response = api_instance.list_api_keys(page_size=page_size, page_number=page_number, sort=sort, filter=filter, filter_created_at_start=filter_created_at_start, filter_created_at_end=filter_created_at_end, filter_modified_at_start=filter_modified_at_start, filter_modified_at_end=filter_modified_at_end, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->list_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **APIKeysSort**| API key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. | [optional]
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

# **list_application_keys**
> ListApplicationKeysResponse list_application_keys()

Get all application keys

List all application keys available for your org

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = ApplicationKeysSort("name")  # ApplicationKeysSort | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. (optional)
    filter = "filter_example"  # str | Filter application keys by the specified string. (optional)
    filter_created_at_start = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or after the specified date. (optional)
    filter_created_at_end = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or before the specified date. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all application keys
        api_response = api_instance.list_application_keys(page_size=page_size, page_number=page_number, sort=sort, filter=filter, filter_created_at_start=filter_created_at_start, filter_created_at_end=filter_created_at_end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->list_application_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **ApplicationKeysSort**| Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. | [optional]
 **filter** | **str**| Filter application keys by the specified string. | [optional]
 **filter_created_at_start** | **str**| Only include application keys created on or after the specified date. | [optional]
 **filter_created_at_end** | **str**| Only include application keys created on or before the specified date. | [optional]

### Return type

[**ListApplicationKeysResponse**](ListApplicationKeysResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_current_user_application_keys**
> ListApplicationKeysResponse list_current_user_application_keys()

Get all application keys owned by current user

List all application keys available for current user

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = ApplicationKeysSort("name")  # ApplicationKeysSort | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. (optional)
    filter = "filter_example"  # str | Filter application keys by the specified string. (optional)
    filter_created_at_start = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or after the specified date. (optional)
    filter_created_at_end = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or before the specified date. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all application keys owned by current user
        api_response = api_instance.list_current_user_application_keys(page_size=page_size, page_number=page_number, sort=sort, filter=filter, filter_created_at_start=filter_created_at_start, filter_created_at_end=filter_created_at_end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->list_current_user_application_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **ApplicationKeysSort**| Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. | [optional]
 **filter** | **str**| Filter application keys by the specified string. | [optional]
 **filter_created_at_start** | **str**| Only include application keys created on or after the specified date. | [optional]
 **filter_created_at_end** | **str**| Only include application keys created on or before the specified date. | [optional]

### Return type

[**ListApplicationKeysResponse**](ListApplicationKeysResponse.md)

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
**404** | Not Found |  -  |

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
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    api_key_id = "api_key_id_example"  # str | The ID of the API key.
    body = APIKeyUpdateRequest(
        data=APIKeyUpdateData(
            attributes=APIKeyUpdateAttributes(
                name="API Key for submitting metrics",
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=APIKeysType("api_keys"),
        ),
    )  # APIKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an API key
        api_response = api_instance.update_api_key(api_key_id, body)
        pprint(api_response)
    except ApiException as e:
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

# **update_application_key**
> ApplicationKeyResponse update_application_key(app_key_id, body)

Edit an application key

Edit an application key

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    app_key_id = "app_key_id_example"  # str | The ID of the application key.
    body = ApplicationKeyUpdateRequest(
        data=ApplicationKeyUpdateData(
            attributes=ApplicationKeyUpdateAttributes(
                name="Application Key for submitting metrics",
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=ApplicationKeysType("application_keys"),
        ),
    )  # ApplicationKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an application key
        api_response = api_instance.update_application_key(app_key_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->update_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key_id** | **str**| The ID of the application key. |
 **body** | [**ApplicationKeyUpdateRequest**](ApplicationKeyUpdateRequest.md)|  |

### Return type

[**ApplicationKeyResponse**](ApplicationKeyResponse.md)

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

# **update_current_user_application_key**
> ApplicationKeyResponse update_current_user_application_key(app_key_id, body)

Edit an application key owned by current user

Edit an application key owned by current user

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import key_management_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_api.KeyManagementApi(api_client)
    app_key_id = "app_key_id_example"  # str | The ID of the application key.
    body = ApplicationKeyUpdateRequest(
        data=ApplicationKeyUpdateData(
            attributes=ApplicationKeyUpdateAttributes(
                name="Application Key for submitting metrics",
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=ApplicationKeysType("application_keys"),
        ),
    )  # ApplicationKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an application key owned by current user
        api_response = api_instance.update_current_user_application_key(app_key_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KeyManagementApi->update_current_user_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key_id** | **str**| The ID of the application key. |
 **body** | [**ApplicationKeyUpdateRequest**](ApplicationKeyUpdateRequest.md)|  |

### Return type

[**ApplicationKeyResponse**](ApplicationKeyResponse.md)

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

