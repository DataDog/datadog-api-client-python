# datadog_api_client.v2.IncidentServicesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_incident_service**](IncidentServicesApi.md#create_incident_service) | **POST** /api/v2/services | Create a new incident service
[**delete_incident_service**](IncidentServicesApi.md#delete_incident_service) | **DELETE** /api/v2/services/{service_id} | Delete an existing incident service
[**get_incident_service**](IncidentServicesApi.md#get_incident_service) | **GET** /api/v2/services/{service_id} | Get details of an incident service
[**list_incident_services**](IncidentServicesApi.md#list_incident_services) | **GET** /api/v2/services | Get a list of all incident services
[**update_incident_service**](IncidentServicesApi.md#update_incident_service) | **PATCH** /api/v2/services/{service_id} | Update an existing incident service


# **create_incident_service**
> IncidentServiceResponse create_incident_service(body)

Create a new incident service

Creates a new incident service.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["create_incident_service"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    body = IncidentServiceCreateRequest(
        data=IncidentServiceCreateData(
            attributes=IncidentServiceCreateAttributes(
                name="an example service name",
            ),
            relationships=IncidentServiceRelationships(
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
            type=IncidentServiceType("services"),
        ),
    )  # IncidentServiceCreateRequest | Incident Service Payload.

    # example passing only required values which don't have defaults set
    try:
        # Create a new incident service
        api_response = api_instance.create_incident_service(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->create_incident_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncidentServiceCreateRequest**](IncidentServiceCreateRequest.md)| Incident Service Payload. |

### Return type

[**IncidentServiceResponse**](IncidentServiceResponse.md)

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

# **delete_incident_service**
> delete_incident_service(service_id)

Delete an existing incident service

Deletes an existing incident service.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["delete_incident_service"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    service_id = "service_id_example"  # str | The ID of the incident service.

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing incident service
        api_instance.delete_incident_service(service_id)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->delete_incident_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The ID of the incident service. |

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

# **get_incident_service**
> IncidentServiceResponse get_incident_service(service_id)

Get details of an incident service

Get details of an incident service. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_incident_service"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    service_id = "service_id_example"  # str | The ID of the incident service.
    include = IncidentRelatedObject("users")  # IncidentRelatedObject | Specifies which types of related objects should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of an incident service
        api_response = api_instance.get_incident_service(service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->get_incident_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of an incident service
        api_response = api_instance.get_incident_service(service_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->get_incident_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The ID of the incident service. |
 **include** | **IncidentRelatedObject**| Specifies which types of related objects should be included in the response. | [optional]

### Return type

[**IncidentServiceResponse**](IncidentServiceResponse.md)

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

# **list_incident_services**
> IncidentServicesResponse list_incident_services()

Get a list of all incident services

Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_incident_services"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    include = IncidentRelatedObject("users")  # IncidentRelatedObject | Specifies which types of related objects should be included in the response. (optional)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_offset = 0  # int | Specific offset to use as the beginning of the returned page. (optional) if omitted the server will use the default value of 0
    filter = "ExampleServiceName"  # str | A search query that filters services by name. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all incident services
        api_response = api_instance.list_incident_services(include=include, page_size=page_size, page_offset=page_offset, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->list_incident_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **IncidentRelatedObject**| Specifies which types of related objects should be included in the response. | [optional]
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_offset** | **int**| Specific offset to use as the beginning of the returned page. | [optional] if omitted the server will use the default value of 0
 **filter** | **str**| A search query that filters services by name. | [optional]

### Return type

[**IncidentServicesResponse**](IncidentServicesResponse.md)

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

# **update_incident_service**
> IncidentServiceResponse update_incident_service(service_id, body)

Update an existing incident service

Updates an existing incident service. Only provide the attributes which should be updated as this request is a partial update.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["update_incident_service"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    service_id = "service_id_example"  # str | The ID of the incident service.
    body = IncidentServiceUpdateRequest(
        data=IncidentServiceUpdateData(
            attributes=IncidentServiceUpdateAttributes(
                name="an example service name",
            ),
            id="00000000-0000-0000-0000-000000000000",
            relationships=IncidentServiceRelationships(
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
            type=IncidentServiceType("services"),
        ),
    )  # IncidentServiceUpdateRequest | Incident Service Payload.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing incident service
        api_response = api_instance.update_incident_service(service_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->update_incident_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The ID of the incident service. |
 **body** | [**IncidentServiceUpdateRequest**](IncidentServiceUpdateRequest.md)| Incident Service Payload. |

### Return type

[**IncidentServiceResponse**](IncidentServiceResponse.md)

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

