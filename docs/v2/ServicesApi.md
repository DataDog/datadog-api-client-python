# datadog_api_client.v2.ServicesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServicesApi.md#create_service) | **POST** /api/v2/services | Create a new service
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /api/v2/services/{service_id} | Delete an existing service
[**get_service**](ServicesApi.md#get_service) | **GET** /api/v2/services/{service_id} | Get details of a service
[**get_services**](ServicesApi.md#get_services) | **GET** /api/v2/services | Get a list of all services
[**update_service**](ServicesApi.md#update_service) | **PATCH** /api/v2/services/{service_id} | Update an existing service


# **create_service**
> ServiceResponse create_service(body)

Create a new service

Creates a new service.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    body = ServiceCreateRequest(
        data=ServiceCreateData(
            attributes=ServiceCreateAttributes(
                name="an example service name",
            ),
            relationships=ServiceRelationships(
                created_by=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                last_modified_by=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
            ),
            type=ServiceType("services"),
        ),
    ) # ServiceCreateRequest | Service Payload.

    # example passing only required values which don't have defaults set
    try:
        # Create a new service
        api_response = api_instance.create_service(body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling ServicesApi->create_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceCreateRequest**](ServiceCreateRequest.md)| Service Payload. |

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_service**
> delete_service(service_id)

Delete an existing service

Deletes an existing service.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    service_id = "service_id_example" # str | The ID of the service.

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing service
        api_instance.delete_service(service_id)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The ID of the service. |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_service**
> ServiceResponse get_service(service_id)

Get details of a service

Get details of a service. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these services

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    service_id = "service_id_example" # str | The ID of the service.
    include = "users" # str | Specifies which types of related objects should be included in the response. (optional) if omitted the server will use the default value of "users"

    # example passing only required values which don't have defaults set
    try:
        # Get details of a service
        api_response = api_instance.get_service(service_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of a service
        api_response = api_instance.get_service(service_id, include=include)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The ID of the service. |
 **include** | **str**| Specifies which types of related objects should be included in the response. | [optional] if omitted the server will use the default value of "users"

### Return type

[**ServiceResponse**](ServiceResponse.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_services**
> ServicesResponse get_services()

Get a list of all services

Get all services for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these services.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    include = "users" # str | Specifies which types of related objects should be included in the response. (optional) if omitted the server will use the default value of "users"
    page_size = 10 # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_offset = 0 # int | Specific offset to use as the beginning of the returned page. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all services
        api_response = api_instance.get_services(include=include, page_size=page_size, page_offset=page_offset)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling ServicesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Specifies which types of related objects should be included in the response. | [optional] if omitted the server will use the default value of "users"
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_offset** | **int**| Specific offset to use as the beginning of the returned page. | [optional] if omitted the server will use the default value of 0

### Return type

[**ServicesResponse**](ServicesResponse.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_service**
> ServiceResponse update_service(service_id, body)

Update an existing service

Updates an existing service. Only provide the attributes which should be updated as this request is a partial update.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    service_id = "service_id_example" # str | The ID of the service.
    body = ServiceUpdateRequest(
        data=ServiceUpdateData(
            attributes=ServiceUpdateAttributes(
                name="an example service name",
            ),
            id="00000000-0000-0000-0000-000000000000",
            relationships=ServiceRelationships(
                created_by=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                last_modified_by=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
            ),
            type=ServiceType("services"),
        ),
    ) # ServiceUpdateRequest | Service Payload.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing service
        api_response = api_instance.update_service(service_id, body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The ID of the service. |
 **body** | [**ServiceUpdateRequest**](ServiceUpdateRequest.md)| Service Payload. |

### Return type

[**ServiceResponse**](ServiceResponse.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

