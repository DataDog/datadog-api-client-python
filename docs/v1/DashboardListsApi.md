# datadog_api_client.v1.DashboardListsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_list**](DashboardListsApi.md#create_dashboard_list) | **POST** /api/v1/dashboard/lists/manual | Create a dashboard list
[**delete_dashboard_list**](DashboardListsApi.md#delete_dashboard_list) | **DELETE** /api/v1/dashboard/lists/manual/{list_id} | Delete a dashboard list
[**get_dashboard_list**](DashboardListsApi.md#get_dashboard_list) | **GET** /api/v1/dashboard/lists/manual/{list_id} | Get a dashboard list
[**list_dashboard_lists**](DashboardListsApi.md#list_dashboard_lists) | **GET** /api/v1/dashboard/lists/manual | Get all dashboard lists
[**update_dashboard_list**](DashboardListsApi.md#update_dashboard_list) | **PUT** /api/v1/dashboard/lists/manual/{list_id} | Update a dashboard list


# **create_dashboard_list**
> DashboardList create_dashboard_list(body)

Create an empty dashboard list.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboard_lists_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    body = DashboardList(
        name="My Dashboard",
    )  # DashboardList | Create a dashboard list request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a dashboard list
        api_response = api_instance.create_dashboard_list(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->create_dashboard_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardList**](DashboardList.md)| Create a dashboard list request body. |

### Return type

[**DashboardList**](DashboardList.md)

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

# **delete_dashboard_list**
> DashboardListDeleteResponse delete_dashboard_list(list_id)

Delete a dashboard list.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboard_lists_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    list_id = 1  # int | ID of the dashboard list to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a dashboard list
        api_response = api_instance.delete_dashboard_list(list_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->delete_dashboard_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the dashboard list to delete. |

### Return type

[**DashboardListDeleteResponse**](DashboardListDeleteResponse.md)

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

# **get_dashboard_list**
> DashboardList get_dashboard_list(list_id)

Fetch an existing dashboard list's definition.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboard_lists_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    list_id = 1  # int | ID of the dashboard list to fetch.

    # example passing only required values which don't have defaults set
    try:
        # Get a dashboard list
        api_response = api_instance.get_dashboard_list(list_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->get_dashboard_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the dashboard list to fetch. |

### Return type

[**DashboardList**](DashboardList.md)

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

# **list_dashboard_lists**
> DashboardListListResponse list_dashboard_lists()

Fetch all of your existing dashboard list definitions.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboard_lists_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all dashboard lists
        api_response = api_instance.list_dashboard_lists()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->list_dashboard_lists: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardListListResponse**](DashboardListListResponse.md)

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

# **update_dashboard_list**
> DashboardList update_dashboard_list(list_id, body)

Update the name of a dashboard list.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboard_lists_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    list_id = 1  # int | ID of the dashboard list to update.
    body = DashboardList(
        name="My Dashboard",
    )  # DashboardList | Update a dashboard list request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a dashboard list
        api_response = api_instance.update_dashboard_list(list_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardListsApi->update_dashboard_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the dashboard list to update. |
 **body** | [**DashboardList**](DashboardList.md)| Update a dashboard list request body. |

### Return type

[**DashboardList**](DashboardList.md)

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

