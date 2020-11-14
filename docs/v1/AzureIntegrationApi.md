# datadog_api_client.v1.AzureIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_integration**](AzureIntegrationApi.md#create_azure_integration) | **POST** /api/v1/integration/azure | Create an Azure integration
[**delete_azure_integration**](AzureIntegrationApi.md#delete_azure_integration) | **DELETE** /api/v1/integration/azure | Delete an Azure integration
[**list_azure_integration**](AzureIntegrationApi.md#list_azure_integration) | **GET** /api/v1/integration/azure | List all Azure integrations
[**update_azure_host_filters**](AzureIntegrationApi.md#update_azure_host_filters) | **POST** /api/v1/integration/azure/host_filters | Update Azure integration host filters
[**update_azure_integration**](AzureIntegrationApi.md#update_azure_integration) | **PUT** /api/v1/integration/azure | Update an Azure integration


# **create_azure_integration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_azure_integration(body)

Create an Azure integration

Create a Datadog-Azure integration.  Using the `POST` method updates your integration configuration by adding your new configuration to the existing one in your Datadog organization.  Using the `PUT` method updates your integration configuration by replacing your current configuration with the new one sent to your Datadog organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import azure_integration_api
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
    api_instance = azure_integration_api.AzureIntegrationApi(api_client)
    body = AzureAccount(
        client_id="testc7f6-1234-5678-9101-3fcbf464test",
        client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
        errors=[
            "["*"]",
        ],
        host_filters="key:value,filter:example",
        new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
        new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
        tenant_name="testc44-1234-5678-9101-cc00736ftest",
    ) # AzureAccount | Create a Datadog-Azure integration for your Datadog account request body.

    # example passing only required values which don't have defaults set
    try:
        # Create an Azure integration
        api_response = api_instance.create_azure_integration(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AzureIntegrationApi->create_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| Create a Datadog-Azure integration for your Datadog account request body. |

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_azure_integration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_azure_integration(body)

Delete an Azure integration

Delete a given Datadog-Azure integration from your Datadog account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import azure_integration_api
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
    api_instance = azure_integration_api.AzureIntegrationApi(api_client)
    body = AzureAccount(
        client_id="testc7f6-1234-5678-9101-3fcbf464test",
        client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
        errors=[
            "["*"]",
        ],
        host_filters="key:value,filter:example",
        new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
        new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
        tenant_name="testc44-1234-5678-9101-cc00736ftest",
    ) # AzureAccount | Delete a given Datadog-Azure integration request body.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Azure integration
        api_response = api_instance.delete_azure_integration(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AzureIntegrationApi->delete_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| Delete a given Datadog-Azure integration request body. |

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_azure_integration**
> AzureAccountListResponse list_azure_integration()

List all Azure integrations

List all Datadog-Azure integrations configured in your Datadog account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import azure_integration_api
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
    api_instance = azure_integration_api.AzureIntegrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all Azure integrations
        api_response = api_instance.list_azure_integration()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AzureIntegrationApi->list_azure_integration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AzureAccountListResponse**](AzureAccountListResponse.md)

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_azure_host_filters**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_azure_host_filters(body)

Update Azure integration host filters

Update the defined list of host filters for a given Datadog-Azure integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import azure_integration_api
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
    api_instance = azure_integration_api.AzureIntegrationApi(api_client)
    body = AzureAccount(
        client_id="testc7f6-1234-5678-9101-3fcbf464test",
        client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
        errors=[
            "["*"]",
        ],
        host_filters="key:value,filter:example",
        new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
        new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
        tenant_name="testc44-1234-5678-9101-cc00736ftest",
    ) # AzureAccount | Update a Datadog-Azure integration's host filters request body.

    # example passing only required values which don't have defaults set
    try:
        # Update Azure integration host filters
        api_response = api_instance.update_azure_host_filters(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AzureIntegrationApi->update_azure_host_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| Update a Datadog-Azure integration&#39;s host filters request body. |

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_azure_integration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_azure_integration(body)

Update an Azure integration

Update a Datadog-Azure integration. Requires an existing `tenant_name` and `client_id`. Any other fields supplied will overwrite existing values. To overwrite `tenant_name` or `client_id`, use `new_tenant_name` and `new_client_id`. To leave a field unchanged, do not supply that field in the payload.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import azure_integration_api
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
    api_instance = azure_integration_api.AzureIntegrationApi(api_client)
    body = AzureAccount(
        client_id="testc7f6-1234-5678-9101-3fcbf464test",
        client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
        errors=[
            "["*"]",
        ],
        host_filters="key:value,filter:example",
        new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
        new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
        tenant_name="testc44-1234-5678-9101-cc00736ftest",
    ) # AzureAccount | Update a Datadog-Azure integration request body.

    # example passing only required values which don't have defaults set
    try:
        # Update an Azure integration
        api_response = api_instance.update_azure_integration(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AzureIntegrationApi->update_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| Update a Datadog-Azure integration request body. |

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

