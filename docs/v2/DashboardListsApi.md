# datadog_api_client.v2.DashboardListsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_list_items**](DashboardListsApi.md#create_dashboard_list_items) | **POST** /api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards | Add Items to a Dashboard List
[**delete_dashboard_list_items**](DashboardListsApi.md#delete_dashboard_list_items) | **DELETE** /api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards | Delete items from a dashboard list
[**get_dashboard_list_items**](DashboardListsApi.md#get_dashboard_list_items) | **GET** /api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards | Get a Dashboard List
[**update_dashboard_list_items**](DashboardListsApi.md#update_dashboard_list_items) | **PUT** /api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards | Update items of a dashboard list


# **create_dashboard_list_items**
> DashboardListAddItemsResponse create_dashboard_list_items(dashboard_list_id, body)

Add Items to a Dashboard List

Add dashboards to an existing dashboard list.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import dashboard_lists_api
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
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    dashboard_list_id = 1 # int | ID of the dashboard list to add items to.
    body = DashboardListAddItemsRequest(
        dashboards=[
            DashboardListItemRequest(
                id="q5j-nti-fv6",
                type=DashboardType("custom_timeboard"),
            ),
        ],
    ) # DashboardListAddItemsRequest | Dashboards to add to the dashboard list.

    # example passing only required values which don't have defaults set
    try:
        # Add Items to a Dashboard List
        api_response = api_instance.create_dashboard_list_items(dashboard_list_id, body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling DashboardListsApi->create_dashboard_list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_list_id** | **int**| ID of the dashboard list to add items to. |
 **body** | [**DashboardListAddItemsRequest**](DashboardListAddItemsRequest.md)| Dashboards to add to the dashboard list. |

### Return type

[**DashboardListAddItemsResponse**](DashboardListAddItemsResponse.md)

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

# **delete_dashboard_list_items**
> DashboardListDeleteItemsResponse delete_dashboard_list_items(dashboard_list_id, body)

Delete items from a dashboard list

Delete dashboards from an existing dashboard list.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import dashboard_lists_api
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
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    dashboard_list_id = 1 # int | ID of the dashboard list to delete items from.
    body = DashboardListDeleteItemsRequest(
        dashboards=[
            DashboardListItemRequest(
                id="q5j-nti-fv6",
                type=DashboardType("custom_timeboard"),
            ),
        ],
    ) # DashboardListDeleteItemsRequest | Dashboards to delete from the dashboard list.

    # example passing only required values which don't have defaults set
    try:
        # Delete items from a dashboard list
        api_response = api_instance.delete_dashboard_list_items(dashboard_list_id, body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling DashboardListsApi->delete_dashboard_list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_list_id** | **int**| ID of the dashboard list to delete items from. |
 **body** | [**DashboardListDeleteItemsRequest**](DashboardListDeleteItemsRequest.md)| Dashboards to delete from the dashboard list. |

### Return type

[**DashboardListDeleteItemsResponse**](DashboardListDeleteItemsResponse.md)

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

# **get_dashboard_list_items**
> DashboardListItems get_dashboard_list_items(dashboard_list_id)

Get a Dashboard List

Fetch the dashboard list’s dashboard definitions.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import dashboard_lists_api
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
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    dashboard_list_id = 1 # int | ID of the dashboard list to get items from.

    # example passing only required values which don't have defaults set
    try:
        # Get a Dashboard List
        api_response = api_instance.get_dashboard_list_items(dashboard_list_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling DashboardListsApi->get_dashboard_list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_list_id** | **int**| ID of the dashboard list to get items from. |

### Return type

[**DashboardListItems**](DashboardListItems.md)

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

# **update_dashboard_list_items**
> DashboardListUpdateItemsResponse update_dashboard_list_items(dashboard_list_id, body)

Update items of a dashboard list

Update dashboards of an existing dashboard list.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import dashboard_lists_api
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
    api_instance = dashboard_lists_api.DashboardListsApi(api_client)
    dashboard_list_id = 1 # int | ID of the dashboard list to update items from.
    body = DashboardListUpdateItemsRequest(
        dashboards=[
            DashboardListItemRequest(
                id="q5j-nti-fv6",
                type=DashboardType("custom_timeboard"),
            ),
        ],
    ) # DashboardListUpdateItemsRequest | New dashboards of the dashboard list.

    # example passing only required values which don't have defaults set
    try:
        # Update items of a dashboard list
        api_response = api_instance.update_dashboard_list_items(dashboard_list_id, body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling DashboardListsApi->update_dashboard_list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_list_id** | **int**| ID of the dashboard list to update items from. |
 **body** | [**DashboardListUpdateItemsRequest**](DashboardListUpdateItemsRequest.md)| New dashboards of the dashboard list. |

### Return type

[**DashboardListUpdateItemsResponse**](DashboardListUpdateItemsResponse.md)

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

