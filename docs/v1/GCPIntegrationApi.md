# datadog_api_client.v1.GCPIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gcp_integration**](GCPIntegrationApi.md#create_gcp_integration) | **POST** /api/v1/integration/gcp | Create a GCP integration
[**delete_gcp_integration**](GCPIntegrationApi.md#delete_gcp_integration) | **DELETE** /api/v1/integration/gcp | Delete a GCP integration
[**list_gcp_integration**](GCPIntegrationApi.md#list_gcp_integration) | **GET** /api/v1/integration/gcp | List all GCP integrations
[**update_gcp_integration**](GCPIntegrationApi.md#update_gcp_integration) | **PUT** /api/v1/integration/gcp | Update a GCP integration


# **create_gcp_integration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_gcp_integration(body)

Create a GCP integration

Create a Datadog-GCP integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import gcp_integration_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import gcp_account
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
    api_instance = gcp_integration_api.GCPIntegrationApi(api_client)
    body = gcp_account.GCPAccount() # gcp_account.GCPAccount | Create a Datadog-Azure integration.
    
    # example passing only required values which don't have defaults set
    try:
        # Create a GCP integration
        api_response = api_instance.create_gcp_integration(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling GCPIntegrationApi->create_gcp_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**gcp_account.GCPAccount**](GCPAccount.md)| Create a Datadog-Azure integration. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_gcp_integration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_gcp_integration(body)

Delete a GCP integration

Delete a given Datadog-GCP integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import gcp_integration_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import gcp_account
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
    api_instance = gcp_integration_api.GCPIntegrationApi(api_client)
    body = gcp_account.GCPAccount() # gcp_account.GCPAccount | Delete a given Datadog-GCP integration.
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a GCP integration
        api_response = api_instance.delete_gcp_integration(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling GCPIntegrationApi->delete_gcp_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**gcp_account.GCPAccount**](GCPAccount.md)| Delete a given Datadog-GCP integration. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_gcp_integration**
> gcp_account_list_response.GCPAccountListResponse list_gcp_integration()

List all GCP integrations

List all Datadog-GCP integrations configured in your Datadog account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import gcp_integration_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import gcp_account_list_response
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
    api_instance = gcp_integration_api.GCPIntegrationApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # List all GCP integrations
        api_response = api_instance.list_gcp_integration()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling GCPIntegrationApi->list_gcp_integration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**gcp_account_list_response.GCPAccountListResponse**](GCPAccountListResponse.md)

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
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_gcp_integration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_gcp_integration(body)

Update a GCP integration

Update a Datadog-GCP integrations host_filters and/or auto-mute. Requires a `project_id` and `client_email`, however these fields cannot be updated. If you need to update these fields, delete and use the create (`POST`) endpoint. The unspecified fields will keep their original values.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import gcp_integration_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import gcp_account
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
    api_instance = gcp_integration_api.GCPIntegrationApi(api_client)
    body = gcp_account.GCPAccount() # gcp_account.GCPAccount | Update a Datadog-GCP integration.
    
    # example passing only required values which don't have defaults set
    try:
        # Update a GCP integration
        api_response = api_instance.update_gcp_integration(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling GCPIntegrationApi->update_gcp_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**gcp_account.GCPAccount**](GCPAccount.md)| Update a Datadog-GCP integration. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

