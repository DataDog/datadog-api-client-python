# datadog_api_client.v1.SyntheticsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test**](SyntheticsApi.md#create_test) | **POST** /api/v1/synthetics/tests | Create a test
[**delete_tests**](SyntheticsApi.md#delete_tests) | **POST** /api/v1/synthetics/tests/delete | Delete tests
[**get_api_test_latest_results**](SyntheticsApi.md#get_api_test_latest_results) | **GET** /api/v1/synthetics/tests/{public_id}/results | Get the test&#39;s latest results summaries (API)
[**get_api_test_result**](SyntheticsApi.md#get_api_test_result) | **GET** /api/v1/synthetics/tests/{public_id}/results/{result_id} | Get a test result (API)
[**get_browser_test**](SyntheticsApi.md#get_browser_test) | **GET** /api/v1/synthetics/tests/browser/{public_id} | Get a browser test configuration
[**get_browser_test_latest_results**](SyntheticsApi.md#get_browser_test_latest_results) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results | Get the test&#39;s latest results summaries (browser)
[**get_browser_test_result**](SyntheticsApi.md#get_browser_test_result) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results/{result_id} | Get a test result (browser)
[**get_test**](SyntheticsApi.md#get_test) | **GET** /api/v1/synthetics/tests/{public_id} | Get a test configuration
[**list_tests**](SyntheticsApi.md#list_tests) | **GET** /api/v1/synthetics/tests | Get a list of tests
[**update_test**](SyntheticsApi.md#update_test) | **PUT** /api/v1/synthetics/tests/{public_id} | Edit a test
[**update_test_pause_status**](SyntheticsApi.md#update_test_pause_status) | **PUT** /api/v1/synthetics/tests/{public_id}/status | Pause or start a test


# **create_test**
> synthetics_test_details.SyntheticsTestDetails create_test(body)

Create a test

Create a Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_test_details
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = synthetics_test_details.SyntheticsTestDetails() # synthetics_test_details.SyntheticsTestDetails | Details of the test to create.
    
    # example passing only required values which don't have defaults set
    try:
        # Create a test
        api_response = api_instance.create_test(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->create_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**synthetics_test_details.SyntheticsTestDetails**](SyntheticsTestDetails.md)| Details of the test to create. |

### Return type

[**synthetics_test_details.SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Returns the created test details. |  -  |
**400** | - JSON format is wrong - Creation failed |  -  |
**402** | Test quota is reached |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tests**
> synthetics_delete_tests_response.SyntheticsDeleteTestsResponse delete_tests(body)

Delete tests

Delete multiple Synthetic tests by ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_delete_tests_payload
from datadog_api_client.v1.model import synthetics_delete_tests_response
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = synthetics_delete_tests_payload.SyntheticsDeleteTestsPayload() # synthetics_delete_tests_payload.SyntheticsDeleteTestsPayload | Public ID list of the Synthetic tests to be deleted.
    
    # example passing only required values which don't have defaults set
    try:
        # Delete tests
        api_response = api_instance.delete_tests(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->delete_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**synthetics_delete_tests_payload.SyntheticsDeleteTestsPayload**](SyntheticsDeleteTestsPayload.md)| Public ID list of the Synthetic tests to be deleted. |

### Return type

[**synthetics_delete_tests_response.SyntheticsDeleteTestsResponse**](SyntheticsDeleteTestsResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | - JSON format is wrong - Test cannot be deleted as it&#39;s used elsewhere (as a sub-test or in an uptime widget) - Some IDs are not owned by the user |  -  |
**403** | Forbidden |  -  |
**404** | - Tests to be deleted can&#39;t be found - Synthetics is not activated for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_test_latest_results**
> synthetics_get_api_test_latest_results_response.SyntheticsGetAPITestLatestResultsResponse get_api_test_latest_results(public_id)

Get the test's latest results summaries (API)

Get the last 50 test results summaries for a given Synthetics API test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import synthetics_get_api_test_latest_results_response
from datadog_api_client.v1.model import api_error_response
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the test for which to search results for.
    from_ts = 56 # int | Timestamp from which to start querying results. (optional)
to_ts = 56 # int | Timestamp up to which to query results. (optional)
probe_dc = ['probe_dc_example'] # [str] | Locations for which to query results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the test's latest results summaries (API)
        api_response = api_instance.get_api_test_latest_results(public_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_api_test_latest_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the test's latest results summaries (API)
        api_response = api_instance.get_api_test_latest_results(public_id, from_ts=from_ts, to_ts=to_ts, probe_dc=probe_dc)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_api_test_latest_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test for which to search results for. |
 **from_ts** | **int**| Timestamp from which to start querying results. | [optional]
 **to_ts** | **int**| Timestamp up to which to query results. | [optional]
 **probe_dc** | **[str]**| Locations for which to query results. | [optional]

### Return type

[**synthetics_get_api_test_latest_results_response.SyntheticsGetAPITestLatestResultsResponse**](SyntheticsGetAPITestLatestResultsResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_test_result**
> synthetics_api_test_result_full.SyntheticsAPITestResultFull get_api_test_result(public_id, result_id)

Get a test result (API)

Get a specific full result from a given (API) Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_api_test_result_full
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the API test to which the target result belongs.
    result_id = 'result_id_example' # str | The ID of the result to get.
    
    # example passing only required values which don't have defaults set
    try:
        # Get a test result (API)
        api_response = api_instance.get_api_test_result(public_id, result_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_api_test_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the API test to which the target result belongs. |
 **result_id** | **str**| The ID of the result to get. |

### Return type

[**synthetics_api_test_result_full.SyntheticsAPITestResultFull**](SyntheticsAPITestResultFull.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test or result is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browser_test**
> synthetics_test_details.SyntheticsTestDetails get_browser_test(public_id)

Get a browser test configuration

Get the detailed configuration (including steps) associated with a Synthetics browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_test_details
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the test to get details from.
    
    # example passing only required values which don't have defaults set
    try:
        # Get a browser test configuration
        api_response = api_instance.get_browser_test(public_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |

### Return type

[**synthetics_test_details.SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browser_test_latest_results**
> synthetics_get_browser_test_latest_results_response.SyntheticsGetBrowserTestLatestResultsResponse get_browser_test_latest_results(public_id)

Get the test's latest results summaries (browser)

Get the last 50 test results summaries for a given Synthetics Browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_get_browser_test_latest_results_response
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the browser test for which to search results for.
    from_ts = 56 # int | Timestamp from which to start querying results. (optional)
to_ts = 56 # int | Timestamp up to which to query results. (optional)
probe_dc = ['probe_dc_example'] # [str] | Locations for which to query results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the test's latest results summaries (browser)
        api_response = api_instance.get_browser_test_latest_results(public_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test_latest_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the test's latest results summaries (browser)
        api_response = api_instance.get_browser_test_latest_results(public_id, from_ts=from_ts, to_ts=to_ts, probe_dc=probe_dc)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test_latest_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the browser test for which to search results for. |
 **from_ts** | **int**| Timestamp from which to start querying results. | [optional]
 **to_ts** | **int**| Timestamp up to which to query results. | [optional]
 **probe_dc** | **[str]**| Locations for which to query results. | [optional]

### Return type

[**synthetics_get_browser_test_latest_results_response.SyntheticsGetBrowserTestLatestResultsResponse**](SyntheticsGetBrowserTestLatestResultsResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browser_test_result**
> synthetics_browser_test_result_full.SyntheticsBrowserTestResultFull get_browser_test_result(public_id, result_id)

Get a test result (browser)

Get a specific full result from a given (browser) Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_browser_test_result_full
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the browser test to which the target result belongs.
    result_id = 'result_id_example' # str | The ID of the result to get.
    
    # example passing only required values which don't have defaults set
    try:
        # Get a test result (browser)
        api_response = api_instance.get_browser_test_result(public_id, result_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the browser test to which the target result belongs. |
 **result_id** | **str**| The ID of the result to get. |

### Return type

[**synthetics_browser_test_result_full.SyntheticsBrowserTestResultFull**](SyntheticsBrowserTestResultFull.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test or result is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test**
> synthetics_test_details.SyntheticsTestDetails get_test(public_id)

Get a test configuration

Get the detailed configuration associated with a Synthetics test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_test_details
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the test to get details from.
    
    # example passing only required values which don't have defaults set
    try:
        # Get a test configuration
        api_response = api_instance.get_test(public_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |

### Return type

[**synthetics_test_details.SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tests**
> synthetics_list_tests_response.SyntheticsListTestsResponse list_tests()

Get a list of tests

Get the list of all Synthetic tests (can be filtered by type).

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_list_tests_response
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    check_type = 'check_type_example' # str | API or browser to filter the list by test type, undefined to get the unfiltered list. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of tests
        api_response = api_instance.list_tests(check_type=check_type)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->list_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_type** | **str**| API or browser to filter the list by test type, undefined to get the unfiltered list. | [optional]

### Return type

[**synthetics_list_tests_response.SyntheticsListTestsResponse**](SyntheticsListTestsResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Returns the list of all Synthetic tests (properly filtered by type). |  -  |
**403** | Forbidden |  -  |
**404** | Synthetics is not activated for the user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test**
> synthetics_test_details.SyntheticsTestDetails update_test(public_id, body)

Edit a test

Edit the configuration of a Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import api_error_response
from datadog_api_client.v1.model import synthetics_test_details
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the test to get details from.
    body = synthetics_test_details.SyntheticsTestDetails() # synthetics_test_details.SyntheticsTestDetails | New test details to be saved.
    
    # example passing only required values which don't have defaults set
    try:
        # Edit a test
        api_response = api_instance.update_test(public_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->update_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |
 **body** | [**synthetics_test_details.SyntheticsTestDetails**](SyntheticsTestDetails.md)| New test details to be saved. |

### Return type

[**synthetics_test_details.SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | - JSON format is wrong - Updating sub-type is forbidden |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user - Test can&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_pause_status**
> bool update_test_pause_status(public_id, body)

Pause or start a test

Pause or start a Synthetics test by changing the status.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
from __future__ import print_function
import time
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.model import synthetics_update_test_pause_status_payload
from datadog_api_client.v1.model import api_error_response
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
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'apiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure API key authorization: appKeyAuth
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com",
    api_key = {
        'appKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = 'public_id_example' # str | The public ID of the Synthetic test to update.
    body = synthetics_update_test_pause_status_payload.SyntheticsUpdateTestPauseStatusPayload() # synthetics_update_test_pause_status_payload.SyntheticsUpdateTestPauseStatusPayload | Status to set the given Synthetic test to.
    
    # example passing only required values which don't have defaults set
    try:
        # Pause or start a test
        api_response = api_instance.update_test_pause_status(public_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->update_test_pause_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the Synthetic test to update. |
 **body** | [**synthetics_update_test_pause_status_payload.SyntheticsUpdateTestPauseStatusPayload**](SyntheticsUpdateTestPauseStatusPayload.md)| Status to set the given Synthetic test to. |

### Return type

**bool**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [appKeyAuth](../README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Returns a boolean indicating if the update was successful. |  -  |
**400** | JSON format is wrong. |  -  |
**403** | Forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

