# datadog_api_client.v1.WebhooksIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhooks_integration**](WebhooksIntegrationApi.md#create_webhooks_integration) | **POST** /api/v1/integration/webhooks/configuration/webhooks | Create a webhooks integration
[**create_webhooks_integration_custom_variable**](WebhooksIntegrationApi.md#create_webhooks_integration_custom_variable) | **POST** /api/v1/integration/webhooks/configuration/custom-variables | Create a custom variable
[**delete_webhooks_integration**](WebhooksIntegrationApi.md#delete_webhooks_integration) | **DELETE** /api/v1/integration/webhooks/configuration/webhooks/{webhook_name} | Delete a webhook
[**delete_webhooks_integration_custom_variable**](WebhooksIntegrationApi.md#delete_webhooks_integration_custom_variable) | **DELETE** /api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} | Delete a custom variable
[**get_webhooks_integration**](WebhooksIntegrationApi.md#get_webhooks_integration) | **GET** /api/v1/integration/webhooks/configuration/webhooks/{webhook_name} | Get a webhook integration
[**get_webhooks_integration_custom_variable**](WebhooksIntegrationApi.md#get_webhooks_integration_custom_variable) | **GET** /api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} | Get a custom variable
[**update_webhooks_integration**](WebhooksIntegrationApi.md#update_webhooks_integration) | **PUT** /api/v1/integration/webhooks/configuration/webhooks/{webhook_name} | Update a webhook
[**update_webhooks_integration_custom_variable**](WebhooksIntegrationApi.md#update_webhooks_integration_custom_variable) | **PUT** /api/v1/integration/webhooks/configuration/custom-variables/{custom_variable_name} | Update a custom variable


# **create_webhooks_integration**
> WebhooksIntegration create_webhooks_integration(body)

Creates an endpoint with the name `<WEBHOOK_NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    body = WebhooksIntegration(
        custom_headers="custom_headers_example",
        encode_as=WebhooksIntegrationEncoding("json"),
        name="WEBHOOK_NAME",
        payload="payload_example",
        url="https://example.com/webhook",
    )  # WebhooksIntegration | Create a webhooks integration request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a webhooks integration
        api_response = api_instance.create_webhooks_integration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->create_webhooks_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhooksIntegration**](WebhooksIntegration.md)| Create a webhooks integration request body. |

### Return type

[**WebhooksIntegration**](WebhooksIntegration.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_webhooks_integration_custom_variable**
> WebhooksIntegrationCustomVariableResponse create_webhooks_integration_custom_variable(body)

Creates an endpoint with the name `<CUSTOM_VARIABLE_NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    body = WebhooksIntegrationCustomVariable(
        is_secret=True,
        name="CUSTOM_VARIABLE_NAME",
        value="CUSTOM_VARIABLE_VALUE",
    )  # WebhooksIntegrationCustomVariable | Define a custom variable request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a custom variable
        api_response = api_instance.create_webhooks_integration_custom_variable(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->create_webhooks_integration_custom_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhooksIntegrationCustomVariable**](WebhooksIntegrationCustomVariable.md)| Define a custom variable request body. |

### Return type

[**WebhooksIntegrationCustomVariableResponse**](WebhooksIntegrationCustomVariableResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_webhooks_integration**
> delete_webhooks_integration(webhook_name)

Deletes the endpoint with the name `<WEBHOOK NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    webhook_name = "webhook_name_example"  # str | The name of the webhook.

    # example passing only required values which don't have defaults set
    try:
        # Delete a webhook
        api_instance.delete_webhooks_integration(webhook_name)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->delete_webhooks_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_name** | **str**| The name of the webhook. |

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
**200** | OK |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_webhooks_integration_custom_variable**
> delete_webhooks_integration_custom_variable(custom_variable_name)

Deletes the endpoint with the name `<CUSTOM_VARIABLE_NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    custom_variable_name = "custom_variable_name_example"  # str | The name of the custom variable.

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom variable
        api_instance.delete_webhooks_integration_custom_variable(custom_variable_name)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->delete_webhooks_integration_custom_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_variable_name** | **str**| The name of the custom variable. |

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
**200** | OK |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_webhooks_integration**
> WebhooksIntegration get_webhooks_integration(webhook_name)

Gets the content of the webhook with the name `<WEBHOOK_NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    webhook_name = "webhook_name_example"  # str | The name of the webhook.

    # example passing only required values which don't have defaults set
    try:
        # Get a webhook integration
        api_response = api_instance.get_webhooks_integration(webhook_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->get_webhooks_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_name** | **str**| The name of the webhook. |

### Return type

[**WebhooksIntegration**](WebhooksIntegration.md)

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
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_webhooks_integration_custom_variable**
> WebhooksIntegrationCustomVariableResponse get_webhooks_integration_custom_variable(custom_variable_name)

Shows the content of the custom variable with the name `<CUSTOM_VARIABLE_NAME>`.

If the custom variable is secret, the value does not return in the
response payload.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    custom_variable_name = "custom_variable_name_example"  # str | The name of the custom variable.

    # example passing only required values which don't have defaults set
    try:
        # Get a custom variable
        api_response = api_instance.get_webhooks_integration_custom_variable(custom_variable_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->get_webhooks_integration_custom_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_variable_name** | **str**| The name of the custom variable. |

### Return type

[**WebhooksIntegrationCustomVariableResponse**](WebhooksIntegrationCustomVariableResponse.md)

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
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_webhooks_integration**
> WebhooksIntegration update_webhooks_integration(webhook_name, body)

Updates the endpoint with the name `<WEBHOOK_NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    webhook_name = "webhook_name_example"  # str | The name of the webhook.
    body = WebhooksIntegrationUpdateRequest(
        custom_headers="custom_headers_example",
        encode_as=WebhooksIntegrationEncoding("json"),
        name="WEBHOOK_NAME",
        payload="payload_example",
        url="https://example.com/webhook",
    )  # WebhooksIntegrationUpdateRequest | Update an existing Datadog-Webhooks integration.

    # example passing only required values which don't have defaults set
    try:
        # Update a webhook
        api_response = api_instance.update_webhooks_integration(webhook_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->update_webhooks_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_name** | **str**| The name of the webhook. |
 **body** | [**WebhooksIntegrationUpdateRequest**](WebhooksIntegrationUpdateRequest.md)| Update an existing Datadog-Webhooks integration. |

### Return type

[**WebhooksIntegration**](WebhooksIntegration.md)

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
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_webhooks_integration_custom_variable**
> WebhooksIntegrationCustomVariableResponse update_webhooks_integration_custom_variable(custom_variable_name, body)

Updates the endpoint with the name `<CUSTOM_VARIABLE_NAME>`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    custom_variable_name = "custom_variable_name_example"  # str | The name of the custom variable.
    body = WebhooksIntegrationCustomVariableUpdateRequest(
        is_secret=True,
        name="CUSTOM_VARIABLE_NAME",
        value="CUSTOM_VARIABLE_VALUE",
    )  # WebhooksIntegrationCustomVariableUpdateRequest | Update an existing custom variable request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a custom variable
        api_response = api_instance.update_webhooks_integration_custom_variable(custom_variable_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->update_webhooks_integration_custom_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_variable_name** | **str**| The name of the custom variable. |
 **body** | [**WebhooksIntegrationCustomVariableUpdateRequest**](WebhooksIntegrationCustomVariableUpdateRequest.md)| Update an existing custom variable request body. |

### Return type

[**WebhooksIntegrationCustomVariableResponse**](WebhooksIntegrationCustomVariableResponse.md)

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
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

