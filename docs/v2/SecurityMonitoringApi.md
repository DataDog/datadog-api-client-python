# datadog_api_client.v2.SecurityMonitoringApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_monitoring_rule**](SecurityMonitoringApi.md#create_security_monitoring_rule) | **POST** /api/v2/security_monitoring/rules | Create a detection rule
[**delete_security_monitoring_rule**](SecurityMonitoringApi.md#delete_security_monitoring_rule) | **DELETE** /api/v2/security_monitoring/rules/{rule_id} | Delete an existing rule
[**get_security_monitoring_rule**](SecurityMonitoringApi.md#get_security_monitoring_rule) | **GET** /api/v2/security_monitoring/rules/{rule_id} | Get a rule&#39;s details
[**list_security_monitoring_rules**](SecurityMonitoringApi.md#list_security_monitoring_rules) | **GET** /api/v2/security_monitoring/rules | List rules
[**list_security_monitoring_signals**](SecurityMonitoringApi.md#list_security_monitoring_signals) | **GET** /api/v2/security_monitoring/signals | Get a quick list of security signals
[**search_security_monitoring_signals**](SecurityMonitoringApi.md#search_security_monitoring_signals) | **POST** /api/v2/security_monitoring/signals/search | Get a list of security signals
[**update_security_monitoring_rule**](SecurityMonitoringApi.md#update_security_monitoring_rule) | **PUT** /api/v2/security_monitoring/rules/{rule_id} | Update an existing rule


# **create_security_monitoring_rule**
> SecurityMonitoringRuleResponse create_security_monitoring_rule()

Create a detection rule

Create a detection rule.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    body = SecurityMonitoringRuleCreatePayload(
        cases=[
            SecurityMonitoringRuleCaseCreate(
                condition="condition_example",
                name="name_example",
                notifications=[
                    "notifications_example",
                ],
                status=SecurityMonitoringRuleSeverity("info"),
            ),
        ],
        is_enabled=True,
        message="message_example",
        name="name_example",
        options=SecurityMonitoringRuleOptions(
            evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
            keep_alive=SecurityMonitoringRuleKeepAlive(0),
            max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(0),
        ),
        queries=[
            SecurityMonitoringRuleQueryCreate(
                aggregation=SecurityMonitoringRuleQueryAggregation("count"),
                distinct_fields=[
                    "distinct_fields_example",
                ],
                group_by_fields=[
                    "group_by_fields_example",
                ],
                metric="metric_example",
                name="name_example",
                query="a < 3",
            ),
        ],
        tags=[
            "["env:prod","team:security"]",
        ],
    ) # SecurityMonitoringRuleCreatePayload |  (optional)

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
 **body** | [**SecurityMonitoringRuleCreatePayload**](SecurityMonitoringRuleCreatePayload.md)|  | [optional]

### Return type

[**SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

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
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = "rule_id_example" # str | The ID of the rule.

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
> SecurityMonitoringRuleResponse get_security_monitoring_rule(rule_id)

Get a rule's details

Get a rule's details.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = "rule_id_example" # str | The ID of the rule.

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

[**SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

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
> SecurityMonitoringListRulesResponse list_security_monitoring_rules()

List rules

List rules.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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

[**SecurityMonitoringListRulesResponse**](SecurityMonitoringListRulesResponse.md)

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

# **list_security_monitoring_signals**
> SecurityMonitoringSignalsListResponse list_security_monitoring_signals()

Get a quick list of security signals

The list endpoint returns security signals that match a search query. Both this endpoint and the POST endpoint can be used interchangeably when listing security signals.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    filter_query = "security:attack status:high" # str | The search query for security signals. (optional)
    filter_from = dateutil_parser('2019-01-02T09:42:36.320Z') # datetime | The minimum timestamp for requested security signals. (optional)
    filter_to = dateutil_parser('2019-01-03T09:42:36.320Z') # datetime | The maximum timestamp for requested security signals. (optional)
    sort = SecurityMonitoringSignalsSort("timestamp") # SecurityMonitoringSignalsSort | The order of the security signals in results. (optional)
    page_cursor = "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==" # str | A list of results using the cursor provided in the previous query. (optional)
    page_limit = 25 # int | The maximum number of security signals in the response. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a quick list of security signals
        api_response = api_instance.list_security_monitoring_signals(filter_query=filter_query, filter_from=filter_from, filter_to=filter_to, sort=sort, page_cursor=page_cursor, page_limit=page_limit)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->list_security_monitoring_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_query** | **str**| The search query for security signals. | [optional]
 **filter_from** | **datetime**| The minimum timestamp for requested security signals. | [optional]
 **filter_to** | **datetime**| The maximum timestamp for requested security signals. | [optional]
 **sort** | **SecurityMonitoringSignalsSort**| The order of the security signals in results. | [optional]
 **page_cursor** | **str**| A list of results using the cursor provided in the previous query. | [optional]
 **page_limit** | **int**| The maximum number of security signals in the response. | [optional] if omitted the server will use the default value of 10

### Return type

[**SecurityMonitoringSignalsListResponse**](SecurityMonitoringSignalsListResponse.md)

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
**403** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_security_monitoring_signals**
> SecurityMonitoringSignalsListResponse search_security_monitoring_signals()

Get a list of security signals

Returns security signals that match a search query. Both this endpoint and the GET endpoint can be used interchangeably for listing security signals.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    body = SecurityMonitoringSignalListRequest(
        filter=SecurityMonitoringSignalListRequestFilter(
            _from=dateutil_parser('2019-01-02T09:42:36.32Z'),
            query="security:attack status:high",
            to=dateutil_parser('2019-01-03T09:42:36.32Z'),
        ),
        page=SecurityMonitoringSignalListRequestPage(
            cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
            limit=25,
        ),
        sort=SecurityMonitoringSignalsSort("timestamp"),
    ) # SecurityMonitoringSignalListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of security signals
        api_response = api_instance.search_security_monitoring_signals(body=body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling SecurityMonitoringApi->search_security_monitoring_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityMonitoringSignalListRequest**](SecurityMonitoringSignalListRequest.md)|  | [optional]

### Return type

[**SecurityMonitoringSignalsListResponse**](SecurityMonitoringSignalsListResponse.md)

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

# **update_security_monitoring_rule**
> SecurityMonitoringRuleResponse update_security_monitoring_rule(rule_id)

Update an existing rule

Update an existing rule. When updating `cases`, `queries` or `options`, the whole field must be included. For example, when modifying a query all queries must be included. Default rules can only be updated to be enabled and to change notifications.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import security_monitoring_api
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
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = "rule_id_example" # str | The ID of the rule.
    body = SecurityMonitoringRuleUpdatePayload(
        cases=[
            SecurityMonitoringRuleCase(
                condition="condition_example",
                name="name_example",
                notifications=[
                    "notifications_example",
                ],
                status=SecurityMonitoringRuleSeverity("info"),
            ),
        ],
        is_enabled=True,
        message="message_example",
        name="name_example",
        options=SecurityMonitoringRuleOptions(
            evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
            keep_alive=SecurityMonitoringRuleKeepAlive(0),
            max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(0),
        ),
        queries=[
            SecurityMonitoringRuleQuery(
                aggregation=SecurityMonitoringRuleQueryAggregation("count"),
                distinct_fields=[
                    "distinct_fields_example",
                ],
                group_by_fields=[
                    "group_by_fields_example",
                ],
                metric="metric_example",
                name="name_example",
                query="query_example",
            ),
        ],
        tags=[
            "tags_example",
        ],
    ) # SecurityMonitoringRuleUpdatePayload |  (optional)

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
 **body** | [**SecurityMonitoringRuleUpdatePayload**](SecurityMonitoringRuleUpdatePayload.md)|  | [optional]

### Return type

[**SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

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

