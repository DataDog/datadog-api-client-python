# datadog_api_client.v1.DashboardsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /api/v1/dashboard | Create a new dashboard
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /api/v1/dashboard/{dashboard_id} | Delete a dashboard
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /api/v1/dashboard/{dashboard_id} | Get a dashboard
[**list_dashboards**](DashboardsApi.md#list_dashboards) | **GET** /api/v1/dashboard | Get all dashboards
[**update_dashboard**](DashboardsApi.md#update_dashboard) | **PUT** /api/v1/dashboard/{dashboard_id} | Update a dashboard


# **create_dashboard**
> dashboard.Dashboard create_dashboard(body)

Create a new dashboard

Create a dashboard using the specified options.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import dashboard
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    body = dashboard.Dashboard() # dashboard.Dashboard | Create a dashboard request body.
    
    # example passing only required values which don't have defaults set
    try:
        # Create a new dashboard
        api_response = api_instance.create_dashboard(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dashboard.Dashboard**](Dashboard.md)| Create a dashboard request body. |

### Return type

[**dashboard.Dashboard**](Dashboard.md)

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_dashboard**
> dashboard_delete_response.DashboardDeleteResponse delete_dashboard(dashboard_id)

Delete a dashboard

Delete a dashboard using the specified ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import dashboard_delete_response
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = 'dashboard_id_example' # str | The ID of the dashboard.
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a dashboard
        api_response = api_instance.delete_dashboard(dashboard_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DashboardsApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The ID of the dashboard. |

### Return type

[**dashboard_delete_response.DashboardDeleteResponse**](DashboardDeleteResponse.md)

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
**404** | Dashboards Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_dashboard**
> dashboard.Dashboard get_dashboard(dashboard_id)

Get a dashboard

Get a dashboard using the specified ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import dashboard
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = 'dashboard_id_example' # str | The ID of the dashboard.
    
    # example passing only required values which don't have defaults set
    try:
        # Get a dashboard
        api_response = api_instance.get_dashboard(dashboard_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The ID of the dashboard. |

### Return type

[**dashboard.Dashboard**](Dashboard.md)

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

# **list_dashboards**
> dashboard_summary.DashboardSummary list_dashboards()

Get all dashboards

Get all dashboards.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import dashboard_summary
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get all dashboards
        api_response = api_instance.list_dashboards()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DashboardsApi->list_dashboards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dashboard_summary.DashboardSummary**](DashboardSummary.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_dashboard**
> dashboard.Dashboard update_dashboard(dashboard_id, body)

Update a dashboard

Update a dashboard using the specified ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import dashboard
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = 'dashboard_id_example' # str | The ID of the dashboard.
    body = dashboard.Dashboard() # dashboard.Dashboard | Update Dashboard request body.
    
    # example passing only required values which don't have defaults set
    try:
        # Update a dashboard
        api_response = api_instance.update_dashboard(dashboard_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling DashboardsApi->update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The ID of the dashboard. |
 **body** | [**dashboard.Dashboard**](Dashboard.md)| Update Dashboard request body. |

### Return type

[**dashboard.Dashboard**](Dashboard.md)

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
**403** | Authentication Error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

