# datadog_api_client.v1.HostsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_host_totals**](HostsApi.md#get_host_totals) | **GET** /api/v1/hosts/totals | Get the total number of active hosts
[**list_hosts**](HostsApi.md#list_hosts) | **GET** /api/v1/hosts | Get all hosts for your organization
[**mute_host**](HostsApi.md#mute_host) | **POST** /api/v1/host/{host_name}/mute | Mute a host
[**unmute_host**](HostsApi.md#unmute_host) | **POST** /api/v1/host/{host_name}/unmute | Unmute a host


# **get_host_totals**
> HostTotals get_host_totals()

Get the total number of active hosts

This endpoint returns the total number of active and up hosts in your Datadog account. Active means the host has reported in the past hour, and up means it has reported in the past two hours.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import hosts_api
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
    api_instance = hosts_api.HostsApi(api_client)
    _from = 1 # int | Number of seconds from which you want to get total number of active hosts. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the total number of active hosts
        api_response = api_instance.get_host_totals(_from=_from)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling HostsApi->get_host_totals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Number of seconds from which you want to get total number of active hosts. | [optional]

### Return type

[**HostTotals**](HostTotals.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid Parameter Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_hosts**
> HostListResponse list_hosts()

Get all hosts for your organization

This endpoint allows searching for hosts by name, alias, or tag. Hosts live within the past 3 hours are included by default. Retention is 7 days. Results are paginated with a max of 1000 results at a time.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import hosts_api
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
    api_instance = hosts_api.HostsApi(api_client)
    filter = "filter_example" # str | String to filter search results. (optional)
    sort_field = "sort_field_example" # str | Sort hosts by this field. (optional)
    sort_dir = "sort_dir_example" # str | Direction of sort. Options include `asc` and `desc`. (optional)
    start = 1 # int | Host result to start search from. (optional)
    count = 1 # int | Number of hosts to return. Max 1000. (optional)
    _from = 1 # int | Number of seconds since UNIX epoch from which you want to search your hosts. (optional)
    include_muted_hosts_data = True # bool | Include information on the muted status of hosts and when the mute expires. (optional)
    include_hosts_metadata = True # bool | Include additional metadata about the hosts (agent_version, machine, platform, processor, etc.). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all hosts for your organization
        api_response = api_instance.list_hosts(filter=filter, sort_field=sort_field, sort_dir=sort_dir, start=start, count=count, _from=_from, include_muted_hosts_data=include_muted_hosts_data, include_hosts_metadata=include_hosts_metadata)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling HostsApi->list_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| String to filter search results. | [optional]
 **sort_field** | **str**| Sort hosts by this field. | [optional]
 **sort_dir** | **str**| Direction of sort. Options include &#x60;asc&#x60; and &#x60;desc&#x60;. | [optional]
 **start** | **int**| Host result to start search from. | [optional]
 **count** | **int**| Number of hosts to return. Max 1000. | [optional]
 **_from** | **int**| Number of seconds since UNIX epoch from which you want to search your hosts. | [optional]
 **include_muted_hosts_data** | **bool**| Include information on the muted status of hosts and when the mute expires. | [optional]
 **include_hosts_metadata** | **bool**| Include additional metadata about the hosts (agent_version, machine, platform, processor, etc.). | [optional]

### Return type

[**HostListResponse**](HostListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid Parameter Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **mute_host**
> HostMuteResponse mute_host(host_name)

Mute a host

Mute a host.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import hosts_api
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
    api_instance = hosts_api.HostsApi(api_client)
    host_name = "host_name_example" # str | Name of the host to mute.
    body = HostMuteSettings(
        end=1579098130,
        message="Muting this host for a test!",
        override=False,
    ) # HostMuteSettings | Mute a host request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute a host
        api_response = api_instance.mute_host(host_name)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling HostsApi->mute_host: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute a host
        api_response = api_instance.mute_host(host_name, body=body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling HostsApi->mute_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| Name of the host to mute. |
 **body** | [**HostMuteSettings**](HostMuteSettings.md)| Mute a host request body. | [optional]

### Return type

[**HostMuteResponse**](HostMuteResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid Parameter Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **unmute_host**
> HostMuteResponse unmute_host(host_name)

Unmute a host

Unmutes a host. This endpoint takes no JSON arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import hosts_api
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
    api_instance = hosts_api.HostsApi(api_client)
    host_name = "host_name_example" # str | Name of the host to unmute.

    # example passing only required values which don't have defaults set
    try:
        # Unmute a host
        api_response = api_instance.unmute_host(host_name)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling HostsApi->unmute_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| Name of the host to unmute. |

### Return type

[**HostMuteResponse**](HostMuteResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid Parameter Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

