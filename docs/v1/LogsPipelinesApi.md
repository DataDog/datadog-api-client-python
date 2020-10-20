# datadog_api_client.v1.LogsPipelinesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logs_pipeline**](LogsPipelinesApi.md#create_logs_pipeline) | **POST** /api/v1/logs/config/pipelines | Create a pipeline
[**delete_logs_pipeline**](LogsPipelinesApi.md#delete_logs_pipeline) | **DELETE** /api/v1/logs/config/pipelines/{pipeline_id} | Delete a pipeline
[**get_logs_pipeline**](LogsPipelinesApi.md#get_logs_pipeline) | **GET** /api/v1/logs/config/pipelines/{pipeline_id} | Get a pipeline
[**get_logs_pipeline_order**](LogsPipelinesApi.md#get_logs_pipeline_order) | **GET** /api/v1/logs/config/pipeline-order | Get pipeline order
[**list_logs_pipelines**](LogsPipelinesApi.md#list_logs_pipelines) | **GET** /api/v1/logs/config/pipelines | Get all pipelines
[**update_logs_pipeline**](LogsPipelinesApi.md#update_logs_pipeline) | **PUT** /api/v1/logs/config/pipelines/{pipeline_id} | Update a pipeline
[**update_logs_pipeline_order**](LogsPipelinesApi.md#update_logs_pipeline_order) | **PUT** /api/v1/logs/config/pipeline-order | Update pipeline order


# **create_logs_pipeline**
> LogsPipeline create_logs_pipeline(body)

Create a pipeline

Create a pipeline in your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)
    body = LogsPipeline(
        filter=LogsFilter(
            query="source:python",
        ),
        id="id_example",
        is_enabled=True,
        is_read_only=True,
        name="name_example",
        processors=[
            LogsProcessor(),
        ],
        type="pipeline",
    ) # LogsPipeline | Definition of the new pipeline.

    # example passing only required values which don't have defaults set
    try:
        # Create a pipeline
        api_response = api_instance.create_logs_pipeline(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->create_logs_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsPipeline**](LogsPipeline.md)| Definition of the new pipeline. |

### Return type

[**LogsPipeline**](LogsPipeline.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_logs_pipeline**
> delete_logs_pipeline(pipeline_id)

Delete a pipeline

Delete a given pipeline from your organization. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)
    pipeline_id = "pipeline_id_example" # str | ID of the pipeline to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a pipeline
        api_instance.delete_logs_pipeline(pipeline_id)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->delete_logs_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| ID of the pipeline to delete. |

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_logs_pipeline**
> LogsPipeline get_logs_pipeline(pipeline_id)

Get a pipeline

Get a specific pipeline from your organization. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)
    pipeline_id = "pipeline_id_example" # str | ID of the pipeline to get.

    # example passing only required values which don't have defaults set
    try:
        # Get a pipeline
        api_response = api_instance.get_logs_pipeline(pipeline_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->get_logs_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| ID of the pipeline to get. |

### Return type

[**LogsPipeline**](LogsPipeline.md)

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

# **get_logs_pipeline_order**
> LogsPipelinesOrder get_logs_pipeline_order()

Get pipeline order

Get the current order of your pipelines. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get pipeline order
        api_response = api_instance.get_logs_pipeline_order()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->get_logs_pipeline_order: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsPipelinesOrder**](LogsPipelinesOrder.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs_pipelines**
> LogsPipelineList list_logs_pipelines()

Get all pipelines

Get all pipelines from your organization. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all pipelines
        api_response = api_instance.list_logs_pipelines()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->list_logs_pipelines: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsPipelineList**](LogsPipelineList.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_logs_pipeline**
> LogsPipeline update_logs_pipeline(pipeline_id, body)

Update a pipeline

Update a given pipeline configuration to change it’s processors or their order.  **Note**: Using this method updates your pipeline configuration by **replacing** your current configuration with the new one sent to your Datadog organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)
    pipeline_id = "pipeline_id_example" # str | ID of the pipeline to delete.
    body = LogsPipeline(
        filter=LogsFilter(
            query="source:python",
        ),
        id="id_example",
        is_enabled=True,
        is_read_only=True,
        name="name_example",
        processors=[
            LogsProcessor(),
        ],
        type="pipeline",
    ) # LogsPipeline | New definition of the pipeline.

    # example passing only required values which don't have defaults set
    try:
        # Update a pipeline
        api_response = api_instance.update_logs_pipeline(pipeline_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->update_logs_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| ID of the pipeline to delete. |
 **body** | [**LogsPipeline**](LogsPipeline.md)| New definition of the pipeline. |

### Return type

[**LogsPipeline**](LogsPipeline.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_logs_pipeline_order**
> LogsPipelinesOrder update_logs_pipeline_order(body)

Update pipeline order

Update the order of your pipelines. Since logs are processed sequentially, reordering a pipeline may change the structure and content of the data processed by other pipelines and their processors.  **Note**: Using the `PUT` method updates your pipeline order by replacing your current order with the new one sent to your Datadog organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import logs_pipelines_api
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
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)
    body = LogsPipelinesOrder(
        pipeline_ids=[
            "["tags","org_ids","products"]",
        ],
    ) # LogsPipelinesOrder | Object containing the new ordered list of pipeline IDs.

    # example passing only required values which don't have defaults set
    try:
        # Update pipeline order
        api_response = api_instance.update_logs_pipeline_order(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling LogsPipelinesApi->update_logs_pipeline_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsPipelinesOrder**](LogsPipelinesOrder.md)| Object containing the new ordered list of pipeline IDs. |

### Return type

[**LogsPipelinesOrder**](LogsPipelinesOrder.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

