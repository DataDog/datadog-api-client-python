# datadog_api_client.v1.NotebooksApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notebook**](NotebooksApi.md#create_notebook) | **POST** /api/v1/notebooks | Create a notebook
[**delete_notebook**](NotebooksApi.md#delete_notebook) | **DELETE** /api/v1/notebooks/{notebook_id} | Delete a notebook
[**get_notebook**](NotebooksApi.md#get_notebook) | **GET** /api/v1/notebooks/{notebook_id} | Get a notebook
[**list_notebooks**](NotebooksApi.md#list_notebooks) | **GET** /api/v1/notebooks | Get all notebooks
[**update_notebook**](NotebooksApi.md#update_notebook) | **PUT** /api/v1/notebooks/{notebook_id} | Update a notebook


# **create_notebook**
> NotebookResponse create_notebook(body)

Create a notebook

Create a notebook using the specified options.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    body = NotebookCreateRequest(
        data=NotebookCreateData(
            attributes=NotebookCreateDataAttributes(
                cells=[
                    NotebookCellCreateRequest(
                        attributes=NotebookCellCreateRequestAttributes(),
                        type=NotebookCellResourceType("notebook_cells"),
                    ),
                ],
                name="Example Notebook",
                status=NotebookStatus("published"),
                time=NotebookGlobalTime(),
            ),
            type=NotebookResourceType("notebooks"),
        ),
    )  # NotebookCreateRequest | The JSON description of the notebook you want to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a notebook
        api_response = api_instance.create_notebook(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotebooksApi->create_notebook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotebookCreateRequest**](NotebookCreateRequest.md)| The JSON description of the notebook you want to create. |

### Return type

[**NotebookResponse**](NotebookResponse.md)

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_notebook**
> delete_notebook(notebook_id)

Delete a notebook

Delete a notebook using the specified ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    notebook_id = 1  # int | Unique ID, assigned when you create the notebook.

    # example passing only required values which don't have defaults set
    try:
        # Delete a notebook
        api_instance.delete_notebook(notebook_id)
    except ApiException as e:
        print("Exception when calling NotebooksApi->delete_notebook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_id** | **int**| Unique ID, assigned when you create the notebook. |

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
**400** | Bad Request |  -  |
**403** | Authentication Error |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_notebook**
> NotebookResponse get_notebook(notebook_id)

Get a notebook

Get a notebook using the specified notebook ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    notebook_id = 1  # int | Unique ID, assigned when you create the notebook.

    # example passing only required values which don't have defaults set
    try:
        # Get a notebook
        api_response = api_instance.get_notebook(notebook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotebooksApi->get_notebook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_id** | **int**| Unique ID, assigned when you create the notebook. |

### Return type

[**NotebookResponse**](NotebookResponse.md)

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
**403** | Authentication Error |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_notebooks**
> NotebooksResponse list_notebooks()

Get all notebooks

Get all notebooks. This can also be used to search for notebooks with a particular `query` in the notebook `name` or author `handle`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    author_handle = "test@datadoghq.com"  # str | Return notebooks created by the given `author_handle`. (optional)
    exclude_author_handle = "test@datadoghq.com"  # str | Return notebooks not created by the given `author_handle`. (optional)
    start = 0  # int | The index of the first notebook you want returned. (optional)
    count = 5  # int | The number of notebooks to be returned. (optional)
    sort_field = "modified"  # str | Sort by field `modified` or `name`. (optional) if omitted the server will use the default value of "modified"
    sort_dir = "desc"  # str | Sort by direction `asc` or `desc`. (optional) if omitted the server will use the default value of "desc"
    query = "postmortem"  # str | Return only notebooks with `query` string in notebook name or author handle. (optional)
    include_cells = False  # bool | Value of `false` excludes the `cells` and global `time` for each notebook. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all notebooks
        api_response = api_instance.list_notebooks(author_handle=author_handle, exclude_author_handle=exclude_author_handle, start=start, count=count, sort_field=sort_field, sort_dir=sort_dir, query=query, include_cells=include_cells)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotebooksApi->list_notebooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_handle** | **str**| Return notebooks created by the given &#x60;author_handle&#x60;. | [optional]
 **exclude_author_handle** | **str**| Return notebooks not created by the given &#x60;author_handle&#x60;. | [optional]
 **start** | **int**| The index of the first notebook you want returned. | [optional]
 **count** | **int**| The number of notebooks to be returned. | [optional]
 **sort_field** | **str**| Sort by field &#x60;modified&#x60; or &#x60;name&#x60;. | [optional] if omitted the server will use the default value of "modified"
 **sort_dir** | **str**| Sort by direction &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] if omitted the server will use the default value of "desc"
 **query** | **str**| Return only notebooks with &#x60;query&#x60; string in notebook name or author handle. | [optional]
 **include_cells** | **bool**| Value of &#x60;false&#x60; excludes the &#x60;cells&#x60; and global &#x60;time&#x60; for each notebook. | [optional] if omitted the server will use the default value of True

### Return type

[**NotebooksResponse**](NotebooksResponse.md)

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
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_notebook**
> NotebookResponse update_notebook(notebook_id, body)

Update a notebook

Update a notebook using the specified ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    notebook_id = 1  # int | Unique ID, assigned when you create the notebook.
    body = NotebookUpdateRequest(
        data=NotebookUpdateData(
            attributes=NotebookUpdateDataAttributes(
                cells=[
                    NotebookUpdateCell(),
                ],
                name="Example Notebook",
                status=NotebookStatus("published"),
                time=NotebookGlobalTime(),
            ),
            type=NotebookResourceType("notebooks"),
        ),
    )  # NotebookUpdateRequest | Update notebook request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a notebook
        api_response = api_instance.update_notebook(notebook_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotebooksApi->update_notebook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_id** | **int**| Unique ID, assigned when you create the notebook. |
 **body** | [**NotebookUpdateRequest**](NotebookUpdateRequest.md)| Update notebook request body. |

### Return type

[**NotebookResponse**](NotebookResponse.md)

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
**403** | Authentication Error |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

