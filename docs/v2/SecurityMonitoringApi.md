# datadog_api_client.v2.SecurityMonitoringApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_monitoring_rule**](SecurityMonitoringApi.md#create_security_monitoring_rule) | **POST** /api/v2/security_monitoring/rules | Create a detection rule
[**delete_security_monitoring_rule**](SecurityMonitoringApi.md#delete_security_monitoring_rule) | **DELETE** /api/v2/security_monitoring/rules/{rule_id} | Delete an existing rule
[**get_security_monitoring_rule**](SecurityMonitoringApi.md#get_security_monitoring_rule) | **GET** /api/v2/security_monitoring/rules/{rule_id} | Get a rule&#39;s details
[**list_security_monitoring_rules**](SecurityMonitoringApi.md#list_security_monitoring_rules) | **GET** /api/v2/security_monitoring/rules | List rules
[**update_security_monitoring_rule**](SecurityMonitoringApi.md#update_security_monitoring_rule) | **PUT** /api/v2/security_monitoring/rules/{rule_id} | Update an existing rule


# **create_security_monitoring_rule**
> security_monitoring_rule_response.SecurityMonitoringRuleResponse create_security_monitoring_rule()

Create a detection rule

Create a detection rule.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.model import security_monitoring_rule_response
from datadog_api_client.v2.model import security_monitoring_rule_create_payload
from datadog_api_client.v2.model import api_error_response
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
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    body = security_monitoring_rule_create_payload.SecurityMonitoringRuleCreatePayload() # security_monitoring_rule_create_payload.SecurityMonitoringRuleCreatePayload |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a detection rule
        api_response = api_instance.create_security_monitoring_rule(body=body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->create_security_monitoring_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**security_monitoring_rule_create_payload.SecurityMonitoringRuleCreatePayload**](SecurityMonitoringRuleCreatePayload.md)|  | [optional]

### Return type

[**security_monitoring_rule_response.SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

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
**403** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_security_monitoring_rule**
> delete_security_monitoring_rule(rule_id)

Delete an existing rule

Delete an existing rule. Default rules cannot be deleted.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.model import api_error_response
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
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = 'rule_id_example' # str | The ID of the rule.
    
    # example passing only required values which don't have defaults set
    try:
        # Delete an existing rule
        api_instance.delete_security_monitoring_rule(rule_id)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->delete_security_monitoring_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The ID of the rule. |

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
**403** | Not Authorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_security_monitoring_rule**
> security_monitoring_rule_response.SecurityMonitoringRuleResponse get_security_monitoring_rule(rule_id)

Get a rule's details

Get a rule's details.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.model import security_monitoring_rule_response
from datadog_api_client.v2.model import api_error_response
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
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = 'rule_id_example' # str | The ID of the rule.
    
    # example passing only required values which don't have defaults set
    try:
        # Get a rule's details
        api_response = api_instance.get_security_monitoring_rule(rule_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->get_security_monitoring_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The ID of the rule. |

### Return type

[**security_monitoring_rule_response.SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_security_monitoring_rules**
> security_monitoring_list_rules_response.SecurityMonitoringListRulesResponse list_security_monitoring_rules()

List rules

List rules.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.model import api_error_response
from datadog_api_client.v2.model import security_monitoring_list_rules_response
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
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    page_size = 10 # int | Size for a given page. (optional) if omitted the server will use the default value of 10
page_number = 0 # int | Specific page number to return. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List rules
        api_response = api_instance.list_security_monitoring_rules(page_size=page_size, page_number=page_number)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->list_security_monitoring_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0

### Return type

[**security_monitoring_list_rules_response.SecurityMonitoringListRulesResponse**](SecurityMonitoringListRulesResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_security_monitoring_rule**
> security_monitoring_rule_response.SecurityMonitoringRuleResponse update_security_monitoring_rule(rule_id)

Update an existing rule

Update an existing rule. When updating `cases`, `queries` or `options`, the whole field must be included. For example, when modifying a query all queries must be included. Default rules can only be updated to be enabled and to change notifications.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.model import security_monitoring_rule_response
from datadog_api_client.v2.model import security_monitoring_rule_update_payload
from datadog_api_client.v2.model import api_error_response
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
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v2.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = 'rule_id_example' # str | The ID of the rule.
    body = security_monitoring_rule_update_payload.SecurityMonitoringRuleUpdatePayload() # security_monitoring_rule_update_payload.SecurityMonitoringRuleUpdatePayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an existing rule
        api_response = api_instance.update_security_monitoring_rule(rule_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->update_security_monitoring_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an existing rule
        api_response = api_instance.update_security_monitoring_rule(rule_id, body=body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->update_security_monitoring_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The ID of the rule. |
 **body** | [**security_monitoring_rule_update_payload.SecurityMonitoringRuleUpdatePayload**](SecurityMonitoringRuleUpdatePayload.md)|  | [optional]

### Return type

[**security_monitoring_rule_response.SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

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
**401** | Concurrent Modification |  -  |
**403** | Not Authorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

