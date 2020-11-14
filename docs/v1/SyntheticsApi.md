# datadog_api_client.v1.SyntheticsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_variable**](SyntheticsApi.md#create_global_variable) | **POST** /api/v1/synthetics/variables | Create a global variable
[**create_test**](SyntheticsApi.md#create_test) | **POST** /api/v1/synthetics/tests | Create a test
[**delete_global_variable**](SyntheticsApi.md#delete_global_variable) | **DELETE** /api/v1/synthetics/variables/{variable_id} | Delete a global variable
[**delete_tests**](SyntheticsApi.md#delete_tests) | **POST** /api/v1/synthetics/tests/delete | Delete tests
[**edit_global_variable**](SyntheticsApi.md#edit_global_variable) | **PUT** /api/v1/synthetics/variables/{variable_id} | Edit a global variable
[**get_api_test_latest_results**](SyntheticsApi.md#get_api_test_latest_results) | **GET** /api/v1/synthetics/tests/{public_id}/results | Get the test&#39;s latest results summaries (API)
[**get_api_test_result**](SyntheticsApi.md#get_api_test_result) | **GET** /api/v1/synthetics/tests/{public_id}/results/{result_id} | Get a test result (API)
[**get_browser_test**](SyntheticsApi.md#get_browser_test) | **GET** /api/v1/synthetics/tests/browser/{public_id} | Get a test configuration (browser)
[**get_browser_test_latest_results**](SyntheticsApi.md#get_browser_test_latest_results) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results | Get the test&#39;s latest results summaries (browser)
[**get_browser_test_result**](SyntheticsApi.md#get_browser_test_result) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results/{result_id} | Get a test result (browser)
[**get_global_variable**](SyntheticsApi.md#get_global_variable) | **GET** /api/v1/synthetics/variables/{variable_id} | Get a global variable
[**get_test**](SyntheticsApi.md#get_test) | **GET** /api/v1/synthetics/tests/{public_id} | Get a test configuration (API)
[**list_locations**](SyntheticsApi.md#list_locations) | **GET** /api/v1/synthetics/locations | Get all locations (public and private)
[**list_tests**](SyntheticsApi.md#list_tests) | **GET** /api/v1/synthetics/tests | Get the list of all tests
[**trigger_ci_tests**](SyntheticsApi.md#trigger_ci_tests) | **POST** /api/v1/synthetics/tests/trigger/ci | Trigger some Synthetics tests for CI
[**update_test**](SyntheticsApi.md#update_test) | **PUT** /api/v1/synthetics/tests/{public_id} | Edit a test
[**update_test_pause_status**](SyntheticsApi.md#update_test_pause_status) | **PUT** /api/v1/synthetics/tests/{public_id}/status | Pause or start a test


# **create_global_variable**
> SyntheticsGlobalVariable create_global_variable(body)

Create a global variable

Create a Synthetics global variable.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsGlobalVariable(
        description="Example description",
        id="id_example",
        name="MY_VARIABLE",
        tags=[
            "["team:front","test:workflow-1"]",
        ],
        value=SyntheticsGlobalVariableValue(
            secure=True,
            value="example-value",
        ),
    ) # SyntheticsGlobalVariable | Details of the global variable to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a global variable
        api_response = api_instance.create_global_variable(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->create_global_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)| Details of the global variable to create. |

### Return type

[**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_test**
> SyntheticsTestDetails create_test(body)

Create a test

Create a Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsTestDetails(
        config=SyntheticsTestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            request=SyntheticsTestRequest(
                basic_auth=SyntheticsBasicAuth(
                    password="password_example",
                    username="username_example",
                ),
                body="body_example",
                certificate=SyntheticsTestRequestCertificate(
                    cert=SyntheticsTestRequestCertificateItem(
                        content="content_example",
                        filename="filename_example",
                        updated_at="updated_at_example",
                    ),
                    key=SyntheticsTestRequestCertificateItem(
                        content="content_example",
                        filename="filename_example",
                        updated_at="updated_at_example",
                    ),
                ),
                dns_server="dns_server_example",
                headers=SyntheticsTestHeaders(
                    "key": "key_example",
                ),
                host="host_example",
                method=HTTPMethod("GET"),
                port=1,
                query={},
                timeout=3.14,
                url="url_example",
            ),
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="name_example",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("element"),
                ),
            ],
        ),
        locations=[
            "locations_example",
        ],
        message="message_example",
        monitor_id=1,
        name="name_example",
        options=SyntheticsTestOptions(
            accept_self_signed=True,
            allow_insecure=True,
            device_ids=[
                SyntheticsDeviceID("laptop_large"),
            ],
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=SyntheticsTickInterval(60),
        ),
        public_id="public_id_example",
        status=SyntheticsTestPauseStatus("live"),
        steps=[
            SyntheticsStep(
                allow_failure=True,
                name="name_example",
                params={},
                timeout=3.14,
                type=SyntheticsStepType("assertCurrentUrl"),
            ),
        ],
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=[
            "tags_example",
        ],
        type=SyntheticsTestDetailsType("api"),
    ) # SyntheticsTestDetails | Details of the test to create.

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
 **body** | [**SyntheticsTestDetails**](SyntheticsTestDetails.md)| Details of the test to create. |

### Return type

[**SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_global_variable**
> delete_global_variable(variable_id)

Delete a global variable

Delete a Synthetics global variable.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example" # str | The ID of the global variable.

    # example passing only required values which don't have defaults set
    try:
        # Delete a global variable
        api_instance.delete_global_variable(variable_id)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->delete_global_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| The ID of the global variable. |

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
**400** | JSON format is wrong |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_tests**
> SyntheticsDeleteTestsResponse delete_tests(body)

Delete tests

Delete multiple Synthetic tests by ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsDeleteTestsPayload(
        public_ids=[
            "[]",
        ],
    ) # SyntheticsDeleteTestsPayload | Public ID list of the Synthetic tests to be deleted.

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
 **body** | [**SyntheticsDeleteTestsPayload**](SyntheticsDeleteTestsPayload.md)| Public ID list of the Synthetic tests to be deleted. |

### Return type

[**SyntheticsDeleteTestsResponse**](SyntheticsDeleteTestsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **edit_global_variable**
> SyntheticsGlobalVariable edit_global_variable(variable_id, body)

Edit a global variable

Edit a Synthetics global variable.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example" # str | The ID of the global variable.
    body = SyntheticsGlobalVariable(
        description="Example description",
        id="id_example",
        name="MY_VARIABLE",
        tags=[
            "["team:front","test:workflow-1"]",
        ],
        value=SyntheticsGlobalVariableValue(
            secure=True,
            value="example-value",
        ),
    ) # SyntheticsGlobalVariable | Details of the global variable to update.

    # example passing only required values which don't have defaults set
    try:
        # Edit a global variable
        api_response = api_instance.edit_global_variable(variable_id, body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->edit_global_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| The ID of the global variable. |
 **body** | [**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)| Details of the global variable to update. |

### Return type

[**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_test_latest_results**
> SyntheticsGetAPITestLatestResultsResponse get_api_test_latest_results(public_id)

Get the test's latest results summaries (API)

Get the last 50 test results summaries for a given Synthetics API test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the test for which to search results for.
    from_ts = 1 # int | Timestamp from which to start querying results. (optional)
    to_ts = 1 # int | Timestamp up to which to query results. (optional)
    probe_dc = [
        "probe_dc_example",
    ] # [str] | Locations for which to query results. (optional)

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

[**SyntheticsGetAPITestLatestResultsResponse**](SyntheticsGetAPITestLatestResultsResponse.md)

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
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_test_result**
> SyntheticsAPITestResultFull get_api_test_result(public_id, result_id)

Get a test result (API)

Get a specific full result from a given (API) Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the API test to which the target result belongs.
    result_id = "result_id_example" # str | The ID of the result to get.

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

[**SyntheticsAPITestResultFull**](SyntheticsAPITestResultFull.md)

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
**404** | - Synthetic is not activated for the user - Test or result is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_browser_test**
> SyntheticsTestDetails get_browser_test(public_id)

Get a test configuration (browser)

Get the detailed configuration (including steps) associated with a Synthetic browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the test to get details from.

    # example passing only required values which don't have defaults set
    try:
        # Get a test configuration (browser)
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

[**SyntheticsTestDetails**](SyntheticsTestDetails.md)

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
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_browser_test_latest_results**
> SyntheticsGetBrowserTestLatestResultsResponse get_browser_test_latest_results(public_id)

Get the test's latest results summaries (browser)

Get the last 50 test results summaries for a given Synthetics Browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the browser test for which to search results for.
    from_ts = 1 # int | Timestamp from which to start querying results. (optional)
    to_ts = 1 # int | Timestamp up to which to query results. (optional)
    probe_dc = [
        "probe_dc_example",
    ] # [str] | Locations for which to query results. (optional)

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

[**SyntheticsGetBrowserTestLatestResultsResponse**](SyntheticsGetBrowserTestLatestResultsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | forbidden |  -  |
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_browser_test_result**
> SyntheticsBrowserTestResultFull get_browser_test_result(public_id, result_id)

Get a test result (browser)

Get a specific full result from a given (browser) Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the browser test to which the target result belongs.
    result_id = "result_id_example" # str | The ID of the result to get.

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

[**SyntheticsBrowserTestResultFull**](SyntheticsBrowserTestResultFull.md)

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
**404** | - Synthetic is not activated for the user - Test or result is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_global_variable**
> SyntheticsGlobalVariable get_global_variable(variable_id)

Get a global variable

Get the detailed configuration of a global variable.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example" # str | The ID of the global variable.

    # example passing only required values which don't have defaults set
    try:
        # Get a global variable
        api_response = api_instance.get_global_variable(variable_id)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->get_global_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| The ID of the global variable. |

### Return type

[**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)

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

# **get_test**
> SyntheticsTestDetails get_test(public_id)

Get a test configuration (API)

Get the detailed configuration associated with a Synthetics test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the test to get details from.

    # example passing only required values which don't have defaults set
    try:
        # Get a test configuration (API)
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

[**SyntheticsTestDetails**](SyntheticsTestDetails.md)

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
**404** | - Synthetic is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_locations**
> SyntheticsLocations list_locations()

Get all locations (public and private)

Get the list of public and private locations available for Synthetic tests. No arguments required.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all locations (public and private)
        api_response = api_instance.list_locations()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->list_locations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SyntheticsLocations**](SyntheticsLocations.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_tests**
> SyntheticsListTestsResponse list_tests()

Get the list of all tests

Get the list of all Synthetic tests.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the list of all tests
        api_response = api_instance.list_tests()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->list_tests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SyntheticsListTestsResponse**](SyntheticsListTestsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Returns the list of all Synthetic tests. |  -  |
**403** | Forbidden |  -  |
**404** | Synthetics is not activated for the user. |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **trigger_ci_tests**
> SyntheticsTriggerCITestsResponse trigger_ci_tests(body)

Trigger some Synthetics tests for CI

Trigger a set of Synthetics tests for continuous integration

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsCITestBody(
        tests=[
            SyntheticsCITest(
                allow_insecure_certificates=True,
                basic_auth=SyntheticsBasicAuth(
                    password="password_example",
                    username="username_example",
                ),
                body="body_example",
                body_type="body_type_example",
                cookies="cookies_example",
                device_ids=[
                    SyntheticsDeviceID("laptop_large"),
                ],
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    "key": "key_example",
                ),
                locations=[
                    "locations_example",
                ],
                metadata=SyntheticsCITestMetadata(
                    ci=SyntheticsCITestMetadataCi(
                        pipeline="pipeline_example",
                        provider="provider_example",
                    ),
                    git=SyntheticsCITestMetadataGit(
                        branch="branch_example",
                        commit_sha="commit_sha_example",
                    ),
                ),
                public_id="aaa-aaa-aaa",
                retry=SyntheticsTestOptionsRetry(
                    count=1,
                    interval=3.14,
                ),
                start_url="start_url_example",
                variables={
                    "key": "key_example",
                },
            ),
        ],
    ) # SyntheticsCITestBody | Details of the test to trigger.

    # example passing only required values which don't have defaults set
    try:
        # Trigger some Synthetics tests for CI
        api_response = api_instance.trigger_ci_tests(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling SyntheticsApi->trigger_ci_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyntheticsCITestBody**](SyntheticsCITestBody.md)| Details of the test to trigger. |

### Return type

[**SyntheticsTriggerCITestsResponse**](SyntheticsTriggerCITestsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | JSON format is wrong |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_test**
> SyntheticsTestDetails update_test(public_id, body)

Edit a test

Edit the configuration of a Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the test to get details from.
    body = SyntheticsTestDetails(
        config=SyntheticsTestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            request=SyntheticsTestRequest(
                basic_auth=SyntheticsBasicAuth(
                    password="password_example",
                    username="username_example",
                ),
                body="body_example",
                certificate=SyntheticsTestRequestCertificate(
                    cert=SyntheticsTestRequestCertificateItem(
                        content="content_example",
                        filename="filename_example",
                        updated_at="updated_at_example",
                    ),
                    key=SyntheticsTestRequestCertificateItem(
                        content="content_example",
                        filename="filename_example",
                        updated_at="updated_at_example",
                    ),
                ),
                dns_server="dns_server_example",
                headers=SyntheticsTestHeaders(
                    "key": "key_example",
                ),
                host="host_example",
                method=HTTPMethod("GET"),
                port=1,
                query={},
                timeout=3.14,
                url="url_example",
            ),
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="name_example",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("element"),
                ),
            ],
        ),
        locations=[
            "locations_example",
        ],
        message="message_example",
        monitor_id=1,
        name="name_example",
        options=SyntheticsTestOptions(
            accept_self_signed=True,
            allow_insecure=True,
            device_ids=[
                SyntheticsDeviceID("laptop_large"),
            ],
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=SyntheticsTickInterval(60),
        ),
        public_id="public_id_example",
        status=SyntheticsTestPauseStatus("live"),
        steps=[
            SyntheticsStep(
                allow_failure=True,
                name="name_example",
                params={},
                timeout=3.14,
                type=SyntheticsStepType("assertCurrentUrl"),
            ),
        ],
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=[
            "tags_example",
        ],
        type=SyntheticsTestDetailsType("api"),
    ) # SyntheticsTestDetails | New test details to be saved.

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
 **body** | [**SyntheticsTestDetails**](SyntheticsTestDetails.md)| New test details to be saved. |

### Return type

[**SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_test_pause_status**
> bool update_test_pause_status(public_id, body)

Pause or start a test

Pause or start a Synthetics test by changing the status.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import synthetics_api
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
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example" # str | The public ID of the Synthetic test to update.
    body = SyntheticsUpdateTestPauseStatusPayload(
        new_status=SyntheticsTestPauseStatus("live"),
    ) # SyntheticsUpdateTestPauseStatusPayload | Status to set the given Synthetic test to.

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
 **body** | [**SyntheticsUpdateTestPauseStatusPayload**](SyntheticsUpdateTestPauseStatusPayload.md)| Status to set the given Synthetic test to. |

### Return type

**bool**

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

