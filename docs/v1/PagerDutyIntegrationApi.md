# datadog_api_client.v1.PagerDutyIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pager_duty_integration_service**](PagerDutyIntegrationApi.md#create_pager_duty_integration_service) | **POST** /api/v1/integration/pagerduty/configuration/services | Create a new service object
[**delete_pager_duty_integration_service**](PagerDutyIntegrationApi.md#delete_pager_duty_integration_service) | **DELETE** /api/v1/integration/pagerduty/configuration/services/{service_name} | Delete a single service object
[**get_pager_duty_integration_service**](PagerDutyIntegrationApi.md#get_pager_duty_integration_service) | **GET** /api/v1/integration/pagerduty/configuration/services/{service_name} | Get a single service object
[**update_pager_duty_integration_service**](PagerDutyIntegrationApi.md#update_pager_duty_integration_service) | **PUT** /api/v1/integration/pagerduty/configuration/services/{service_name} | Update a single service object


# **create_pager_duty_integration_service**
> PagerDutyServiceName create_pager_duty_integration_service(body)

Create a new service object

Create a new service object in the PagerDuty integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import pager_duty_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pager_duty_integration_api.PagerDutyIntegrationApi(api_client)
    body = PagerDutyService(
        service_key="",
        service_name="",
    )  # PagerDutyService | Create a new service object request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a new service object
        api_response = api_instance.create_pager_duty_integration_service(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PagerDutyIntegrationApi->create_pager_duty_integration_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PagerDutyService**](PagerDutyService.md)| Create a new service object request body. |

### Return type

[**PagerDutyServiceName**](PagerDutyServiceName.md)

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

# **delete_pager_duty_integration_service**
> delete_pager_duty_integration_service(service_name)

Delete a single service object

Delete a single service object in the Datadog-PagerDuty integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import pager_duty_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pager_duty_integration_api.PagerDutyIntegrationApi(api_client)
    service_name = "service_name_example"  # str | The service name

    # example passing only required values which don't have defaults set
    try:
        # Delete a single service object
        api_instance.delete_pager_duty_integration_service(service_name)
    except ApiException as e:
        print("Exception when calling PagerDutyIntegrationApi->delete_pager_duty_integration_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The service name |

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

# **get_pager_duty_integration_service**
> PagerDutyServiceName get_pager_duty_integration_service(service_name)

Get a single service object

Get service name in the Datadog-PagerDuty integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import pager_duty_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pager_duty_integration_api.PagerDutyIntegrationApi(api_client)
    service_name = "service_name_example"  # str | The service name.

    # example passing only required values which don't have defaults set
    try:
        # Get a single service object
        api_response = api_instance.get_pager_duty_integration_service(service_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PagerDutyIntegrationApi->get_pager_duty_integration_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The service name. |

### Return type

[**PagerDutyServiceName**](PagerDutyServiceName.md)

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

# **update_pager_duty_integration_service**
> update_pager_duty_integration_service(service_name, body)

Update a single service object

Update a single service object in the Datadog-PagerDuty integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import pager_duty_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pager_duty_integration_api.PagerDutyIntegrationApi(api_client)
    service_name = "service_name_example"  # str | The service name
    body = PagerDutyServiceKey(
        service_key="",
    )  # PagerDutyServiceKey | Update an existing service object request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a single service object
        api_instance.update_pager_duty_integration_service(service_name, body)
    except ApiException as e:
        print("Exception when calling PagerDutyIntegrationApi->update_pager_duty_integration_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The service name |
 **body** | [**PagerDutyServiceKey**](PagerDutyServiceKey.md)| Update an existing service object request body. |

### Return type

void (empty response body)

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

