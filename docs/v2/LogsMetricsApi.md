# datadog_api_client.v2.LogsMetricsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logs_metric**](LogsMetricsApi.md#create_logs_metric) | **POST** /api/v2/logs/config/metrics | Create a log-based metric
[**delete_logs_metric**](LogsMetricsApi.md#delete_logs_metric) | **DELETE** /api/v2/logs/config/metrics/{metric_id} | Delete a log-based metric
[**get_logs_metric**](LogsMetricsApi.md#get_logs_metric) | **GET** /api/v2/logs/config/metrics/{metric_id} | Get a log-based metric
[**list_logs_metrics**](LogsMetricsApi.md#list_logs_metrics) | **GET** /api/v2/logs/config/metrics | Get all log-based metrics
[**update_logs_metric**](LogsMetricsApi.md#update_logs_metric) | **PATCH** /api/v2/logs/config/metrics/{metric_id} | Update a log-based metric


# **create_logs_metric**
> LogsMetricResponse create_logs_metric(body)

Create a metric based on your ingested logs in your organization.
Returns the log-based metric object from the request body when the request is successful.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)
    body = LogsMetricCreateRequest(
        data=LogsMetricCreateData(
            attributes=LogsMetricCreateAttributes(
                compute=LogsMetricCompute(
                    aggregation_type=LogsMetricComputeAggregationType("distribution"),
                    path="@duration",
                ),
                filter=LogsMetricFilter(
                    query="service:web* AND @http.status_code:[200 TO 299]",
                ),
                group_by=[
                    LogsMetricGroupBy(
                        path="@http.status_code",
                        tag_name="status_code",
                    ),
                ],
            ),
            id="logs.page.load.count",
            type=LogsMetricType("logs_metrics"),
        ),
    )  # LogsMetricCreateRequest | The definition of the new log-based metric.

    # example passing only required values which don't have defaults set
    try:
        # Create a log-based metric
        api_response = api_instance.create_logs_metric(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->create_logs_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsMetricCreateRequest**](LogsMetricCreateRequest.md)| The definition of the new log-based metric. |

### Return type

[**LogsMetricResponse**](LogsMetricResponse.md)

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
**409** | Conflict |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_logs_metric**
> delete_logs_metric(metric_id)

Delete a specific log-based metric from your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)
    metric_id = "metric_id_example"  # str | The name of the log-based metric.

    # example passing only required values which don't have defaults set
    try:
        # Delete a log-based metric
        api_instance.delete_logs_metric(metric_id)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->delete_logs_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| The name of the log-based metric. |

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
**403** | Not Authorized |  -  |
**404** | Not Found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_logs_metric**
> LogsMetricResponse get_logs_metric(metric_id)

Get a specific log-based metric from your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)
    metric_id = "metric_id_example"  # str | The name of the log-based metric.

    # example passing only required values which don't have defaults set
    try:
        # Get a log-based metric
        api_response = api_instance.get_logs_metric(metric_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->get_logs_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| The name of the log-based metric. |

### Return type

[**LogsMetricResponse**](LogsMetricResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Not Authorized |  -  |
**404** | Not Found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs_metrics**
> LogsMetricsResponse list_logs_metrics()

Get the list of configured log-based metrics with their definitions.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all log-based metrics
        api_response = api_instance.list_logs_metrics()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->list_logs_metrics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsMetricsResponse**](LogsMetricsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Not Authorized |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_logs_metric**
> LogsMetricResponse update_logs_metric(metric_id, body)

Update a specific log-based metric from your organization.
Returns the log-based metric object from the request body when the request is successful.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)
    metric_id = "metric_id_example"  # str | The name of the log-based metric.
    body = LogsMetricUpdateRequest(
        data=LogsMetricUpdateData(
            attributes=LogsMetricUpdateAttributes(
                filter=LogsMetricFilter(
                    query="service:web* AND @http.status_code:[200 TO 299]",
                ),
                group_by=[
                    LogsMetricGroupBy(
                        path="@http.status_code",
                        tag_name="status_code",
                    ),
                ],
            ),
            type=LogsMetricType("logs_metrics"),
        ),
    )  # LogsMetricUpdateRequest | New definition of the log-based metric.

    # example passing only required values which don't have defaults set
    try:
        # Update a log-based metric
        api_response = api_instance.update_logs_metric(metric_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->update_logs_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| The name of the log-based metric. |
 **body** | [**LogsMetricUpdateRequest**](LogsMetricUpdateRequest.md)| New definition of the log-based metric. |

### Return type

[**LogsMetricResponse**](LogsMetricResponse.md)

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
**404** | Not Found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

