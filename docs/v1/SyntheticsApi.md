# datadog_api_client.v1.SyntheticsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_variable**](SyntheticsApi.md#create_global_variable) | **POST** /api/v1/synthetics/variables | Create a global variable
[**create_private_location**](SyntheticsApi.md#create_private_location) | **POST** /api/v1/synthetics/private-locations | Create a private location
[**create_synthetics_api_test**](SyntheticsApi.md#create_synthetics_api_test) | **POST** /api/v1/synthetics/tests/api | Create an API test
[**create_synthetics_browser_test**](SyntheticsApi.md#create_synthetics_browser_test) | **POST** /api/v1/synthetics/tests/browser | Create a browser test
[**delete_global_variable**](SyntheticsApi.md#delete_global_variable) | **DELETE** /api/v1/synthetics/variables/{variable_id} | Delete a global variable
[**delete_private_location**](SyntheticsApi.md#delete_private_location) | **DELETE** /api/v1/synthetics/private-locations/{location_id} | Delete a private location
[**delete_tests**](SyntheticsApi.md#delete_tests) | **POST** /api/v1/synthetics/tests/delete | Delete tests
[**edit_global_variable**](SyntheticsApi.md#edit_global_variable) | **PUT** /api/v1/synthetics/variables/{variable_id} | Edit a global variable
[**get_api_test**](SyntheticsApi.md#get_api_test) | **GET** /api/v1/synthetics/tests/api/{public_id} | Get an API test
[**get_api_test_latest_results**](SyntheticsApi.md#get_api_test_latest_results) | **GET** /api/v1/synthetics/tests/{public_id}/results | Get an API test&#39;s latest results summaries
[**get_api_test_result**](SyntheticsApi.md#get_api_test_result) | **GET** /api/v1/synthetics/tests/{public_id}/results/{result_id} | Get an API test result
[**get_browser_test**](SyntheticsApi.md#get_browser_test) | **GET** /api/v1/synthetics/tests/browser/{public_id} | Get a browser test
[**get_browser_test_latest_results**](SyntheticsApi.md#get_browser_test_latest_results) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results | Get a browser test&#39;s latest results summaries
[**get_browser_test_result**](SyntheticsApi.md#get_browser_test_result) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results/{result_id} | Get a browser test result
[**get_global_variable**](SyntheticsApi.md#get_global_variable) | **GET** /api/v1/synthetics/variables/{variable_id} | Get a global variable
[**get_private_location**](SyntheticsApi.md#get_private_location) | **GET** /api/v1/synthetics/private-locations/{location_id} | Get a private location
[**get_test**](SyntheticsApi.md#get_test) | **GET** /api/v1/synthetics/tests/{public_id} | Get a test configuration
[**list_locations**](SyntheticsApi.md#list_locations) | **GET** /api/v1/synthetics/locations | Get all locations (public and private)
[**list_tests**](SyntheticsApi.md#list_tests) | **GET** /api/v1/synthetics/tests | Get the list of all tests
[**trigger_ci_tests**](SyntheticsApi.md#trigger_ci_tests) | **POST** /api/v1/synthetics/tests/trigger/ci | Trigger tests from CI/CD pipelines
[**update_api_test**](SyntheticsApi.md#update_api_test) | **PUT** /api/v1/synthetics/tests/api/{public_id} | Edit an API test
[**update_browser_test**](SyntheticsApi.md#update_browser_test) | **PUT** /api/v1/synthetics/tests/browser/{public_id} | Edit a browser test
[**update_private_location**](SyntheticsApi.md#update_private_location) | **PUT** /api/v1/synthetics/private-locations/{location_id} | Edit a private location
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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsGlobalVariable(
        description="Example description",
        id="id_example",
        name="MY_VARIABLE",
        parse_test_options=SyntheticsGlobalVariableParseTestOptions(
            field="content-type",
            parser=SyntheticsVariableParser(
                type=SyntheticsGlobalVariableParserType("raw"),
                value="value_example",
            ),
            type=SyntheticsGlobalVariableParseTestOptionsType("http_body"),
        ),
        parse_test_public_id="abc-def-123",
        tags=["team:front","test:workflow-1"],
        value=SyntheticsGlobalVariableValue(
            secure=True,
            value="example-value",
        ),
    )  # SyntheticsGlobalVariable | Details of the global variable to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a global variable
        api_response = api_instance.create_global_variable(body)
        pprint(api_response)
    except ApiException as e:
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

# **create_private_location**
> SyntheticsPrivateLocationCreationResponse create_private_location(body)

Create a private location

Create a new Synthetics private location.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsPrivateLocation(
        description="Description of private location",
        id="id_example",
        name="New private location",
        secrets=SyntheticsPrivateLocationSecrets(
            authentication=SyntheticsPrivateLocationSecretsAuthentication(
                id="id_example",
                key="key_example",
            ),
            config_decryption=SyntheticsPrivateLocationSecretsConfigDecryption(
                key="key_example",
            ),
        ),
        tags=["team:front"],
    )  # SyntheticsPrivateLocation | Details of the private location to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a private location
        api_response = api_instance.create_private_location(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->create_private_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md)| Details of the private location to create. |

### Return type

[**SyntheticsPrivateLocationCreationResponse**](SyntheticsPrivateLocationCreationResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Quota reached for private locations |  -  |
**404** | Private locations are not activated for the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_synthetics_api_test**
> SyntheticsAPITest create_synthetics_api_test(body)

Create an API test

Create a Synthetic API test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsAPITest(
        config=SyntheticsAPITestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            config_variables=[
                SyntheticsConfigVariable(
                    example="example_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                basic_auth=SyntheticsBasicAuth(
                    password="",
                    username="",
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
                    key="key_example",
                ),
                host="host_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                port=1,
                query={},
                timeout=3.14,
                url="url_example",
            ),
            steps=[
                SyntheticsAPIStep(
                    assertions=[],
                    extracted_values=[
                        SyntheticsParsingOptions(
                            field="content-type",
                            name="name_example",
                            parser=SyntheticsVariableParser(
                                type=SyntheticsGlobalVariableParserType("raw"),
                                value="value_example",
                            ),
                            type=SyntheticsGlobalVariableParseTestOptionsType("http_body"),
                        ),
                    ],
                    name="name_example",
                    request=SyntheticsTestRequest(
                        basic_auth=SyntheticsBasicAuth(
                            password="",
                            username="",
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
                        headers=SyntheticsTestHeaders(SyntheticsTestHeaders),
                        host="host_example",
                        method=HTTPMethod("GET"),
                        no_saving_response_body=True,
                        port=1,
                        query={},
                        timeout=3.14,
                        url="url_example",
                    ),
                    subtype=SyntheticsAPIStepSubtype("http"),
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
            disable_cors=True,
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=SyntheticsTickInterval(60),
        ),
        public_id="public_id_example",
        status=SyntheticsTestPauseStatus("live"),
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=[
            "tags_example",
        ],
        type=SyntheticsAPITestType("api"),
    )  # SyntheticsAPITest | Details of the test to create.

    # example passing only required values which don't have defaults set
    try:
        # Create an API test
        api_response = api_instance.create_synthetics_api_test(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->create_synthetics_api_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyntheticsAPITest**](SyntheticsAPITest.md)| Details of the test to create. |

### Return type

[**SyntheticsAPITest**](SyntheticsAPITest.md)

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

# **create_synthetics_browser_test**
> SyntheticsBrowserTest create_synthetics_browser_test(body)

Create a browser test

Create a Synthetic browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsBrowserTest(
        config=SyntheticsBrowserTestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            request=SyntheticsTestRequest(
                basic_auth=SyntheticsBasicAuth(
                    password="",
                    username="",
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
                    key="key_example",
                ),
                host="host_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                port=1,
                query={},
                timeout=3.14,
                url="url_example",
            ),
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("element"),
                ),
            ],
        ),
        locations=[
            "locations_example",
        ],
        message="",
        monitor_id=1,
        name="name_example",
        options=SyntheticsTestOptions(
            accept_self_signed=True,
            allow_insecure=True,
            device_ids=[
                SyntheticsDeviceID("laptop_large"),
            ],
            disable_cors=True,
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            no_screenshot=True,
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
                timeout=1,
                type=SyntheticsStepType("assertCurrentUrl"),
            ),
        ],
        tags=[
            "tags_example",
        ],
        type=SyntheticsBrowserTestType("browser"),
    )  # SyntheticsBrowserTest | Details of the test to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a browser test
        api_response = api_instance.create_synthetics_browser_test(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->create_synthetics_browser_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)| Details of the test to create. |

### Return type

[**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)

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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example"  # str | The ID of the global variable.

    # example passing only required values which don't have defaults set
    try:
        # Delete a global variable
        api_instance.delete_global_variable(variable_id)
    except ApiException as e:
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

# **delete_private_location**
> delete_private_location(location_id)

Delete a private location

Delete a Synthetics private location.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    location_id = "location_id_example"  # str | The ID of the private location.

    # example passing only required values which don't have defaults set
    try:
        # Delete a private location
        api_instance.delete_private_location(location_id)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->delete_private_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The ID of the private location. |

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
**404** | - Private locations are not activated for the user - Private location does not exist |  -  |

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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsDeleteTestsPayload(
        public_ids=[],
    )  # SyntheticsDeleteTestsPayload | Public ID list of the Synthetic tests to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete tests
        api_response = api_instance.delete_tests(body)
        pprint(api_response)
    except ApiException as e:
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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example"  # str | The ID of the global variable.
    body = SyntheticsGlobalVariable(
        description="Example description",
        id="id_example",
        name="MY_VARIABLE",
        parse_test_options=SyntheticsGlobalVariableParseTestOptions(
            field="content-type",
            parser=SyntheticsVariableParser(
                type=SyntheticsGlobalVariableParserType("raw"),
                value="value_example",
            ),
            type=SyntheticsGlobalVariableParseTestOptionsType("http_body"),
        ),
        parse_test_public_id="abc-def-123",
        tags=["team:front","test:workflow-1"],
        value=SyntheticsGlobalVariableValue(
            secure=True,
            value="example-value",
        ),
    )  # SyntheticsGlobalVariable | Details of the global variable to update.

    # example passing only required values which don't have defaults set
    try:
        # Edit a global variable
        api_response = api_instance.edit_global_variable(variable_id, body)
        pprint(api_response)
    except ApiException as e:
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

# **get_api_test**
> SyntheticsAPITest get_api_test(public_id)

Get an API test

Get the detailed configuration associated with a Synthetic API test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the test to get details from.

    # example passing only required values which don't have defaults set
    try:
        # Get an API test
        api_response = api_instance.get_api_test(public_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_api_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |

### Return type

[**SyntheticsAPITest**](SyntheticsAPITest.md)

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
**404** | - Synthetic Monitoring is not activated for the user - Test is not owned by the user |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_test_latest_results**
> SyntheticsGetAPITestLatestResultsResponse get_api_test_latest_results(public_id)

Get an API test's latest results summaries

Get the last 50 test results summaries for a given Synthetics API test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the test for which to search results for.
    from_ts = 1  # int | Timestamp from which to start querying results. (optional)
    to_ts = 1  # int | Timestamp up to which to query results. (optional)
    probe_dc = [
        "probe_dc_example",
    ]  # [str] | Locations for which to query results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an API test's latest results summaries
        api_response = api_instance.get_api_test_latest_results(public_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_api_test_latest_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an API test's latest results summaries
        api_response = api_instance.get_api_test_latest_results(public_id, from_ts=from_ts, to_ts=to_ts, probe_dc=probe_dc)
        pprint(api_response)
    except ApiException as e:
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

Get an API test result

Get a specific full result from a given (API) Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the API test to which the target result belongs.
    result_id = "result_id_example"  # str | The ID of the result to get.

    # example passing only required values which don't have defaults set
    try:
        # Get an API test result
        api_response = api_instance.get_api_test_result(public_id, result_id)
        pprint(api_response)
    except ApiException as e:
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
> SyntheticsBrowserTest get_browser_test(public_id)

Get a browser test

Get the detailed configuration (including steps) associated with a Synthetic browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the test to get details from.

    # example passing only required values which don't have defaults set
    try:
        # Get a browser test
        api_response = api_instance.get_browser_test(public_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |

### Return type

[**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)

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

Get a browser test's latest results summaries

Get the last 50 test results summaries for a given Synthetics Browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the browser test for which to search results for.
    from_ts = 1  # int | Timestamp from which to start querying results. (optional)
    to_ts = 1  # int | Timestamp up to which to query results. (optional)
    probe_dc = [
        "probe_dc_example",
    ]  # [str] | Locations for which to query results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a browser test's latest results summaries
        api_response = api_instance.get_browser_test_latest_results(public_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test_latest_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a browser test's latest results summaries
        api_response = api_instance.get_browser_test_latest_results(public_id, from_ts=from_ts, to_ts=to_ts, probe_dc=probe_dc)
        pprint(api_response)
    except ApiException as e:
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

Get a browser test result

Get a specific full result from a given (browser) Synthetic test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the browser test to which the target result belongs.
    result_id = "result_id_example"  # str | The ID of the result to get.

    # example passing only required values which don't have defaults set
    try:
        # Get a browser test result
        api_response = api_instance.get_browser_test_result(public_id, result_id)
        pprint(api_response)
    except ApiException as e:
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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    variable_id = "variable_id_example"  # str | The ID of the global variable.

    # example passing only required values which don't have defaults set
    try:
        # Get a global variable
        api_response = api_instance.get_global_variable(variable_id)
        pprint(api_response)
    except ApiException as e:
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

# **get_private_location**
> SyntheticsPrivateLocation get_private_location(location_id)

Get a private location

Get a Synthetics private location.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    location_id = "location_id_example"  # str | The ID of the private location.

    # example passing only required values which don't have defaults set
    try:
        # Get a private location
        api_response = api_instance.get_private_location(location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_private_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The ID of the private location. |

### Return type

[**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | - Synthetic private locations are not activated for the user - Private location does not exist |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_test**
> SyntheticsTestDetails get_test(public_id)

Get a test configuration

Get the detailed configuration associated with a Synthetics test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the test to get details from.

    # example passing only required values which don't have defaults set
    try:
        # Get a test configuration
        api_response = api_instance.get_test(public_id)
        pprint(api_response)
    except ApiException as e:
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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all locations (public and private)
        api_response = api_instance.list_locations()
        pprint(api_response)
    except ApiException as e:
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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the list of all tests
        api_response = api_instance.list_tests()
        pprint(api_response)
    except ApiException as e:
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

Trigger tests from CI/CD pipelines

Trigger a set of Synthetics tests for continuous integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsCITestBody(
        tests=[
            SyntheticsCITest(
                allow_insecure_certificates=True,
                basic_auth=SyntheticsBasicAuth(
                    password="",
                    username="",
                ),
                body="body_example",
                body_type="body_type_example",
                cookies="cookies_example",
                device_ids=[
                    SyntheticsDeviceID("laptop_large"),
                ],
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
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
    )  # SyntheticsCITestBody | Details of the test to trigger.

    # example passing only required values which don't have defaults set
    try:
        # Trigger tests from CI/CD pipelines
        api_response = api_instance.trigger_ci_tests(body)
        pprint(api_response)
    except ApiException as e:
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

# **update_api_test**
> SyntheticsAPITest update_api_test(public_id, body)

Edit an API test

Edit the configuration of a Synthetic API test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the test to get details from.
    body = SyntheticsAPITest(
        config=SyntheticsAPITestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            config_variables=[
                SyntheticsConfigVariable(
                    example="example_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                basic_auth=SyntheticsBasicAuth(
                    password="",
                    username="",
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
                    key="key_example",
                ),
                host="host_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                port=1,
                query={},
                timeout=3.14,
                url="url_example",
            ),
            steps=[
                SyntheticsAPIStep(
                    assertions=[],
                    extracted_values=[
                        SyntheticsParsingOptions(
                            field="content-type",
                            name="name_example",
                            parser=SyntheticsVariableParser(
                                type=SyntheticsGlobalVariableParserType("raw"),
                                value="value_example",
                            ),
                            type=SyntheticsGlobalVariableParseTestOptionsType("http_body"),
                        ),
                    ],
                    name="name_example",
                    request=SyntheticsTestRequest(
                        basic_auth=SyntheticsBasicAuth(
                            password="",
                            username="",
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
                        headers=SyntheticsTestHeaders(SyntheticsTestHeaders),
                        host="host_example",
                        method=HTTPMethod("GET"),
                        no_saving_response_body=True,
                        port=1,
                        query={},
                        timeout=3.14,
                        url="url_example",
                    ),
                    subtype=SyntheticsAPIStepSubtype("http"),
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
            disable_cors=True,
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=SyntheticsTickInterval(60),
        ),
        public_id="public_id_example",
        status=SyntheticsTestPauseStatus("live"),
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=[
            "tags_example",
        ],
        type=SyntheticsAPITestType("api"),
    )  # SyntheticsAPITest | New test details to be saved.

    # example passing only required values which don't have defaults set
    try:
        # Edit an API test
        api_response = api_instance.update_api_test(public_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->update_api_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |
 **body** | [**SyntheticsAPITest**](SyntheticsAPITest.md)| New test details to be saved. |

### Return type

[**SyntheticsAPITest**](SyntheticsAPITest.md)

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
**404** | - Synthetic Monitoring is not activated for the user - Test is not owned by the user - Test can&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_browser_test**
> SyntheticsBrowserTest update_browser_test(public_id, body)

Edit a browser test

Edit the configuration of a Synthetic browser test.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the test to get details from.
    body = SyntheticsBrowserTest(
        config=SyntheticsBrowserTestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            request=SyntheticsTestRequest(
                basic_auth=SyntheticsBasicAuth(
                    password="",
                    username="",
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
                    key="key_example",
                ),
                host="host_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                port=1,
                query={},
                timeout=3.14,
                url="url_example",
            ),
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("element"),
                ),
            ],
        ),
        locations=[
            "locations_example",
        ],
        message="",
        monitor_id=1,
        name="name_example",
        options=SyntheticsTestOptions(
            accept_self_signed=True,
            allow_insecure=True,
            device_ids=[
                SyntheticsDeviceID("laptop_large"),
            ],
            disable_cors=True,
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            no_screenshot=True,
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
                timeout=1,
                type=SyntheticsStepType("assertCurrentUrl"),
            ),
        ],
        tags=[
            "tags_example",
        ],
        type=SyntheticsBrowserTestType("browser"),
    )  # SyntheticsBrowserTest | New test details to be saved.

    # example passing only required values which don't have defaults set
    try:
        # Edit a browser test
        api_response = api_instance.update_browser_test(public_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->update_browser_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| The public ID of the test to get details from. |
 **body** | [**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)| New test details to be saved. |

### Return type

[**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)

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
**404** | - Synthetic Monitoring is not activated for the user - Test is not owned by the user - Test can&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_private_location**
> SyntheticsPrivateLocation update_private_location(location_id, body)

Edit a private location

Edit a Synthetics private location.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    location_id = "location_id_example"  # str | The ID of the private location.
    body = SyntheticsPrivateLocation(
        description="Description of private location",
        id="id_example",
        name="New private location",
        secrets=SyntheticsPrivateLocationSecrets(
            authentication=SyntheticsPrivateLocationSecretsAuthentication(
                id="id_example",
                key="key_example",
            ),
            config_decryption=SyntheticsPrivateLocationSecretsConfigDecryption(
                key="key_example",
            ),
        ),
        tags=["team:front"],
    )  # SyntheticsPrivateLocation | Details of the private location to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Edit a private location
        api_response = api_instance.update_private_location(location_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->update_private_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The ID of the private location. |
 **body** | [**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md)| Details of the private location to be updated. |

### Return type

[**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | - Private locations are not activated for the user - Private location does not exist |  -  |

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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the Synthetic test to update.
    body = SyntheticsUpdateTestPauseStatusPayload(
        new_status=SyntheticsTestPauseStatus("live"),
    )  # SyntheticsUpdateTestPauseStatusPayload | Status to set the given Synthetic test to.

    # example passing only required values which don't have defaults set
    try:
        # Pause or start a test
        api_response = api_instance.update_test_pause_status(public_id, body)
        pprint(api_response)
    except ApiException as e:
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

