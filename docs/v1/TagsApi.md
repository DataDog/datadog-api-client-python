# datadog_api_client.v1.TagsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_tags**](TagsApi.md#create_host_tags) | **POST** /api/v1/tags/hosts/{host_name} | Add tags to a host
[**delete_host_tags**](TagsApi.md#delete_host_tags) | **DELETE** /api/v1/tags/hosts/{host_name} | Remove host tags
[**get_host_tags**](TagsApi.md#get_host_tags) | **GET** /api/v1/tags/hosts/{host_name} | Get host tags
[**list_host_tags**](TagsApi.md#list_host_tags) | **GET** /api/v1/tags/hosts | Get Tags
[**update_host_tags**](TagsApi.md#update_host_tags) | **PUT** /api/v1/tags/hosts/{host_name} | Update host tags


# **create_host_tags**
> HostTags create_host_tags(host_name, body)

Add tags to a host

This endpoint allows you to add new tags to a host, optionally specifying where these tags come from.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    host_name = "host_name_example" # str | This endpoint allows you to add new tags to a host, optionally specifying where the tags came from.
    body = HostTags(
        host="test.host",
        tags=[
            "environment:production",
        ],
    ) # HostTags | Update host tags request body.
    source = "chef" # str | The source of the tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add tags to a host
        api_response = api_instance.create_host_tags(host_name, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->create_host_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add tags to a host
        api_response = api_instance.create_host_tags(host_name, body, source=source)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->create_host_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| This endpoint allows you to add new tags to a host, optionally specifying where the tags came from. |
 **body** | [**HostTags**](HostTags.md)| Update host tags request body. |
 **source** | **str**| The source of the tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). | [optional]

### Return type

[**HostTags**](HostTags.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_host_tags**
> delete_host_tags(host_name)

Remove host tags

This endpoint allows you to remove all user-assigned tags for a single host.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    host_name = "host_name_example" # str | This endpoint allows you to remove all user-assigned tags for a single host.
    source = "source_example" # str | The source of the tags (e.g. chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove host tags
        api_instance.delete_host_tags(host_name)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->delete_host_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove host tags
        api_instance.delete_host_tags(host_name, source=source)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->delete_host_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| This endpoint allows you to remove all user-assigned tags for a single host. |
 **source** | **str**| The source of the tags (e.g. chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). | [optional]

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_host_tags**
> HostTags get_host_tags(host_name)

Get host tags

Return the list of tags that apply to a given host.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    host_name = "host_name_example" # str | When specified, filters list of tags to those tags with the specified source.
    source = "source_example" # str | Source to filter. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get host tags
        api_response = api_instance.get_host_tags(host_name)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->get_host_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get host tags
        api_response = api_instance.get_host_tags(host_name, source=source)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->get_host_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| When specified, filters list of tags to those tags with the specified source. |
 **source** | **str**| Source to filter. | [optional]

### Return type

[**HostTags**](HostTags.md)

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

# **list_host_tags**
> TagToHosts list_host_tags()

Get Tags

Return a mapping of tags to hosts for your whole infrastructure.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    source = "source_example" # str | When specified, filters host list to those tags with the specified source. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Tags
        api_response = api_instance.list_host_tags(source=source)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->list_host_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| When specified, filters host list to those tags with the specified source. | [optional]

### Return type

[**TagToHosts**](TagToHosts.md)

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

# **update_host_tags**
> HostTags update_host_tags(host_name, body)

Update host tags

This endpoint allows you to update/replace all tags in an integration source with those supplied in the request.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    host_name = "host_name_example" # str | This endpoint allows you to update/replace all in an integration source with those supplied in the request.
    body = HostTags(
        host="test.host",
        tags=[
            "environment:production",
        ],
    ) # HostTags | Add tags to host
    source = "source_example" # str | The source of the tags (e.g. chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update host tags
        api_response = api_instance.update_host_tags(host_name, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->update_host_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update host tags
        api_response = api_instance.update_host_tags(host_name, body, source=source)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling TagsApi->update_host_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| This endpoint allows you to update/replace all in an integration source with those supplied in the request. |
 **body** | [**HostTags**](HostTags.md)| Add tags to host |
 **source** | **str**| The source of the tags (e.g. chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value) | [optional]

### Return type

[**HostTags**](HostTags.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

