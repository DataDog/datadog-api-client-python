# datadog_api_client.v2.CloudSIEMApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                                                                       | HTTP request                                                                               | Description                          |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------ |
| [**create_security_filter**](CloudSIEMApi.md#create_security_filter)                         | **POST** /api/v2/security_monitoring/configuration/security_filters                        | Create a security filter             |
| [**create_security_monitoring_rule**](CloudSIEMApi.md#create_security_monitoring_rule)       | **POST** /api/v2/security_monitoring/rules                                                 | Create a detection rule              |
| [**delete_security_filter**](CloudSIEMApi.md#delete_security_filter)                         | **DELETE** /api/v2/security_monitoring/configuration/security_filters/{security_filter_id} | Delete a security filter             |
| [**delete_security_monitoring_rule**](CloudSIEMApi.md#delete_security_monitoring_rule)       | **DELETE** /api/v2/security_monitoring/rules/{rule_id}                                     | Delete an existing rule              |
| [**get_security_filter**](CloudSIEMApi.md#get_security_filter)                               | **GET** /api/v2/security_monitoring/configuration/security_filters/{security_filter_id}    | Get a security filter                |
| [**get_security_monitoring_rule**](CloudSIEMApi.md#get_security_monitoring_rule)             | **GET** /api/v2/security_monitoring/rules/{rule_id}                                        | Get a rule&#39;s details             |
| [**list_security_filters**](CloudSIEMApi.md#list_security_filters)                           | **GET** /api/v2/security_monitoring/configuration/security_filters                         | Get all security filters             |
| [**list_security_monitoring_rules**](CloudSIEMApi.md#list_security_monitoring_rules)         | **GET** /api/v2/security_monitoring/rules                                                  | List rules                           |
| [**list_security_monitoring_signals**](CloudSIEMApi.md#list_security_monitoring_signals)     | **GET** /api/v2/security_monitoring/signals                                                | Get a quick list of security signals |
| [**search_security_monitoring_signals**](CloudSIEMApi.md#search_security_monitoring_signals) | **POST** /api/v2/security_monitoring/signals/search                                        | Get a list of security signals       |
| [**update_security_filter**](CloudSIEMApi.md#update_security_filter)                         | **PATCH** /api/v2/security_monitoring/configuration/security_filters/{security_filter_id}  | Update a security filter             |
| [**update_security_monitoring_rule**](CloudSIEMApi.md#update_security_monitoring_rule)       | **PUT** /api/v2/security_monitoring/rules/{rule_id}                                        | Update an existing rule              |

# **create_security_filter**

> SecurityFilterResponse create_security_filter(body)

Create a security filter.

See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/)
for more examples.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    body = SecurityFilterCreateRequest(
        data=SecurityFilterCreateData(
            attributes=SecurityFilterCreateAttributes(
                exclusion_filters=[
                    SecurityFilterExclusionFilter(
                        name="Exclude staging",
                        query="source:staging",
                    ),
                ],
                filtered_data_type=SecurityFilterFilteredDataType("logs"),
                is_enabled=True,
                name="Custom security filter",
                query="service:api",
            ),
            type=SecurityFilterType("security_filters"),
        ),
    )  # SecurityFilterCreateRequest | The definition of the new security filter.

    # example passing only required values which don't have defaults set
    try:
        # Create a security filter
        api_response = api_instance.create_security_filter(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->create_security_filter: %s\n" % e)
```

### Parameters

| Name     | Type                                                              | Description                                | Notes |
| -------- | ----------------------------------------------------------------- | ------------------------------------------ | ----- |
| **body** | [**SecurityFilterCreateRequest**](SecurityFilterCreateRequest.md) | The definition of the new security filter. |

### Return type

[**SecurityFilterResponse**](SecurityFilterResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Not Authorized    | -                |
| **409**     | Conflict          | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_security_monitoring_rule**

> SecurityMonitoringRuleResponse create_security_monitoring_rule(body)

Create a detection rule.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    body = SecurityMonitoringRuleCreatePayload(
        cases=[
            SecurityMonitoringRuleCaseCreate(
                condition="condition_example",
                name="name_example",
                notifications=[
                    "notifications_example",
                ],
                status=SecurityMonitoringRuleSeverity("critical"),
            ),
        ],
        filters=[
            SecurityMonitoringFilter(
                action=SecurityMonitoringFilterAction("require"),
                query="query_example",
            ),
        ],
        has_extended_title=True,
        is_enabled=True,
        message="",
        name="My Cloud SIEM rule.",
        options=SecurityMonitoringRuleOptions(
            detection_method=SecurityMonitoringRuleDetectionMethod("threshold"),
            evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
            keep_alive=SecurityMonitoringRuleKeepAlive(0),
            max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(0),
            new_value_options=SecurityMonitoringRuleNewValueOptions(
                forget_after=SecurityMonitoringRuleNewValueOptionsForgetAfter(1),
                learning_duration=SecurityMonitoringRuleNewValueOptionsLearningDuration(0),
            ),
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
                query="a > 3",
            ),
        ],
        tags=["env:prod","team:security"],
        type=SecurityMonitoringRuleTypeCreate("log_detection"),
    )  # SecurityMonitoringRuleCreatePayload |

    # example passing only required values which don't have defaults set
    try:
        # Create a detection rule
        api_response = api_instance.create_security_monitoring_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->create_security_monitoring_rule: %s\n" % e)
```

### Parameters

| Name     | Type                                                                              | Description | Notes |
| -------- | --------------------------------------------------------------------------------- | ----------- | ----- |
| **body** | [**SecurityMonitoringRuleCreatePayload**](SecurityMonitoringRuleCreatePayload.md) |             |

### Return type

[**SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Not Authorized    | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_security_filter**

> delete_security_filter(security_filter_id)

Delete a specific security filter.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    security_filter_id = "security_filter_id_example"  # str | The ID of the security filter.

    # example passing only required values which don't have defaults set
    try:
        # Delete a security filter
        api_instance.delete_security_filter(security_filter_id)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->delete_security_filter: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                    | Notes |
| ---------------------- | ------- | ------------------------------ | ----- |
| **security_filter_id** | **str** | The ID of the security filter. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **204**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_security_monitoring_rule**

> delete_security_monitoring_rule(rule_id)

Delete an existing rule. Default rules cannot be deleted.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    rule_id = "rule_id_example"  # str | The ID of the rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing rule
        api_instance.delete_security_monitoring_rule(rule_id)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->delete_security_monitoring_rule: %s\n" % e)
```

### Parameters

| Name        | Type    | Description         | Notes |
| ----------- | ------- | ------------------- | ----- |
| **rule_id** | **str** | The ID of the rule. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **204**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_security_filter**

> SecurityFilterResponse get_security_filter(security_filter_id)

Get the details of a specific security filter.

See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/)
for more examples.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    security_filter_id = "security_filter_id_example"  # str | The ID of the security filter.

    # example passing only required values which don't have defaults set
    try:
        # Get a security filter
        api_response = api_instance.get_security_filter(security_filter_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->get_security_filter: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                    | Notes |
| ---------------------- | ------- | ------------------------------ | ----- |
| **security_filter_id** | **str** | The ID of the security filter. |

### Return type

[**SecurityFilterResponse**](SecurityFilterResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_security_monitoring_rule**

> SecurityMonitoringRuleResponse get_security_monitoring_rule(rule_id)

Get a rule's details.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    rule_id = "rule_id_example"  # str | The ID of the rule.

    # example passing only required values which don't have defaults set
    try:
        # Get a rule's details
        api_response = api_instance.get_security_monitoring_rule(rule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->get_security_monitoring_rule: %s\n" % e)
```

### Parameters

| Name        | Type    | Description         | Notes |
| ----------- | ------- | ------------------- | ----- |
| **rule_id** | **str** | The ID of the rule. |

### Return type

[**SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_security_filters**

> SecurityFiltersResponse list_security_filters()

Get the list of configured security filters with their definitions.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all security filters
        api_response = api_instance.list_security_filters()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->list_security_filters: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SecurityFiltersResponse**](SecurityFiltersResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_security_monitoring_rules**

> SecurityMonitoringListRulesResponse list_security_monitoring_rules()

List rules.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List rules
        api_response = api_instance.list_security_monitoring_rules(page_size=page_size, page_number=page_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->list_security_monitoring_rules: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                     | Notes                                                             |
| --------------- | ------- | ------------------------------- | ----------------------------------------------------------------- |
| **page_size**   | **int** | Size for a given page.          | [optional] if omitted the server will use the default value of 10 |
| **page_number** | **int** | Specific page number to return. | [optional] if omitted the server will use the default value of 0  |

### Return type

[**SecurityMonitoringListRulesResponse**](SecurityMonitoringListRulesResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_security_monitoring_signals**

> SecurityMonitoringSignalsListResponse list_security_monitoring_signals()

The list endpoint returns security signals that match a search query.
Both this endpoint and the POST endpoint can be used interchangeably when listing
security signals.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_security_monitoring_signals"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    filter_query = "security:attack status:high"  # str | The search query for security signals. (optional)
    filter_from = dateutil_parser('2019-01-02T09:42:36.320Z')  # datetime | The minimum timestamp for requested security signals. (optional)
    filter_to = dateutil_parser('2019-01-03T09:42:36.320Z')  # datetime | The maximum timestamp for requested security signals. (optional)
    sort = SecurityMonitoringSignalsSort("timestamp")  # SecurityMonitoringSignalsSort | The order of the security signals in results. (optional)
    page_cursor = "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="  # str | A list of results using the cursor provided in the previous query. (optional)
    page_limit = 25  # int | The maximum number of security signals in the response. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a quick list of security signals
        api_response = api_instance.list_security_monitoring_signals(filter_query=filter_query, filter_from=filter_from, filter_to=filter_to, sort=sort, page_cursor=page_cursor, page_limit=page_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->list_security_monitoring_signals: %s\n" % e)
```

### Parameters

| Name             | Type                              | Description                                                        | Notes                                                             |
| ---------------- | --------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **filter_query** | **str**                           | The search query for security signals.                             | [optional]                                                        |
| **filter_from**  | **datetime**                      | The minimum timestamp for requested security signals.              | [optional]                                                        |
| **filter_to**    | **datetime**                      | The maximum timestamp for requested security signals.              | [optional]                                                        |
| **sort**         | **SecurityMonitoringSignalsSort** | The order of the security signals in results.                      | [optional]                                                        |
| **page_cursor**  | **str**                           | A list of results using the cursor provided in the previous query. | [optional]                                                        |
| **page_limit**   | **int**                           | The maximum number of security signals in the response.            | [optional] if omitted the server will use the default value of 10 |

### Return type

[**SecurityMonitoringSignalsListResponse**](SecurityMonitoringSignalsListResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Not Authorized    | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_security_monitoring_signals**

> SecurityMonitoringSignalsListResponse search_security_monitoring_signals()

Returns security signals that match a search query.
Both this endpoint and the GET endpoint can be used interchangeably for listing
security signals.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["search_security_monitoring_signals"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
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
    )  # SecurityMonitoringSignalListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of security signals
        api_response = api_instance.search_security_monitoring_signals(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->search_security_monitoring_signals: %s\n" % e)
```

### Parameters

| Name     | Type                                                                              | Description | Notes      |
| -------- | --------------------------------------------------------------------------------- | ----------- | ---------- |
| **body** | [**SecurityMonitoringSignalListRequest**](SecurityMonitoringSignalListRequest.md) |             | [optional] |

### Return type

[**SecurityMonitoringSignalsListResponse**](SecurityMonitoringSignalsListResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Not Authorized    | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_security_filter**

> SecurityFilterResponse update_security_filter(security_filter_id, body)

Update a specific security filter.
Returns the security filter object when the request is successful.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    security_filter_id = "security_filter_id_example"  # str | The ID of the security filter.
    body = SecurityFilterUpdateRequest(
        data=SecurityFilterUpdateData(
            attributes=SecurityFilterUpdateAttributes(
                exclusion_filters=[
                    SecurityFilterExclusionFilter(
                        name="Exclude staging",
                        query="source:staging",
                    ),
                ],
                filtered_data_type=SecurityFilterFilteredDataType("logs"),
                is_enabled=True,
                name="Custom security filter",
                query="service:api",
                version=1,
            ),
            type=SecurityFilterType("security_filters"),
        ),
    )  # SecurityFilterUpdateRequest | New definition of the security filter.

    # example passing only required values which don't have defaults set
    try:
        # Update a security filter
        api_response = api_instance.update_security_filter(security_filter_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->update_security_filter: %s\n" % e)
```

### Parameters

| Name                   | Type                                                              | Description                            | Notes |
| ---------------------- | ----------------------------------------------------------------- | -------------------------------------- | ----- |
| **security_filter_id** | **str**                                                           | The ID of the security filter.         |
| **body**               | [**SecurityFilterUpdateRequest**](SecurityFilterUpdateRequest.md) | New definition of the security filter. |

### Return type

[**SecurityFilterResponse**](SecurityFilterResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description             | Response headers |
| ----------- | ----------------------- | ---------------- |
| **200**     | OK                      | -                |
| **400**     | Bad Request             | -                |
| **403**     | Not Authorized          | -                |
| **404**     | Not Found               | -                |
| **409**     | Concurrent Modification | -                |
| **429**     | Too many requests       | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_security_monitoring_rule**

> SecurityMonitoringRuleResponse update_security_monitoring_rule(rule_id, body)

Update an existing rule. When updating `cases`, `queries` or `options`, the whole field
must be included. For example, when modifying a query all queries must be included.
Default rules can only be updated to be enabled and to change notifications.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_siem_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_siem_api.CloudSIEMApi(api_client)
    rule_id = "rule_id_example"  # str | The ID of the rule.
    body = SecurityMonitoringRuleUpdatePayload(
        cases=[
            SecurityMonitoringRuleCase(
                condition="condition_example",
                name="name_example",
                notifications=[
                    "notifications_example",
                ],
                status=SecurityMonitoringRuleSeverity("critical"),
            ),
        ],
        filters=[
            SecurityMonitoringFilter(
                action=SecurityMonitoringFilterAction("require"),
                query="query_example",
            ),
        ],
        has_extended_title=True,
        is_enabled=True,
        message="message_example",
        name="name_example",
        options=SecurityMonitoringRuleOptions(
            detection_method=SecurityMonitoringRuleDetectionMethod("threshold"),
            evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
            keep_alive=SecurityMonitoringRuleKeepAlive(0),
            max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(0),
            new_value_options=SecurityMonitoringRuleNewValueOptions(
                forget_after=SecurityMonitoringRuleNewValueOptionsForgetAfter(1),
                learning_duration=SecurityMonitoringRuleNewValueOptionsLearningDuration(0),
            ),
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
        version=1,
    )  # SecurityMonitoringRuleUpdatePayload |

    # example passing only required values which don't have defaults set
    try:
        # Update an existing rule
        api_response = api_instance.update_security_monitoring_rule(rule_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudSIEMApi->update_security_monitoring_rule: %s\n" % e)
```

### Parameters

| Name        | Type                                                                              | Description         | Notes |
| ----------- | --------------------------------------------------------------------------------- | ------------------- | ----- |
| **rule_id** | **str**                                                                           | The ID of the rule. |
| **body**    | [**SecurityMonitoringRuleUpdatePayload**](SecurityMonitoringRuleUpdatePayload.md) |                     |

### Return type

[**SecurityMonitoringRuleResponse**](SecurityMonitoringRuleResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description             | Response headers |
| ----------- | ----------------------- | ---------------- |
| **200**     | OK                      | -                |
| **400**     | Bad Request             | -                |
| **401**     | Concurrent Modification | -                |
| **403**     | Not Authorized          | -                |
| **404**     | Not Found               | -                |
| **429**     | Too many requests       | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
