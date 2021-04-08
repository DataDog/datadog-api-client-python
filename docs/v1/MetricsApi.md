# datadog_api_client.v1.MetricsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_metadata**](MetricsApi.md#get_metric_metadata) | **GET** /api/v1/metrics/{metric_name} | Get metric metadata
[**list_active_metrics**](MetricsApi.md#list_active_metrics) | **GET** /api/v1/metrics | Get active metrics list
[**list_metrics**](MetricsApi.md#list_metrics) | **GET** /api/v1/search | Search metrics
[**query_metrics**](MetricsApi.md#query_metrics) | **GET** /api/v1/query | Query timeseries points
[**submit_metrics**](MetricsApi.md#submit_metrics) | **POST** /api/v1/series | Submit metrics
[**update_metric_metadata**](MetricsApi.md#update_metric_metadata) | **PUT** /api/v1/metrics/{metric_name} | Edit metric metadata


# **get_metric_metadata**
> MetricMetadata get_metric_metadata(metric_name)

Get metric metadata

Get metadata about a specific metric.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "metric_name_example"  # str | Name of the metric for which to get metadata.

    # example passing only required values which don't have defaults set
    try:
        # Get metric metadata
        api_response = api_instance.get_metric_metadata(metric_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_metric_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| Name of the metric for which to get metadata. |

### Return type

[**MetricMetadata**](MetricMetadata.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_active_metrics**
> MetricsListResponse list_active_metrics(_from)

Get active metrics list

Get the list of actively reporting metrics from a given time until now.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    _from = 1  # int | Seconds since the Unix epoch.
    host = "host_example"  # str | Hostname for filtering the list of metrics returned. If set, metrics retrieved are those with the corresponding hostname tag. (optional)
    tag_filter = "env IN (staging,test) AND service:web"  # str | Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Cannot be combined with other filters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get active metrics list
        api_response = api_instance.list_active_metrics(_from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_active_metrics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get active metrics list
        api_response = api_instance.list_active_metrics(_from, host=host, tag_filter=tag_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_active_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Seconds since the Unix epoch. |
 **host** | **str**| Hostname for filtering the list of metrics returned. If set, metrics retrieved are those with the corresponding hostname tag. | [optional]
 **tag_filter** | **str**| Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Cannot be combined with other filters. | [optional]

### Return type

[**MetricsListResponse**](MetricsListResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_metrics**
> MetricSearchResponse list_metrics(q)

Search metrics

Search for metrics from the last 24 hours in Datadog.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    q = "q_example"  # str | Query string to search metrics upon. Must be prefixed with `metrics:`.

    # example passing only required values which don't have defaults set
    try:
        # Search metrics
        api_response = api_instance.list_metrics(q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query string to search metrics upon. Must be prefixed with &#x60;metrics:&#x60;. |

### Return type

[**MetricSearchResponse**](MetricSearchResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **query_metrics**
> MetricsQueryResponse query_metrics(_from, to, query)

Query timeseries points

Query timeseries points.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    _from = 1  # int | Start of the queried time period, seconds since the Unix epoch.
    to = 1  # int | End of the queried time period, seconds since the Unix epoch.
    query = "query_example"  # str | Query string.

    # example passing only required values which don't have defaults set
    try:
        # Query timeseries points
        api_response = api_instance.query_metrics(_from, to, query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->query_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Start of the queried time period, seconds since the Unix epoch. |
 **to** | **int**| End of the queried time period, seconds since the Unix epoch. |
 **query** | **str**| Query string. |

### Return type

[**MetricsQueryResponse**](MetricsQueryResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **submit_metrics**
> IntakePayloadAccepted submit_metrics(body)

Submit metrics

The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards. The maximum payload size is 3.2 megabytes (3200000). Compressed payloads must have a decompressed size of up to 62 megabytes (62914560).  If you’re submitting metrics directly to the Datadog API without using DogStatsD, expect  - 64 bits for the timestamp - 32 bits for the value - 20 bytes for the metric names - 50 bytes for the timeseries - The full payload is approximately ~ 100 bytes. However, with the DogStatsD API, compression is applied, which reduces the payload size.

### Example

* Api Key Authentication (apiKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    body = MetricsPayload(
        series=[
            Series(
                host="test.example.com",
                interval=20,
                metric="system.load.1",
                points=[
                    Point([[1575317847,0.5]]),
                ],
                tags=["environment:test"],
                type="rate",
            ),
        ],
    )  # MetricsPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Submit metrics
        api_response = api_instance.submit_metrics(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->submit_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricsPayload**](MetricsPayload.md)|  |

### Return type

[**IntakePayloadAccepted**](IntakePayloadAccepted.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Payload accepted |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |
**408** | Request timeout |  -  |
**413** | Payload too large |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_metric_metadata**
> MetricMetadata update_metric_metadata(metric_name, body)

Edit metric metadata

Edit metadata of a specific metric. Find out more about [supported types](https://docs.datadoghq.com/developers/metrics).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "metric_name_example"  # str | Name of the metric for which to edit metadata.
    body = MetricMetadata(
        description="description_example",
        integration="integration_example",
        per_unit="second",
        short_name="short_name_example",
        statsd_interval=1,
        type="count",
        unit="byte",
    )  # MetricMetadata | New metadata.

    # example passing only required values which don't have defaults set
    try:
        # Edit metric metadata
        api_response = api_instance.update_metric_metadata(metric_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->update_metric_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| Name of the metric for which to edit metadata. |
 **body** | [**MetricMetadata**](MetricMetadata.md)| New metadata. |

### Return type

[**MetricMetadata**](MetricMetadata.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

