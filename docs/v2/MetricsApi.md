# datadog_api_client.v2.MetricsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag_configuration**](MetricsApi.md#create_tag_configuration) | **POST** /api/v2/metrics/{metric_name}/tags | Create a tag configuration
[**delete_tag_configuration**](MetricsApi.md#delete_tag_configuration) | **DELETE** /api/v2/metrics/{metric_name}/tags | Delete a tag configuration
[**list_tag_configuration_by_name**](MetricsApi.md#list_tag_configuration_by_name) | **GET** /api/v2/metrics/{metric_name}/tags | List tag configuration by name
[**list_tag_configurations**](MetricsApi.md#list_tag_configurations) | **GET** /api/v2/metrics | List tag configurations
[**list_tags_by_metric_name**](MetricsApi.md#list_tags_by_metric_name) | **GET** /api/v2/metrics/{metric_name}/all-tags | List tags by metric name
[**list_volumes_by_metric_name**](MetricsApi.md#list_volumes_by_metric_name) | **GET** /api/v2/metrics/{metric_name}/volumes | List distinct metric volumes by metric name
[**update_tag_configuration**](MetricsApi.md#update_tag_configuration) | **PATCH** /api/v2/metrics/{metric_name}/tags | Update a tag configuration


# **create_tag_configuration**
> MetricTagConfigurationResponse create_tag_configuration(metric_name, body)

Create a tag configuration

Create and define a list of queryable tag keys for a count/gauge/rate/distribution metric. Optionally, include percentile aggregations on any distribution metric. Can only be used with application keys of users with the `Manage Tags for Metrics` permission.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["create_tag_configuration"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.
    body = MetricTagConfigurationCreateRequest(
        data=MetricTagConfigurationCreateData(
            attributes=MetricTagConfigurationCreateAttributes(
                include_percentiles=True,
                metric_type=MetricTagConfigurationMetricTypes("count"),
                tags=["app","datacenter"],
            ),
            id="test.metric.latency",
            type=MetricTagConfigurationType("manage_tags"),
        ),
    )  # MetricTagConfigurationCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a tag configuration
        api_response = api_instance.create_tag_configuration(metric_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->create_tag_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| The name of the metric. |
 **body** | [**MetricTagConfigurationCreateRequest**](MetricTagConfigurationCreateRequest.md)|  |

### Return type

[**MetricTagConfigurationResponse**](MetricTagConfigurationResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_tag_configuration**
> delete_tag_configuration(metric_name)

Delete a tag configuration

Deletes a metric's tag configuration. Can only be used with application keys from users with the `Manage Tags for Metrics` permission.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["delete_tag_configuration"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.

    # example passing only required values which don't have defaults set
    try:
        # Delete a tag configuration
        api_instance.delete_tag_configuration(metric_name)
    except ApiException as e:
        print("Exception when calling MetricsApi->delete_tag_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| The name of the metric. |

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
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_tag_configuration_by_name**
> MetricTagConfigurationResponse list_tag_configuration_by_name(metric_name)

List tag configuration by name

Returns the tag configuration for the given metric name.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["list_tag_configuration_by_name"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.

    # example passing only required values which don't have defaults set
    try:
        # List tag configuration by name
        api_response = api_instance.list_tag_configuration_by_name(metric_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_tag_configuration_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| The name of the metric. |

### Return type

[**MetricTagConfigurationResponse**](MetricTagConfigurationResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_tag_configurations**
> MetricsAndMetricTagConfigurationsResponse list_tag_configurations()

List tag configurations

Returns all configured count/gauge/rate/distribution metric names (with additional filters if specified).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["list_tag_configurations"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    filter_configured = True  # bool | Filter metrics that have configured tags. (optional)
    filter_tags_configured = "app"  # str | Filter tag configurations by configured tags. (optional)
    filter_metric_type = MetricTagConfigurationMetricTypes("count")  # MetricTagConfigurationMetricTypes | Filter tag configurations by metric type. (optional)
    filter_include_percentiles = True  # bool | Filter distributions with additional percentile aggregations enabled or disabled. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List tag configurations
        api_response = api_instance.list_tag_configurations(filter_configured=filter_configured, filter_tags_configured=filter_tags_configured, filter_metric_type=filter_metric_type, filter_include_percentiles=filter_include_percentiles)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_tag_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_configured** | **bool**| Filter metrics that have configured tags. | [optional]
 **filter_tags_configured** | **str**| Filter tag configurations by configured tags. | [optional]
 **filter_metric_type** | **MetricTagConfigurationMetricTypes**| Filter tag configurations by metric type. | [optional]
 **filter_include_percentiles** | **bool**| Filter distributions with additional percentile aggregations enabled or disabled. | [optional]

### Return type

[**MetricsAndMetricTagConfigurationsResponse**](MetricsAndMetricTagConfigurationsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_tags_by_metric_name**
> MetricAllTagsResponse list_tags_by_metric_name(metric_name)

List tags by metric name

View indexed tag key-value pairs for a given metric name.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["list_tags_by_metric_name"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.

    # example passing only required values which don't have defaults set
    try:
        # List tags by metric name
        api_response = api_instance.list_tags_by_metric_name(metric_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_tags_by_metric_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| The name of the metric. |

### Return type

[**MetricAllTagsResponse**](MetricAllTagsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_volumes_by_metric_name**
> MetricVolumesResponse list_volumes_by_metric_name(metric_name)

List distinct metric volumes by metric name

View distinct metrics volumes for the given metric name.  Custom distribution metrics will return both ingested and indexed custom metrics. For Metrics without Limits beta customers, all metrics will return both ingested/indexed volumes. Custom metrics generated in-app from other products will return `null` for ingested volumes.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["list_volumes_by_metric_name"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.

    # example passing only required values which don't have defaults set
    try:
        # List distinct metric volumes by metric name
        api_response = api_instance.list_volumes_by_metric_name(metric_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_volumes_by_metric_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| The name of the metric. |

### Return type

[**MetricVolumesResponse**](MetricVolumesResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_tag_configuration**
> MetricTagConfigurationResponse update_tag_configuration(metric_name, body)

Update a tag configuration

Update the tag configuration of a metric or percentile aggregations of a distribution metric. Can only be used with application keys from users with the `Manage Tags for Metrics` permission.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["update_tag_configuration"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.
    body = MetricTagConfigurationUpdateRequest(
        data=MetricTagConfigurationUpdateData(
            attributes=MetricTagConfigurationUpdateAttributes(
                include_percentiles=True,
                tags=["app","datacenter"],
            ),
            id="test.metric.latency",
            type=MetricTagConfigurationType("manage_tags"),
        ),
    )  # MetricTagConfigurationUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a tag configuration
        api_response = api_instance.update_tag_configuration(metric_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->update_tag_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | **str**| The name of the metric. |
 **body** | [**MetricTagConfigurationUpdateRequest**](MetricTagConfigurationUpdateRequest.md)|  |

### Return type

[**MetricTagConfigurationResponse**](MetricTagConfigurationResponse.md)

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
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

