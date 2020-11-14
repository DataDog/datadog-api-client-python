# datadog_api_client.v1.ServiceLevelObjectivesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_can_delete_slo**](ServiceLevelObjectivesApi.md#check_can_delete_slo) | **GET** /api/v1/slo/can_delete | Check if SLOs can be safely deleted
[**create_slo**](ServiceLevelObjectivesApi.md#create_slo) | **POST** /api/v1/slo | Create a SLO object
[**delete_slo**](ServiceLevelObjectivesApi.md#delete_slo) | **DELETE** /api/v1/slo/{slo_id} | Delete a SLO
[**delete_slo_timeframe_in_bulk**](ServiceLevelObjectivesApi.md#delete_slo_timeframe_in_bulk) | **POST** /api/v1/slo/bulk_delete | Bulk Delete SLO Timeframes
[**get_slo**](ServiceLevelObjectivesApi.md#get_slo) | **GET** /api/v1/slo/{slo_id} | Get a SLO&#39;s details
[**get_slo_history**](ServiceLevelObjectivesApi.md#get_slo_history) | **GET** /api/v1/slo/{slo_id}/history | Get an SLO&#39;s history
[**list_sl_os**](ServiceLevelObjectivesApi.md#list_sl_os) | **GET** /api/v1/slo | Search SLOs
[**update_slo**](ServiceLevelObjectivesApi.md#update_slo) | **PUT** /api/v1/slo/{slo_id} | Update a SLO


# **check_can_delete_slo**
> CheckCanDeleteSLOResponse check_can_delete_slo(ids)

Check if SLOs can be safely deleted

Check if a SLO can be safely deleted. For example, assure an SLO can be deleted without disrupting a dashboard.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    ids = "id1, id2, id3" # str | A comma separated list of the IDs of the service level objectives objects.

    # example passing only required values which don't have defaults set
    try:
        # Check if SLOs can be safely deleted
        api_response = api_instance.check_can_delete_slo(ids)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->check_can_delete_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| A comma separated list of the IDs of the service level objectives objects. |

### Return type

[**CheckCanDeleteSLOResponse**](CheckCanDeleteSLOResponse.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_slo**
> SLOListResponse create_slo(body)

Create a SLO object

Create a service level objective object.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    body = ServiceLevelObjectiveRequest(
        created_at=1,
        creator=Creator(
            email="email_example",
            handle="handle_example",
            name="name_example",
        ),
        description="description_example",
        groups=[
            "["env:prod","role:mysql"]",
        ],
        id="id_example",
        modified_at=1,
        monitor_ids=[
            1,
        ],
        name="name_example",
        query=ServiceLevelObjectiveQuery(
            denominator="denominator_example",
            numerator="numerator_example",
        ),
        tags=[
            "["env:prod","app:core"]",
        ],
        thresholds=[
            SLOThreshold(
                target=0.0,
                target_display="99.9",
                timeframe=SLOTimeframe("7d"),
                warning=3.14,
                warning_display="warning_display_example",
            ),
        ],
        type=SLOType("metric"),
    ) # ServiceLevelObjectiveRequest | Service level objective request object.

    # example passing only required values which don't have defaults set
    try:
        # Create a SLO object
        api_response = api_instance.create_slo(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->create_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceLevelObjectiveRequest**](ServiceLevelObjectiveRequest.md)| Service level objective request object. |

### Return type

[**SLOListResponse**](SLOListResponse.md)

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

# **delete_slo**
> SLODeleteResponse delete_slo(slo_id)

Delete a SLO

Permanently delete the specified service level objective object.  If an SLO is used in a dashboard, the `DELETE /v1/slo/` endpoint returns a 409 conflict error because the SLO is referenced in a dashboard.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    slo_id = "slo_id_example" # str | The ID of the service level objective.
    force = "force_example" # str | Delete the monitor even if it's referenced by other resources (e.g. SLO, composite monitor). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a SLO
        api_response = api_instance.delete_slo(slo_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->delete_slo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a SLO
        api_response = api_instance.delete_slo(slo_id, force=force)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->delete_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| The ID of the service level objective. |
 **force** | **str**| Delete the monitor even if it&#39;s referenced by other resources (e.g. SLO, composite monitor). | [optional]

### Return type

[**SLODeleteResponse**](SLODeleteResponse.md)

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
**404** | Not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_slo_timeframe_in_bulk**
> SLOBulkDeleteResponse delete_slo_timeframe_in_bulk(body)

Bulk Delete SLO Timeframes

Delete (or partially delete) multiple service level objective objects.  This endpoint facilitates deletion of one or more thresholds for one or more service level objective objects. If all thresholds are deleted, the service level objective object is deleted as well.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    body = SLOBulkDelete(
        "key": [
            SLOTimeframe("7d"),
        ],
    ) # SLOBulkDelete | Delete multiple service level objective objects request body.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Delete SLO Timeframes
        api_response = api_instance.delete_slo_timeframe_in_bulk(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->delete_slo_timeframe_in_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SLOBulkDelete**](SLOBulkDelete.md)| Delete multiple service level objective objects request body. |

### Return type

[**SLOBulkDeleteResponse**](SLOBulkDeleteResponse.md)

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

# **get_slo**
> SLOResponse get_slo(slo_id)

Get a SLO's details

Get a service level objective object.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    slo_id = "slo_id_example" # str | The ID of the service level objective object.

    # example passing only required values which don't have defaults set
    try:
        # Get a SLO's details
        api_response = api_instance.get_slo(slo_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->get_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| The ID of the service level objective object. |

### Return type

[**SLOResponse**](SLOResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_slo_history**
> SLOHistoryResponse get_slo_history(slo_id, from_ts, to_ts)

Get an SLO's history

Get a specific SLO’s history, regardless of its SLO type.  The detailed history data is structured according to the source data type. For example, metric data is included for event SLOs that use the metric source, and monitor SLO types include the monitor transition history.  **Note:** There are different response formats for event based and time based SLOs. Examples of both are shown.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    slo_id = "slo_id_example" # str | The ID of the service level objective object.
    from_ts = 1 # int | The `from` timestamp for the query window in epoch seconds.
    to_ts = 1 # int | The `to` timestamp for the query window in epoch seconds.

    # example passing only required values which don't have defaults set
    try:
        # Get an SLO's history
        api_response = api_instance.get_slo_history(slo_id, from_ts, to_ts)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->get_slo_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| The ID of the service level objective object. |
 **from_ts** | **int**| The &#x60;from&#x60; timestamp for the query window in epoch seconds. |
 **to_ts** | **int**| The &#x60;to&#x60; timestamp for the query window in epoch seconds. |

### Return type

[**SLOHistoryResponse**](SLOHistoryResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_sl_os**
> SLOListResponse list_sl_os(ids)

Search SLOs

Get multiple service level objective objects by their IDs.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    ids = "id1, id2, id3" # str | A comma separated list of the IDs of the service level objectives objects.

    # example passing only required values which don't have defaults set
    try:
        # Search SLOs
        api_response = api_instance.list_sl_os(ids)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->list_sl_os: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| A comma separated list of the IDs of the service level objectives objects. |

### Return type

[**SLOListResponse**](SLOListResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_slo**
> SLOListResponse update_slo(slo_id, body)

Update a SLO

Update the specified service level objective object.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import service_level_objectives_api
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
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    slo_id = "slo_id_example" # str | The ID of the service level objective object.
    body = ServiceLevelObjective(
        created_at=1,
        creator=Creator(
            email="email_example",
            handle="handle_example",
            name="name_example",
        ),
        description="description_example",
        groups=[
            "["env:prod","role:mysql"]",
        ],
        id="id_example",
        modified_at=1,
        monitor_ids=[
            1,
        ],
        monitor_tags=[
            "monitor_tags_example",
        ],
        name="name_example",
        query=ServiceLevelObjectiveQuery(
            denominator="denominator_example",
            numerator="numerator_example",
        ),
        tags=[
            "["env:prod","app:core"]",
        ],
        thresholds=[
            SLOThreshold(
                target=0.0,
                target_display="99.9",
                timeframe=SLOTimeframe("7d"),
                warning=3.14,
                warning_display="warning_display_example",
            ),
        ],
        type=SLOType("metric"),
    ) # ServiceLevelObjective | The edited service level objective request object.

    # example passing only required values which don't have defaults set
    try:
        # Update a SLO
        api_response = api_instance.update_slo(slo_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->update_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| The ID of the service level objective object. |
 **body** | [**ServiceLevelObjective**](ServiceLevelObjective.md)| The edited service level objective request object. |

### Return type

[**SLOListResponse**](SLOListResponse.md)

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

