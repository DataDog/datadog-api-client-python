# datadog_api_client.v1.DashboardsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /api/v1/dashboard | Create a new dashboard
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /api/v1/dashboard/{dashboard_id} | Delete a dashboard
[**delete_dashboards**](DashboardsApi.md#delete_dashboards) | **DELETE** /api/v1/dashboard | Delete dashboards
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /api/v1/dashboard/{dashboard_id} | Get a dashboard
[**list_dashboards**](DashboardsApi.md#list_dashboards) | **GET** /api/v1/dashboard | Get all dashboards
[**restore_dashboards**](DashboardsApi.md#restore_dashboards) | **PATCH** /api/v1/dashboard | Restore deleted dashboards
[**update_dashboard**](DashboardsApi.md#update_dashboard) | **PUT** /api/v1/dashboard/{dashboard_id} | Update a dashboard


# **create_dashboard**
> Dashboard create_dashboard(body)

Create a dashboard using the specified options. When defining queries in your widgets, take note of which queries should have the `as_count()` or `as_rate()` modifiers appended.
Refer to the following [documentation](https://docs.datadoghq.com/developers/metrics/type_modifiers/?tab=count#in-application-modifiers) for more information on these modifiers.

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    body = Dashboard(
        description="description_example",
        is_read_only=False,
        layout_type=DashboardLayoutType("ordered"),
        notify_list=[
            "notify_list_example",
        ],
        reflow_type=DashboardReflowType("auto"),
        restricted_roles=[
            "restricted_roles_example",
        ],
        template_variable_presets=[
            DashboardTemplateVariablePreset(
                name="name_example",
                template_variables=[
                    DashboardTemplateVariablePresetValue(
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
        template_variables=[
            DashboardTemplateVariable(
                available_values=["my-host","host1","host2"],
                default="my-host",
                name="host1",
                prefix="host",
            ),
        ],
        title="",
        widgets=[
            Widget(
                definition=WidgetDefinition(),
                id=1,
                layout=WidgetLayout(
                    height=0,
                    is_column_break=True,
                    width=0,
                    x=0,
                    y=0,
                ),
            ),
        ],
    )  # Dashboard | Create a dashboard request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a new dashboard
        api_response = api_instance.create_dashboard(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| Create a dashboard request body. |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_dashboard**
> DashboardDeleteResponse delete_dashboard(dashboard_id)

Delete a dashboard using the specified ID.

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = "dashboard_id_example"  # str | The ID of the dashboard.

    # example passing only required values which don't have defaults set
    try:
        # Delete a dashboard
        api_response = api_instance.delete_dashboard(dashboard_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->delete_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The ID of the dashboard. |

### Return type

[**DashboardDeleteResponse**](DashboardDeleteResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication Error |  -  |
**404** | Dashboards Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_dashboards**
> delete_dashboards(body)

Delete dashboards using the specified IDs. If there are any failures, no dashboards will be deleted (partial success is not allowed).

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    body = DashboardBulkDeleteRequest(
        data=DashboardBulkActionDataList([
            DashboardBulkActionData(
                id="123-abc-456",
                type=DashboardResourceType("dashboard"),
            ),
        ]),
    )  # DashboardBulkDeleteRequest | Delete dashboards request body.

    # example passing only required values which don't have defaults set
    try:
        # Delete dashboards
        api_instance.delete_dashboards(body)
    except ApiException as e:
        print("Exception when calling DashboardsApi->delete_dashboards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardBulkDeleteRequest**](DashboardBulkDeleteRequest.md)| Delete dashboards request body. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Dashboards Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_dashboard**
> Dashboard get_dashboard(dashboard_id)

Get a dashboard using the specified ID.

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = "dashboard_id_example"  # str | The ID of the dashboard.

    # example passing only required values which don't have defaults set
    try:
        # Get a dashboard
        api_response = api_instance.get_dashboard(dashboard_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The ID of the dashboard. |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication Error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_dashboards**
> DashboardSummary list_dashboards()

Get all dashboards.

**Note**: This query will only return custom created or cloned dashboards.
This query will not return preset dashboards.

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    filter_shared = True  # bool | When `true`, this query only returns shared custom created or cloned dashboards. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all dashboards
        api_response = api_instance.list_dashboards(filter_shared=filter_shared)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->list_dashboards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_shared** | **bool**| When &#x60;true&#x60;, this query only returns shared custom created or cloned dashboards. | [optional]

### Return type

[**DashboardSummary**](DashboardSummary.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **restore_dashboards**
> restore_dashboards(body)

Restore dashboards using the specified IDs. If there are any failures, no dashboards will be restored (partial success is not allowed).

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    body = DashboardRestoreRequest(
        data=DashboardBulkActionDataList([
            DashboardBulkActionData(
                id="123-abc-456",
                type=DashboardResourceType("dashboard"),
            ),
        ]),
    )  # DashboardRestoreRequest | Restore dashboards request body.

    # example passing only required values which don't have defaults set
    try:
        # Restore deleted dashboards
        api_instance.restore_dashboards(body)
    except ApiException as e:
        print("Exception when calling DashboardsApi->restore_dashboards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardRestoreRequest**](DashboardRestoreRequest.md)| Restore dashboards request body. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Dashboards Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_dashboard**
> Dashboard update_dashboard(dashboard_id, body)

Update a dashboard using the specified ID.

### Example

* OAuth Authentication (AuthZ):
* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = "dashboard_id_example"  # str | The ID of the dashboard.
    body = Dashboard(
        description="description_example",
        is_read_only=False,
        layout_type=DashboardLayoutType("ordered"),
        notify_list=[
            "notify_list_example",
        ],
        reflow_type=DashboardReflowType("auto"),
        restricted_roles=[
            "restricted_roles_example",
        ],
        template_variable_presets=[
            DashboardTemplateVariablePreset(
                name="name_example",
                template_variables=[
                    DashboardTemplateVariablePresetValue(
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
        template_variables=[
            DashboardTemplateVariable(
                available_values=["my-host","host1","host2"],
                default="my-host",
                name="host1",
                prefix="host",
            ),
        ],
        title="",
        widgets=[
            Widget(
                definition=WidgetDefinition(),
                id=1,
                layout=WidgetLayout(
                    height=0,
                    is_column_break=True,
                    width=0,
                    x=0,
                    y=0,
                ),
            ),
        ],
    )  # Dashboard | Update Dashboard request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a dashboard
        api_response = api_instance.update_dashboard(dashboard_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->update_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The ID of the dashboard. |
 **body** | [**Dashboard**](Dashboard.md)| Update Dashboard request body. |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication Error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

