# datadog_api_client.v1.UsageMeteringApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_custom_reports**](UsageMeteringApi.md#get_daily_custom_reports) | **GET** /api/v1/daily_custom_reports | Get the list of available daily custom reports
[**get_monthly_custom_reports**](UsageMeteringApi.md#get_monthly_custom_reports) | **GET** /api/v1/monthly_custom_reports | Get the list of available monthly custom reports
[**get_specified_daily_custom_reports**](UsageMeteringApi.md#get_specified_daily_custom_reports) | **GET** /api/v1/daily_custom_reports/{report_id} | Get specified daily custom reports
[**get_specified_monthly_custom_reports**](UsageMeteringApi.md#get_specified_monthly_custom_reports) | **GET** /api/v1/monthly_custom_reports/{report_id} | Get specified monthly custom reports
[**get_tracing_without_limits**](UsageMeteringApi.md#get_tracing_without_limits) | **GET** /api/v1/usage/tracing-without-limits | Get hourly usage for tracing without limits
[**get_usage_analyzed_logs**](UsageMeteringApi.md#get_usage_analyzed_logs) | **GET** /api/v1/usage/analyzed_logs | Get hourly usage for analyzed logs
[**get_usage_billable_summary**](UsageMeteringApi.md#get_usage_billable_summary) | **GET** /api/v1/usage/billable-summary | Get billable usage across your multi-org account
[**get_usage_fargate**](UsageMeteringApi.md#get_usage_fargate) | **GET** /api/v1/usage/fargate | Get hourly usage for Fargate
[**get_usage_hosts**](UsageMeteringApi.md#get_usage_hosts) | **GET** /api/v1/usage/hosts | Get hourly usage for hosts and containers
[**get_usage_lambda**](UsageMeteringApi.md#get_usage_lambda) | **GET** /api/v1/usage/aws_lambda | Get hourly usage for Lambda
[**get_usage_logs**](UsageMeteringApi.md#get_usage_logs) | **GET** /api/v1/usage/logs | Get hourly usage for Logs
[**get_usage_logs_by_index**](UsageMeteringApi.md#get_usage_logs_by_index) | **GET** /api/v1/usage/logs_by_index | Get hourly usage for Logs by Index
[**get_usage_network_flows**](UsageMeteringApi.md#get_usage_network_flows) | **GET** /api/v1/usage/network_flows | Get hourly usage for Network Flows
[**get_usage_network_hosts**](UsageMeteringApi.md#get_usage_network_hosts) | **GET** /api/v1/usage/network_hosts | Get hourly usage for Network Hosts
[**get_usage_profiling**](UsageMeteringApi.md#get_usage_profiling) | **GET** /api/v1/usage/profiling | Get hourly usage for profiled hosts
[**get_usage_rum_sessions**](UsageMeteringApi.md#get_usage_rum_sessions) | **GET** /api/v1/usage/rum_sessions | Get hourly usage for RUM Sessions
[**get_usage_snmp**](UsageMeteringApi.md#get_usage_snmp) | **GET** /api/v1/usage/snmp | Get hourly usage for SNMP devices
[**get_usage_summary**](UsageMeteringApi.md#get_usage_summary) | **GET** /api/v1/usage/summary | Get usage across your multi-org account
[**get_usage_synthetics**](UsageMeteringApi.md#get_usage_synthetics) | **GET** /api/v1/usage/synthetics | Get hourly usage for Synthetics Checks
[**get_usage_synthetics_api**](UsageMeteringApi.md#get_usage_synthetics_api) | **GET** /api/v1/usage/synthetics_api | Get hourly usage for Synthetics API Checks
[**get_usage_synthetics_browser**](UsageMeteringApi.md#get_usage_synthetics_browser) | **GET** /api/v1/usage/synthetics_browser | Get hourly usage for Synthetics Browser Checks
[**get_usage_timeseries**](UsageMeteringApi.md#get_usage_timeseries) | **GET** /api/v1/usage/timeseries | Get hourly usage for custom metrics
[**get_usage_top_avg_metrics**](UsageMeteringApi.md#get_usage_top_avg_metrics) | **GET** /api/v1/usage/top_avg_metrics | Get top 500 custom metrics by hourly average
[**get_usage_trace**](UsageMeteringApi.md#get_usage_trace) | **GET** /api/v1/usage/traces | Get hourly usage for Trace Search


# **get_daily_custom_reports**
> UsageCustomReportsResponse get_daily_custom_reports()

Get the list of available daily custom reports

Get daily custom reports.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    page_size = 1 # int | The number of files to return in the response. `[default=60]`. (optional)
    page_number = 1 # int | The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`. (optional)
    sort_dir = UsageSortDirection("desc") # UsageSortDirection | The direction to sort by: `[desc, asc]`. (optional)
    sort = UsageSort("start_date") # UsageSort | The field to sort by: `[computed_on, size, start_date, end_date]`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of available daily custom reports
        api_response = api_instance.get_daily_custom_reports(page_size=page_size, page_number=page_number, sort_dir=sort_dir, sort=sort)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_daily_custom_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of files to return in the response. &#x60;[default&#x3D;60]&#x60;. | [optional]
 **page_number** | **int**| The identifier of the first page to return. This parameter is used for the pagination feature &#x60;[default&#x3D;0]&#x60;. | [optional]
 **sort_dir** | **UsageSortDirection**| The direction to sort by: &#x60;[desc, asc]&#x60;. | [optional]
 **sort** | **UsageSort**| The field to sort by: &#x60;[computed_on, size, start_date, end_date]&#x60;. | [optional]

### Return type

[**UsageCustomReportsResponse**](UsageCustomReportsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_monthly_custom_reports**
> UsageCustomReportsResponse get_monthly_custom_reports()

Get the list of available monthly custom reports

Get monthly custom reports.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    page_size = 1 # int | The number of files to return in the response `[default=60].` (optional)
    page_number = 1 # int | The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`. (optional)
    sort_dir = UsageSortDirection("desc") # UsageSortDirection | The direction to sort by: `[desc, asc]`. (optional)
    sort = UsageSort("start_date") # UsageSort | The field to sort by: `[computed_on, size, start_date, end_date]`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of available monthly custom reports
        api_response = api_instance.get_monthly_custom_reports(page_size=page_size, page_number=page_number, sort_dir=sort_dir, sort=sort)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_monthly_custom_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of files to return in the response &#x60;[default&#x3D;60].&#x60; | [optional]
 **page_number** | **int**| The identifier of the first page to return. This parameter is used for the pagination feature &#x60;[default&#x3D;0]&#x60;. | [optional]
 **sort_dir** | **UsageSortDirection**| The direction to sort by: &#x60;[desc, asc]&#x60;. | [optional]
 **sort** | **UsageSort**| The field to sort by: &#x60;[computed_on, size, start_date, end_date]&#x60;. | [optional]

### Return type

[**UsageCustomReportsResponse**](UsageCustomReportsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_specified_daily_custom_reports**
> UsageSpecifiedCustomReportsResponse get_specified_daily_custom_reports(report_id)

Get specified daily custom reports

Get specified daily custom reports.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    report_id = "report_id_example" # str | The specified ID to search results for.

    # example passing only required values which don't have defaults set
    try:
        # Get specified daily custom reports
        api_response = api_instance.get_specified_daily_custom_reports(report_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_specified_daily_custom_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The specified ID to search results for. |

### Return type

[**UsageSpecifiedCustomReportsResponse**](UsageSpecifiedCustomReportsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden - User is not authorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_specified_monthly_custom_reports**
> UsageSpecifiedCustomReportsResponse get_specified_monthly_custom_reports(report_id)

Get specified monthly custom reports

Get specified monthly custom reports.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    report_id = "report_id_example" # str | The specified ID to search results for.

    # example passing only required values which don't have defaults set
    try:
        # Get specified monthly custom reports
        api_response = api_instance.get_specified_monthly_custom_reports(report_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_specified_monthly_custom_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The specified ID to search results for. |

### Return type

[**UsageSpecifiedCustomReportsResponse**](UsageSpecifiedCustomReportsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_tracing_without_limits**
> UsageTracingWithoutLimitsResponse get_tracing_without_limits(start_hr)

Get hourly usage for tracing without limits

Get hourly usage for tracing without limits.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for tracing without limits
        api_response = api_instance.get_tracing_without_limits(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_tracing_without_limits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for tracing without limits
        api_response = api_instance.get_tracing_without_limits(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_tracing_without_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage ending **before** this hour. | [optional]

### Return type

[**UsageTracingWithoutLimitsResponse**](UsageTracingWithoutLimitsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_analyzed_logs**
> UsageAnalyzedLogsResponse get_usage_analyzed_logs(start_hr)

Get hourly usage for analyzed logs

Get hourly usage for analyzed logs (Security Monitoring).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for analyzed logs
        api_response = api_instance.get_usage_analyzed_logs(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_analyzed_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for analyzed logs
        api_response = api_instance.get_usage_analyzed_logs(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_analyzed_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage ending **before** this hour. | [optional]

### Return type

[**UsageAnalyzedLogsResponse**](UsageAnalyzedLogsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_billable_summary**
> UsageBillableSummaryResponse get_usage_billable_summary()

Get billable usage across your multi-org account

Get billable usage across your multi-org account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage starting this month. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get billable usage across your multi-org account
        api_response = api_instance.get_usage_billable_summary(month=month)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_billable_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **datetime**| Datetime in ISO-8601 format, UTC, precise to month: &#x60;[YYYY-MM]&#x60; for usage starting this month. | [optional]

### Return type

[**UsageBillableSummaryResponse**](UsageBillableSummaryResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_fargate**
> UsageFargateResponse get_usage_fargate(start_hr)

Get hourly usage for Fargate

Get hourly usage for [Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Fargate
        api_response = api_instance.get_usage_fargate(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_fargate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Fargate
        api_response = api_instance.get_usage_fargate(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_fargate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageFargateResponse**](UsageFargateResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_hosts**
> UsageHostsResponse get_usage_hosts(start_hr)

Get hourly usage for hosts and containers

Get hourly usage for hosts and containers.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for hosts and containers
        api_response = api_instance.get_usage_hosts(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_hosts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for hosts and containers
        api_response = api_instance.get_usage_hosts(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageHostsResponse**](UsageHostsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_lambda**
> UsageLambdaResponse get_usage_lambda(start_hr)

Get hourly usage for Lambda

Get hourly usage for lambda.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Lambda
        api_response = api_instance.get_usage_lambda(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_lambda: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Lambda
        api_response = api_instance.get_usage_lambda(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_lambda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageLambdaResponse**](UsageLambdaResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_logs**
> UsageLogsResponse get_usage_logs(start_hr)

Get hourly usage for Logs

Get hourly usage for logs.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Logs
        api_response = api_instance.get_usage_logs(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Logs
        api_response = api_instance.get_usage_logs(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageLogsResponse**](UsageLogsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_logs_by_index**
> UsageLogsByIndexResponse get_usage_logs_by_index(start_hr)

Get hourly usage for Logs by Index

Get hourly usage for logs by index.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)
    index_name = [
        "index_name_example",
    ] # [str] | Comma-separated list of log index names. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Logs by Index
        api_response = api_instance.get_usage_logs_by_index(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_logs_by_index: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Logs by Index
        api_response = api_instance.get_usage_logs_by_index(start_hr, end_hr=end_hr, index_name=index_name)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_logs_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]
 **index_name** | **[str]**| Comma-separated list of log index names. | [optional]

### Return type

[**UsageLogsByIndexResponse**](UsageLogsByIndexResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_network_flows**
> UsageNetworkFlowsResponse get_usage_network_flows(start_hr)

Get hourly usage for Network Flows

Get hourly usage for network flows.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Network Flows
        api_response = api_instance.get_usage_network_flows(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_network_flows: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Network Flows
        api_response = api_instance.get_usage_network_flows(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_network_flows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage ending **before** this hour. | [optional]

### Return type

[**UsageNetworkFlowsResponse**](UsageNetworkFlowsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_network_hosts**
> UsageNetworkHostsResponse get_usage_network_hosts(start_hr)

Get hourly usage for Network Hosts

Get hourly usage for network hosts.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Network Hosts
        api_response = api_instance.get_usage_network_hosts(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_network_hosts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Network Hosts
        api_response = api_instance.get_usage_network_hosts(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_network_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageNetworkHostsResponse**](UsageNetworkHostsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_profiling**
> UsageProfilingResponse get_usage_profiling(start_hr)

Get hourly usage for profiled hosts

Get hourly usage for profiled hosts.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for profiled hosts
        api_response = api_instance.get_usage_profiling(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_profiling: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for profiled hosts
        api_response = api_instance.get_usage_profiling(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_profiling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage ending **before** this hour. | [optional]

### Return type

[**UsageProfilingResponse**](UsageProfilingResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_rum_sessions**
> UsageRumSessionsResponse get_usage_rum_sessions(start_hr)

Get hourly usage for RUM Sessions

Get hourly usage for [RUM](https://docs.datadoghq.com/real_user_monitoring/) Sessions.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)
    type = "type_example" # str | RUM type: `[browser, mobile]`. Defaults to `browser`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for RUM Sessions
        api_response = api_instance.get_usage_rum_sessions(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_rum_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for RUM Sessions
        api_response = api_instance.get_usage_rum_sessions(start_hr, end_hr=end_hr, type=type)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_rum_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]
 **type** | **str**| RUM type: &#x60;[browser, mobile]&#x60;. Defaults to &#x60;browser&#x60;. | [optional]

### Return type

[**UsageRumSessionsResponse**](UsageRumSessionsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_snmp**
> UsageSNMPResponse get_usage_snmp(start_hr)

Get hourly usage for SNMP devices

Get hourly usage for SNMP devices.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for SNMP devices
        api_response = api_instance.get_usage_snmp(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_snmp: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for SNMP devices
        api_response = api_instance.get_usage_snmp(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_snmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: &#x60;[YYYY-MM-DDThh]&#x60; for usage ending **before** this hour. | [optional]

### Return type

[**UsageSNMPResponse**](UsageSNMPResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_summary**
> UsageSummaryResponse get_usage_summary(start_month)

Get usage across your multi-org account

Get usage across your multi-org account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage beginning in this month. Maximum of 15 months ago.
    end_month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage ending this month. (optional)
    include_org_details = True # bool | Include usage summaries for each sub-org. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get usage across your multi-org account
        api_response = api_instance.get_usage_summary(start_month)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage across your multi-org account
        api_response = api_instance.get_usage_summary(start_month, end_month=end_month, include_org_details=include_org_details)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_month** | **datetime**| Datetime in ISO-8601 format, UTC, precise to month: &#x60;[YYYY-MM]&#x60; for usage beginning in this month. Maximum of 15 months ago. |
 **end_month** | **datetime**| Datetime in ISO-8601 format, UTC, precise to month: &#x60;[YYYY-MM]&#x60; for usage ending this month. | [optional]
 **include_org_details** | **bool**| Include usage summaries for each sub-org. | [optional]

### Return type

[**UsageSummaryResponse**](UsageSummaryResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_synthetics**
> UsageSyntheticsResponse get_usage_synthetics(start_hr)

Get hourly usage for Synthetics Checks

Get hourly usage for [Synthetics checks](https://docs.datadoghq.com/synthetics/).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Synthetics Checks
        api_response = api_instance.get_usage_synthetics(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Synthetics Checks
        api_response = api_instance.get_usage_synthetics(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageSyntheticsResponse**](UsageSyntheticsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_synthetics_api**
> UsageSyntheticsAPIResponse get_usage_synthetics_api(start_hr)

Get hourly usage for Synthetics API Checks

Get hourly usage for [synthetics API checks](https://docs.datadoghq.com/synthetics/).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Synthetics API Checks
        api_response = api_instance.get_usage_synthetics_api(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics_api: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Synthetics API Checks
        api_response = api_instance.get_usage_synthetics_api(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageSyntheticsAPIResponse**](UsageSyntheticsAPIResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_synthetics_browser**
> UsageSyntheticsBrowserResponse get_usage_synthetics_browser(start_hr)

Get hourly usage for Synthetics Browser Checks

Get hourly usage for synthetics browser checks.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Synthetics Browser Checks
        api_response = api_instance.get_usage_synthetics_browser(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics_browser: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Synthetics Browser Checks
        api_response = api_instance.get_usage_synthetics_browser(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics_browser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageSyntheticsBrowserResponse**](UsageSyntheticsBrowserResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_timeseries**
> UsageTimeseriesResponse get_usage_timeseries(start_hr)

Get hourly usage for custom metrics

Get hourly usage for [custom metrics](https://docs.datadoghq.com/developers/metrics/custom_metrics/).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for custom metrics
        api_response = api_instance.get_usage_timeseries(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_timeseries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for custom metrics
        api_response = api_instance.get_usage_timeseries(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageTimeseriesResponse**](UsageTimeseriesResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_top_avg_metrics**
> UsageTopAvgMetricsResponse get_usage_top_avg_metrics(month)

Get top 500 custom metrics by hourly average

Get top [custom metrics](https://docs.datadoghq.com/developers/metrics/custom_metrics/) by hourly average.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to month: [YYYY-MM] for usage beginning at this hour.
    names = [
        "names_example",
    ] # [str] | Comma-separated list of metric names. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get top 500 custom metrics by hourly average
        api_response = api_instance.get_usage_top_avg_metrics(month)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_top_avg_metrics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get top 500 custom metrics by hourly average
        api_response = api_instance.get_usage_top_avg_metrics(month, names=names)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_top_avg_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **datetime**| Datetime in ISO-8601 format, UTC, precise to month: [YYYY-MM] for usage beginning at this hour. |
 **names** | **[str]**| Comma-separated list of metric names. | [optional]

### Return type

[**UsageTopAvgMetricsResponse**](UsageTopAvgMetricsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_usage_trace**
> UsageTraceResponse get_usage_trace(start_hr)

Get hourly usage for Trace Search

Get hourly usage for trace search.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import usage_metering_api
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
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Trace Search
        api_response = api_instance.get_usage_trace(start_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_trace: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Trace Search
        api_response = api_instance.get_usage_trace(start_hr, end_hr=end_hr)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour. |
 **end_hr** | **datetime**| Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. | [optional]

### Return type

[**UsageTraceResponse**](UsageTraceResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;datetime-format=rfc3339

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden - User is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

