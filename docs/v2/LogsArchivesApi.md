# datadog_api_client.v2.LogsArchivesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_read_role_to_archive**](LogsArchivesApi.md#add_read_role_to_archive) | **POST** /api/v2/logs/config/archives/{archive_id}/readers | Grant role to an archive
[**create_logs_archive**](LogsArchivesApi.md#create_logs_archive) | **POST** /api/v2/logs/config/archives | Create an archive
[**delete_logs_archive**](LogsArchivesApi.md#delete_logs_archive) | **DELETE** /api/v2/logs/config/archives/{archive_id} | Delete an archive
[**get_logs_archive**](LogsArchivesApi.md#get_logs_archive) | **GET** /api/v2/logs/config/archives/{archive_id} | Get an archive
[**get_logs_archive_order**](LogsArchivesApi.md#get_logs_archive_order) | **GET** /api/v2/logs/config/archive-order | Get archive order
[**list_archive_read_roles**](LogsArchivesApi.md#list_archive_read_roles) | **GET** /api/v2/logs/config/archives/{archive_id}/readers | List read roles for an archive
[**list_logs_archives**](LogsArchivesApi.md#list_logs_archives) | **GET** /api/v2/logs/config/archives | Get all archives
[**remove_role_from_archive**](LogsArchivesApi.md#remove_role_from_archive) | **DELETE** /api/v2/logs/config/archives/{archive_id}/readers | Revoke role from an archive
[**update_logs_archive**](LogsArchivesApi.md#update_logs_archive) | **PUT** /api/v2/logs/config/archives/{archive_id} | Update an archive
[**update_logs_archive_order**](LogsArchivesApi.md#update_logs_archive_order) | **PUT** /api/v2/logs/config/archive-order | Update archive order


# **add_read_role_to_archive**
> add_read_role_to_archive(archive_id)

Grant role to an archive

Adds a read role to an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/))

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example" # str | The ID of the archive.
    body = RelationshipToRole(
        data=RelationshipToRoleData(
            id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            type=RolesType("roles"),
        ),
    ) # RelationshipToRole |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Grant role to an archive
        api_instance.add_read_role_to_archive(archive_id)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->add_read_role_to_archive: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Grant role to an archive
        api_instance.add_read_role_to_archive(archive_id, body=body)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->add_read_role_to_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_id** | **str**| The ID of the archive. |
 **body** | [**RelationshipToRole**](RelationshipToRole.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_logs_archive**
> LogsArchive create_logs_archive(body)

Create an archive

Create an archive in your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    body = LogsArchiveCreateRequest(
        data=LogsArchiveCreateRequestDefinition(
            attributes=LogsArchiveCreateRequestAttributes(
                destination=LogsArchiveCreateRequestDestination(),
                include_tags=False,
                name="Nginx Archive",
                query="source:nginx",
                rehydration_tags=[
                    "["team:intake","team:app"]",
                ],
            ),
            type="archives",
        ),
    ) # LogsArchiveCreateRequest | The definition of the new archive.

    # example passing only required values which don't have defaults set
    try:
        # Create an archive
        api_response = api_instance.create_logs_archive(body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->create_logs_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsArchiveCreateRequest**](LogsArchiveCreateRequest.md)| The definition of the new archive. |

### Return type

[**LogsArchive**](LogsArchive.md)

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

# **delete_logs_archive**
> delete_logs_archive(archive_id)

Delete an archive

Delete a given archive from your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example" # str | The ID of the archive.

    # example passing only required values which don't have defaults set
    try:
        # Delete an archive
        api_instance.delete_logs_archive(archive_id)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->delete_logs_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_id** | **str**| The ID of the archive. |

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_logs_archive**
> LogsArchive get_logs_archive(archive_id)

Get an archive

Get a specific archive from your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example" # str | The ID of the archive.

    # example passing only required values which don't have defaults set
    try:
        # Get an archive
        api_response = api_instance.get_logs_archive(archive_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->get_logs_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_id** | **str**| The ID of the archive. |

### Return type

[**LogsArchive**](LogsArchive.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_logs_archive_order**
> LogsArchiveOrder get_logs_archive_order()

Get archive order

Get the current order of your archives. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get archive order
        api_response = api_instance.get_logs_archive_order()
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->get_logs_archive_order: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsArchiveOrder**](LogsArchiveOrder.md)

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

# **list_archive_read_roles**
> RolesResponse list_archive_read_roles(archive_id)

List read roles for an archive

Returns all read roles a given archive is restricted to.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example" # str | The ID of the archive.

    # example passing only required values which don't have defaults set
    try:
        # List read roles for an archive
        api_response = api_instance.list_archive_read_roles(archive_id)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->list_archive_read_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_id** | **str**| The ID of the archive. |

### Return type

[**RolesResponse**](RolesResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_logs_archives**
> LogsArchives list_logs_archives()

Get all archives

Get the list of configured logs archives with their definitions.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all archives
        api_response = api_instance.list_logs_archives()
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->list_logs_archives: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogsArchives**](LogsArchives.md)

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

# **remove_role_from_archive**
> remove_role_from_archive(archive_id)

Revoke role from an archive

Removes a role from an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/))

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example" # str | The ID of the archive.
    body = RelationshipToRole(
        data=RelationshipToRoleData(
            id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            type=RolesType("roles"),
        ),
    ) # RelationshipToRole |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Revoke role from an archive
        api_instance.remove_role_from_archive(archive_id)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->remove_role_from_archive: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Revoke role from an archive
        api_instance.remove_role_from_archive(archive_id, body=body)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->remove_role_from_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_id** | **str**| The ID of the archive. |
 **body** | [**RelationshipToRole**](RelationshipToRole.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_logs_archive**
> LogsArchive update_logs_archive(archive_id, body)

Update an archive

Update a given archive configuration.  **Note**: Using this method updates your archive configuration by **replacing** your current configuration with the new one sent to your Datadog organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example" # str | The ID of the archive.
    body = LogsArchiveCreateRequest(
        data=LogsArchiveCreateRequestDefinition(
            attributes=LogsArchiveCreateRequestAttributes(
                destination=LogsArchiveCreateRequestDestination(),
                include_tags=False,
                name="Nginx Archive",
                query="source:nginx",
                rehydration_tags=[
                    "["team:intake","team:app"]",
                ],
            ),
            type="archives",
        ),
    ) # LogsArchiveCreateRequest | New definition of the archive.

    # example passing only required values which don't have defaults set
    try:
        # Update an archive
        api_response = api_instance.update_logs_archive(archive_id, body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->update_logs_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_id** | **str**| The ID of the archive. |
 **body** | [**LogsArchiveCreateRequest**](LogsArchiveCreateRequest.md)| New definition of the archive. |

### Return type

[**LogsArchive**](LogsArchive.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_logs_archive_order**
> LogsArchiveOrder update_logs_archive_order(body)

Update archive order

Update the order of your archives. Since logs are processed sequentially, reordering an archive may change the structure and content of the data processed by other archives.  **Note**: Using the `PUT` method updates your archive's order by replacing the current order with the new one.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v2
from datadog_api_client.v2.api import logs_archives_api
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
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    body = LogsArchiveOrder(
        data=LogsArchiveOrderDefinition(
            attributes=LogsArchiveOrderAttributes(
                archive_ids=[
                    "["a2zcMylnM4OCHpYusxIi1g","a2zcMylnM4OCHpYusxIi2g","a2zcMylnM4OCHpYusxIi3g"]",
                ],
            ),
            type=LogsArchiveOrderDefinitionType("archive_order"),
        ),
    ) # LogsArchiveOrder | An object containing the new ordered list of archive IDs.

    # example passing only required values which don't have defaults set
    try:
        # Update archive order
        api_response = api_instance.update_logs_archive_order(body)
        pprint(api_response)
    except datadog_api_client.v2.ApiException as e:
        print("Exception when calling LogsArchivesApi->update_logs_archive_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogsArchiveOrder**](LogsArchiveOrder.md)| An object containing the new ordered list of archive IDs. |

### Return type

[**LogsArchiveOrder**](LogsArchiveOrder.md)

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

