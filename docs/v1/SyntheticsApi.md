# datadog_api_client.v1.SyntheticsApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                                                                  | HTTP request                                                             | Description                                       |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------- |
| [**create_global_variable**](SyntheticsApi.md#create_global_variable)                   | **POST** /api/v1/synthetics/variables                                    | Create a global variable                          |
| [**create_private_location**](SyntheticsApi.md#create_private_location)                 | **POST** /api/v1/synthetics/private-locations                            | Create a private location                         |
| [**create_synthetics_api_test**](SyntheticsApi.md#create_synthetics_api_test)           | **POST** /api/v1/synthetics/tests/api                                    | Create an API test                                |
| [**create_synthetics_browser_test**](SyntheticsApi.md#create_synthetics_browser_test)   | **POST** /api/v1/synthetics/tests/browser                                | Create a browser test                             |
| [**delete_global_variable**](SyntheticsApi.md#delete_global_variable)                   | **DELETE** /api/v1/synthetics/variables/{variable_id}                    | Delete a global variable                          |
| [**delete_private_location**](SyntheticsApi.md#delete_private_location)                 | **DELETE** /api/v1/synthetics/private-locations/{location_id}            | Delete a private location                         |
| [**delete_tests**](SyntheticsApi.md#delete_tests)                                       | **POST** /api/v1/synthetics/tests/delete                                 | Delete tests                                      |
| [**edit_global_variable**](SyntheticsApi.md#edit_global_variable)                       | **PUT** /api/v1/synthetics/variables/{variable_id}                       | Edit a global variable                            |
| [**get_api_test**](SyntheticsApi.md#get_api_test)                                       | **GET** /api/v1/synthetics/tests/api/{public_id}                         | Get an API test                                   |
| [**get_api_test_latest_results**](SyntheticsApi.md#get_api_test_latest_results)         | **GET** /api/v1/synthetics/tests/{public_id}/results                     | Get an API test&#39;s latest results summaries    |
| [**get_api_test_result**](SyntheticsApi.md#get_api_test_result)                         | **GET** /api/v1/synthetics/tests/{public_id}/results/{result_id}         | Get an API test result                            |
| [**get_browser_test**](SyntheticsApi.md#get_browser_test)                               | **GET** /api/v1/synthetics/tests/browser/{public_id}                     | Get a browser test                                |
| [**get_browser_test_latest_results**](SyntheticsApi.md#get_browser_test_latest_results) | **GET** /api/v1/synthetics/tests/browser/{public_id}/results             | Get a browser test&#39;s latest results summaries |
| [**get_browser_test_result**](SyntheticsApi.md#get_browser_test_result)                 | **GET** /api/v1/synthetics/tests/browser/{public_id}/results/{result_id} | Get a browser test result                         |
| [**get_global_variable**](SyntheticsApi.md#get_global_variable)                         | **GET** /api/v1/synthetics/variables/{variable_id}                       | Get a global variable                             |
| [**get_private_location**](SyntheticsApi.md#get_private_location)                       | **GET** /api/v1/synthetics/private-locations/{location_id}               | Get a private location                            |
| [**get_synthetics_ci_batch**](SyntheticsApi.md#get_synthetics_ci_batch)                 | **GET** /api/v1/synthetics/ci/batch/{batch_id}                           | Get details of batch                              |
| [**get_test**](SyntheticsApi.md#get_test)                                               | **GET** /api/v1/synthetics/tests/{public_id}                             | Get a test configuration                          |
| [**list_global_variables**](SyntheticsApi.md#list_global_variables)                     | **GET** /api/v1/synthetics/variables                                     | Get all global variables                          |
| [**list_locations**](SyntheticsApi.md#list_locations)                                   | **GET** /api/v1/synthetics/locations                                     | Get all locations (public and private)            |
| [**list_tests**](SyntheticsApi.md#list_tests)                                           | **GET** /api/v1/synthetics/tests                                         | Get the list of all tests                         |
| [**trigger_ci_tests**](SyntheticsApi.md#trigger_ci_tests)                               | **POST** /api/v1/synthetics/tests/trigger/ci                             | Trigger tests from CI/CD pipelines                |
| [**trigger_tests**](SyntheticsApi.md#trigger_tests)                                     | **POST** /api/v1/synthetics/tests/trigger                                | Trigger Synthetics tests                          |
| [**update_api_test**](SyntheticsApi.md#update_api_test)                                 | **PUT** /api/v1/synthetics/tests/api/{public_id}                         | Edit an API test                                  |
| [**update_browser_test**](SyntheticsApi.md#update_browser_test)                         | **PUT** /api/v1/synthetics/tests/browser/{public_id}                     | Edit a browser test                               |
| [**update_private_location**](SyntheticsApi.md#update_private_location)                 | **PUT** /api/v1/synthetics/private-locations/{location_id}               | Edit a private location                           |
| [**update_test_pause_status**](SyntheticsApi.md#update_test_pause_status)               | **PUT** /api/v1/synthetics/tests/{public_id}/status                      | Pause or start a test                             |

# **create_global_variable**

> SyntheticsGlobalVariable create_global_variable(body)

Create a Synthetics global variable.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
        attributes=SyntheticsGlobalVariableAttributes(
            restricted_roles=[
                "restricted_roles_example",
            ],
        ),
        description="Example description",
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

| Name     | Type                                                        | Description                               | Notes |
| -------- | ----------------------------------------------------------- | ----------------------------------------- | ----- |
| **body** | [**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md) | Details of the global variable to create. |

### Return type

[**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Invalid request   | -                |
| **403**     | Forbidden         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_private_location**

> SyntheticsPrivateLocationCreationResponse create_private_location(body)

Create a new Synthetics private location.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
        name="New private location",
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

| Name     | Type                                                          | Description                                | Notes |
| -------- | ------------------------------------------------------------- | ------------------------------------------ | ----- |
| **body** | [**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md) | Details of the private location to create. |

### Return type

[**SyntheticsPrivateLocationCreationResponse**](SyntheticsPrivateLocationCreationResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                      | Response headers |
| ----------- | ------------------------------------------------ | ---------------- |
| **200**     | OK                                               | -                |
| **402**     | Quota reached for private locations              | -                |
| **404**     | Private locations are not activated for the user | -                |
| **429**     | Too many requests                                | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_synthetics_api_test**

> SyntheticsAPITest create_synthetics_api_test(body)

Create a Synthetic API test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                allow_insecure=True,
                basic_auth=SyntheticsBasicAuth(),
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
                dns_server_port=1,
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
                ),
                host="host_example",
                message="message_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                number_of_packets=0,
                port=1,
                proxy=SyntheticsTestRequestProxy(
                    headers=SyntheticsTestHeaders(
                        key="key_example",
                    ),
                    url="https://example.com",
                ),
                query={},
                servername="servername_example",
                should_track_hops=True,
                timeout=3.14,
                url="https://example.com",
            ),
            steps=[
                SyntheticsAPIStep(
                    allow_failure=True,
                    assertions=[
                        SyntheticsAssertion(),
                    ],
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
                    is_critical=True,
                    name="name_example",
                    request=SyntheticsTestRequest(
                        allow_insecure=True,
                        basic_auth=SyntheticsBasicAuth(),
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
                        dns_server_port=1,
                        follow_redirects=True,
                        headers=SyntheticsTestHeaders(
                            key="key_example",
                        ),
                        host="host_example",
                        message="message_example",
                        method=HTTPMethod("GET"),
                        no_saving_response_body=True,
                        number_of_packets=0,
                        port=1,
                        proxy=SyntheticsTestRequestProxy(
                            headers=SyntheticsTestHeaders(
                                key="key_example",
                            ),
                            url="https://example.com",
                        ),
                        query={},
                        servername="servername_example",
                        should_track_hops=True,
                        timeout=3.14,
                        url="https://example.com",
                    ),
                    retry=SyntheticsTestOptionsRetry(
                        count=1,
                        interval=3.14,
                    ),
                    subtype=SyntheticsAPIStepSubtype("http"),
                ),
            ],
        ),
        locations=["aws:eu-west-3"],
        message="Notification message",
        name="Test name",
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
            monitor_name="monitor_name_example",
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            monitor_priority=1,
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=30,
        ),
        status=SyntheticsTestPauseStatus("live"),
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=["env:production"],
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

| Name     | Type                                          | Description                    | Notes |
| -------- | --------------------------------------------- | ------------------------------ | ----- |
| **body** | [**SyntheticsAPITest**](SyntheticsAPITest.md) | Details of the test to create. |

### Return type

[**SyntheticsAPITest**](SyntheticsAPITest.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                              | Response headers |
| ----------- | ---------------------------------------- | ---------------- |
| **200**     | OK - Returns the created test details.   | -                |
| **400**     | - JSON format is wrong - Creation failed | -                |
| **402**     | Test quota is reached                    | -                |
| **403**     | Forbidden                                | -                |
| **429**     | Too many requests                        | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_synthetics_browser_test**

> SyntheticsBrowserTest create_synthetics_browser_test(body)

Create a Synthetic browser test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
            config_variables=[
                SyntheticsConfigVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                allow_insecure=True,
                basic_auth=SyntheticsBasicAuth(),
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
                dns_server_port=1,
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
                ),
                host="host_example",
                message="message_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                number_of_packets=0,
                port=1,
                proxy=SyntheticsTestRequestProxy(
                    headers=SyntheticsTestHeaders(
                        key="key_example",
                    ),
                    url="https://example.com",
                ),
                query={},
                servername="servername_example",
                should_track_hops=True,
                timeout=3.14,
                url="https://example.com",
            ),
            set_cookie="set_cookie_example",
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("text"),
                ),
            ],
        ),
        locations=[
            "locations_example",
        ],
        message="",
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
            monitor_name="monitor_name_example",
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            monitor_priority=1,
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=30,
        ),
        status=SyntheticsTestPauseStatus("live"),
        steps=[
            SyntheticsStep(
                allow_failure=True,
                name="name_example",
                params={},
                timeout=1,
                type=SyntheticsStepType("assertElementContent"),
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

| Name     | Type                                                  | Description                    | Notes |
| -------- | ----------------------------------------------------- | ------------------------------ | ----- |
| **body** | [**SyntheticsBrowserTest**](SyntheticsBrowserTest.md) | Details of the test to create. |

### Return type

[**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                              | Response headers |
| ----------- | ---------------------------------------- | ---------------- |
| **200**     | OK - Returns the created test details.   | -                |
| **400**     | - JSON format is wrong - Creation failed | -                |
| **402**     | Test quota is reached                    | -                |
| **403**     | Forbidden                                | -                |
| **429**     | Too many requests                        | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_global_variable**

> delete_global_variable(variable_id)

Delete a Synthetics global variable.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name            | Type    | Description                    | Notes |
| --------------- | ------- | ------------------------------ | ----- |
| **variable_id** | **str** | The ID of the global variable. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description          | Response headers |
| ----------- | -------------------- | ---------------- |
| **200**     | OK                   | -                |
| **400**     | JSON format is wrong | -                |
| **403**     | Forbidden            | -                |
| **404**     | Not found            | -                |
| **429**     | Too many requests    | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_private_location**

> delete_private_location(location_id)

Delete a Synthetics private location.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name            | Type    | Description                     | Notes |
| --------------- | ------- | ------------------------------- | ----- |
| **location_id** | **str** | The ID of the private location. |

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                          | Response headers |
| ----------- | ------------------------------------------------------------------------------------ | ---------------- |
| **204**     | OK                                                                                   | -                |
| **404**     | - Private locations are not activated for the user - Private location does not exist | -                |
| **429**     | Too many requests                                                                    | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_tests**

> SyntheticsDeleteTestsResponse delete_tests(body)

Delete multiple Synthetic tests by ID.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name     | Type                                                                | Description                                          | Notes |
| -------- | ------------------------------------------------------------------- | ---------------------------------------------------- | ----- |
| **body** | [**SyntheticsDeleteTestsPayload**](SyntheticsDeleteTestsPayload.md) | Public ID list of the Synthetic tests to be deleted. |

### Return type

[**SyntheticsDeleteTestsResponse**](SyntheticsDeleteTestsResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | OK.                                                                                                                                                    | -                |
| **400**     | - JSON format is wrong - Test cannot be deleted as it&#39;s used elsewhere (as a sub-test or in an uptime widget) - Some IDs are not owned by the user | -                |
| **403**     | Forbidden                                                                                                                                              | -                |
| **404**     | - Tests to be deleted can&#39;t be found - Synthetics is not activated for the user                                                                    | -                |
| **429**     | Too many requests                                                                                                                                      | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **edit_global_variable**

> SyntheticsGlobalVariable edit_global_variable(variable_id, body)

Edit a Synthetics global variable.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
        attributes=SyntheticsGlobalVariableAttributes(
            restricted_roles=[
                "restricted_roles_example",
            ],
        ),
        description="Example description",
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

| Name            | Type                                                        | Description                               | Notes |
| --------------- | ----------------------------------------------------------- | ----------------------------------------- | ----- |
| **variable_id** | **str**                                                     | The ID of the global variable.            |
| **body**        | [**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md) | Details of the global variable to update. |

### Return type

[**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Invalid request   | -                |
| **403**     | Forbidden         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_test**

> SyntheticsAPITest get_api_test(public_id)

Get the detailed configuration associated with
a Synthetic API test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name          | Type    | Description                                    | Notes |
| ------------- | ------- | ---------------------------------------------- | ----- |
| **public_id** | **str** | The public ID of the test to get details from. |

### Return type

[**SyntheticsAPITest**](SyntheticsAPITest.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                          | Response headers |
| ----------- | ------------------------------------------------------------------------------------ | ---------------- |
| **200**     | OK                                                                                   | -                |
| **403**     | Forbidden                                                                            | -                |
| **404**     | - Synthetic Monitoring is not activated for the user - Test is not owned by the user | -                |
| **429**     | Too many requests                                                                    | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_test_latest_results**

> SyntheticsGetAPITestLatestResultsResponse get_api_test_latest_results(public_id)

Get the last 50 test results summaries for a given Synthetics API test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
    from_ts = 1  # int | Timestamp in milliseconds from which to start querying results. (optional)
    to_ts = 1  # int | Timestamp in milliseconds up to which to query results. (optional)
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

| Name          | Type      | Description                                                     | Notes      |
| ------------- | --------- | --------------------------------------------------------------- | ---------- |
| **public_id** | **str**   | The public ID of the test for which to search results for.      |
| **from_ts**   | **int**   | Timestamp in milliseconds from which to start querying results. | [optional] |
| **to_ts**     | **int**   | Timestamp in milliseconds up to which to query results.         | [optional] |
| **probe_dc**  | **[str]** | Locations for which to query results.                           | [optional] |

### Return type

[**SyntheticsGetAPITestLatestResultsResponse**](SyntheticsGetAPITestLatestResultsResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                               | Response headers |
| ----------- | ------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                        | -                |
| **403**     | Forbidden                                                                 | -                |
| **404**     | - Synthetic is not activated for the user - Test is not owned by the user | -                |
| **429**     | Too many requests                                                         | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_api_test_result**

> SyntheticsAPITestResultFull get_api_test_result(public_id, result_id)

Get a specific full result from a given (API) Synthetic test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name          | Type    | Description                                                       | Notes |
| ------------- | ------- | ----------------------------------------------------------------- | ----- |
| **public_id** | **str** | The public ID of the API test to which the target result belongs. |
| **result_id** | **str** | The ID of the result to get.                                      |

### Return type

[**SyntheticsAPITestResultFull**](SyntheticsAPITestResultFull.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                         | Response headers |
| ----------- | ----------------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                                  | -                |
| **403**     | Forbidden                                                                           | -                |
| **404**     | - Synthetic is not activated for the user - Test or result is not owned by the user | -                |
| **429**     | Too many requests                                                                   | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_browser_test**

> SyntheticsBrowserTest get_browser_test(public_id)

Get the detailed configuration (including steps) associated with
a Synthetic browser test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name          | Type    | Description                                    | Notes |
| ------------- | ------- | ---------------------------------------------- | ----- |
| **public_id** | **str** | The public ID of the test to get details from. |

### Return type

[**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                               | Response headers |
| ----------- | ------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                        | -                |
| **403**     | Forbidden                                                                 | -                |
| **404**     | - Synthetic is not activated for the user - Test is not owned by the user | -                |
| **429**     | Too many requests                                                         | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_browser_test_latest_results**

> SyntheticsGetBrowserTestLatestResultsResponse get_browser_test_latest_results(public_id)

Get the last 50 test results summaries for a given Synthetics Browser test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
    from_ts = 1  # int | Timestamp in milliseconds from which to start querying results. (optional)
    to_ts = 1  # int | Timestamp in milliseconds up to which to query results. (optional)
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

| Name          | Type      | Description                                                        | Notes      |
| ------------- | --------- | ------------------------------------------------------------------ | ---------- |
| **public_id** | **str**   | The public ID of the browser test for which to search results for. |
| **from_ts**   | **int**   | Timestamp in milliseconds from which to start querying results.    | [optional] |
| **to_ts**     | **int**   | Timestamp in milliseconds up to which to query results.            | [optional] |
| **probe_dc**  | **[str]** | Locations for which to query results.                              | [optional] |

### Return type

[**SyntheticsGetBrowserTestLatestResultsResponse**](SyntheticsGetBrowserTestLatestResultsResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                               | Response headers |
| ----------- | ------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                        | -                |
| **403**     | forbidden                                                                 | -                |
| **404**     | - Synthetic is not activated for the user - Test is not owned by the user | -                |
| **429**     | Too many requests                                                         | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_browser_test_result**

> SyntheticsBrowserTestResultFull get_browser_test_result(public_id, result_id)

Get a specific full result from a given (browser) Synthetic test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name          | Type    | Description                                                           | Notes |
| ------------- | ------- | --------------------------------------------------------------------- | ----- |
| **public_id** | **str** | The public ID of the browser test to which the target result belongs. |
| **result_id** | **str** | The ID of the result to get.                                          |

### Return type

[**SyntheticsBrowserTestResultFull**](SyntheticsBrowserTestResultFull.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                         | Response headers |
| ----------- | ----------------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                                  | -                |
| **403**     | Forbidden                                                                           | -                |
| **404**     | - Synthetic is not activated for the user - Test or result is not owned by the user | -                |
| **429**     | Too many requests                                                                   | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_global_variable**

> SyntheticsGlobalVariable get_global_variable(variable_id)

Get the detailed configuration of a global variable.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name            | Type    | Description                    | Notes |
| --------------- | ------- | ------------------------------ | ----- |
| **variable_id** | **str** | The ID of the global variable. |

### Return type

[**SyntheticsGlobalVariable**](SyntheticsGlobalVariable.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_private_location**

> SyntheticsPrivateLocation get_private_location(location_id)

Get a Synthetics private location.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name            | Type    | Description                     | Notes |
| --------------- | ------- | ------------------------------- | ----- |
| **location_id** | **str** | The ID of the private location. |

### Return type

[**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                    | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                                             | -                |
| **404**     | - Synthetic private locations are not activated for the user - Private location does not exist | -                |
| **429**     | Too many requests                                                                              | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_synthetics_ci_batch**

> SyntheticsBatchDetails get_synthetics_ci_batch(batch_id)

Get a batch's updated details.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
    batch_id = "batch_id_example"  # str | The ID of the batch.

    # example passing only required values which don't have defaults set
    try:
        # Get details of batch
        api_response = api_instance.get_synthetics_ci_batch(batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_synthetics_ci_batch: %s\n" % e)
```

### Parameters

| Name         | Type    | Description          | Notes |
| ------------ | ------- | -------------------- | ----- |
| **batch_id** | **str** | The ID of the batch. |

### Return type

[**SyntheticsBatchDetails**](SyntheticsBatchDetails.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description           | Response headers |
| ----------- | --------------------- | ---------------- |
| **200**     | OK                    | -                |
| **404**     | Batch does not exist. | -                |
| **429**     | Too many requests     | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_test**

> SyntheticsTestDetails get_test(public_id)

Get the detailed configuration associated with a Synthetics test.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name          | Type    | Description                                    | Notes |
| ------------- | ------- | ---------------------------------------------- | ----- |
| **public_id** | **str** | The public ID of the test to get details from. |

### Return type

[**SyntheticsTestDetails**](SyntheticsTestDetails.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                               | Response headers |
| ----------- | ------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                        | -                |
| **403**     | Forbidden                                                                 | -                |
| **404**     | - Synthetic is not activated for the user - Test is not owned by the user | -                |
| **429**     | Too many requests                                                         | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_global_variables**

> SyntheticsListGlobalVariablesResponse list_global_variables()

Get the list of all Synthetics global variables.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
        # Get all global variables
        api_response = api_instance.list_global_variables()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->list_global_variables: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SyntheticsListGlobalVariablesResponse**](SyntheticsListGlobalVariablesResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Forbidden         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_locations**

> SyntheticsLocations list_locations()

Get the list of public and private locations available for Synthetic
tests. No arguments required.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_tests**

> SyntheticsListTestsResponse list_tests()

Get the list of all Synthetic tests.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                   | Response headers |
| ----------- | --------------------------------------------- | ---------------- |
| **200**     | OK - Returns the list of all Synthetic tests. | -                |
| **403**     | Forbidden                                     | -                |
| **404**     | Synthetics is not activated for the user.     | -                |
| **429**     | Too many requests                             | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **trigger_ci_tests**

> SyntheticsTriggerCITestsResponse trigger_ci_tests(body)

Trigger a set of Synthetics tests for continuous integration.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
                basic_auth=SyntheticsBasicAuth(),
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
                metadata=SyntheticsCIBatchMetadata(
                    ci=SyntheticsCIBatchMetadataCI(
                        pipeline=SyntheticsCIBatchMetadataPipeline(
                            url="url_example",
                        ),
                        provider=SyntheticsCIBatchMetadataProvider(
                            name="name_example",
                        ),
                    ),
                    git=SyntheticsCIBatchMetadataGit(
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

| Name     | Type                                                | Description                     | Notes |
| -------- | --------------------------------------------------- | ------------------------------- | ----- |
| **body** | [**SyntheticsCITestBody**](SyntheticsCITestBody.md) | Details of the test to trigger. |

### Return type

[**SyntheticsTriggerCITestsResponse**](SyntheticsTriggerCITestsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description          | Response headers |
| ----------- | -------------------- | ---------------- |
| **200**     | OK                   | -                |
| **400**     | JSON format is wrong | -                |
| **429**     | Too many requests    | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **trigger_tests**

> SyntheticsTriggerCITestsResponse trigger_tests(body)

Trigger a set of Synthetics tests.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
    body = SyntheticsTriggerBody(
        tests=[
            SyntheticsTriggerTest(
                metadata=SyntheticsCIBatchMetadata(
                    ci=SyntheticsCIBatchMetadataCI(
                        pipeline=SyntheticsCIBatchMetadataPipeline(
                            url="url_example",
                        ),
                        provider=SyntheticsCIBatchMetadataProvider(
                            name="name_example",
                        ),
                    ),
                    git=SyntheticsCIBatchMetadataGit(
                        branch="branch_example",
                        commit_sha="commit_sha_example",
                    ),
                ),
                public_id="aaa-aaa-aaa",
            ),
        ],
    )  # SyntheticsTriggerBody | The identifiers of the tests to trigger.

    # example passing only required values which don't have defaults set
    try:
        # Trigger Synthetics tests
        api_response = api_instance.trigger_tests(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->trigger_tests: %s\n" % e)
```

### Parameters

| Name     | Type                                                  | Description                              | Notes |
| -------- | ----------------------------------------------------- | ---------------------------------------- | ----- |
| **body** | [**SyntheticsTriggerBody**](SyntheticsTriggerBody.md) | The identifiers of the tests to trigger. |

### Return type

[**SyntheticsTriggerCITestsResponse**](SyntheticsTriggerCITestsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_api_test**

> SyntheticsAPITest update_api_test(public_id, body)

Edit the configuration of a Synthetic API test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                allow_insecure=True,
                basic_auth=SyntheticsBasicAuth(),
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
                dns_server_port=1,
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
                ),
                host="host_example",
                message="message_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                number_of_packets=0,
                port=1,
                proxy=SyntheticsTestRequestProxy(
                    headers=SyntheticsTestHeaders(
                        key="key_example",
                    ),
                    url="https://example.com",
                ),
                query={},
                servername="servername_example",
                should_track_hops=True,
                timeout=3.14,
                url="https://example.com",
            ),
            steps=[
                SyntheticsAPIStep(
                    allow_failure=True,
                    assertions=[
                        SyntheticsAssertion(),
                    ],
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
                    is_critical=True,
                    name="name_example",
                    request=SyntheticsTestRequest(
                        allow_insecure=True,
                        basic_auth=SyntheticsBasicAuth(),
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
                        dns_server_port=1,
                        follow_redirects=True,
                        headers=SyntheticsTestHeaders(
                            key="key_example",
                        ),
                        host="host_example",
                        message="message_example",
                        method=HTTPMethod("GET"),
                        no_saving_response_body=True,
                        number_of_packets=0,
                        port=1,
                        proxy=SyntheticsTestRequestProxy(
                            headers=SyntheticsTestHeaders(
                                key="key_example",
                            ),
                            url="https://example.com",
                        ),
                        query={},
                        servername="servername_example",
                        should_track_hops=True,
                        timeout=3.14,
                        url="https://example.com",
                    ),
                    retry=SyntheticsTestOptionsRetry(
                        count=1,
                        interval=3.14,
                    ),
                    subtype=SyntheticsAPIStepSubtype("http"),
                ),
            ],
        ),
        locations=["aws:eu-west-3"],
        message="Notification message",
        name="Test name",
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
            monitor_name="monitor_name_example",
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            monitor_priority=1,
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=30,
        ),
        status=SyntheticsTestPauseStatus("live"),
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=["env:production"],
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

| Name          | Type                                          | Description                                    | Notes |
| ------------- | --------------------------------------------- | ---------------------------------------------- | ----- |
| **public_id** | **str**                                       | The public ID of the test to get details from. |
| **body**      | [**SyntheticsAPITest**](SyntheticsAPITest.md) | New test details to be saved.                  |

### Return type

[**SyntheticsAPITest**](SyntheticsAPITest.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                    | Response headers |
| ----------- | -------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                                                             | -                |
| **400**     | - JSON format is wrong - Updating sub-type is forbidden                                                        | -                |
| **403**     | Forbidden                                                                                                      | -                |
| **404**     | - Synthetic Monitoring is not activated for the user - Test is not owned by the user - Test can&#39;t be found | -                |
| **429**     | Too many requests                                                                                              | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_browser_test**

> SyntheticsBrowserTest update_browser_test(public_id, body)

Edit the configuration of a Synthetic browser test.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
            config_variables=[
                SyntheticsConfigVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                allow_insecure=True,
                basic_auth=SyntheticsBasicAuth(),
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
                dns_server_port=1,
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
                ),
                host="host_example",
                message="message_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                number_of_packets=0,
                port=1,
                proxy=SyntheticsTestRequestProxy(
                    headers=SyntheticsTestHeaders(
                        key="key_example",
                    ),
                    url="https://example.com",
                ),
                query={},
                servername="servername_example",
                should_track_hops=True,
                timeout=3.14,
                url="https://example.com",
            ),
            set_cookie="set_cookie_example",
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("text"),
                ),
            ],
        ),
        locations=[
            "locations_example",
        ],
        message="",
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
            monitor_name="monitor_name_example",
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            monitor_priority=1,
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=30,
        ),
        status=SyntheticsTestPauseStatus("live"),
        steps=[
            SyntheticsStep(
                allow_failure=True,
                name="name_example",
                params={},
                timeout=1,
                type=SyntheticsStepType("assertElementContent"),
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

| Name          | Type                                                  | Description                                    | Notes |
| ------------- | ----------------------------------------------------- | ---------------------------------------------- | ----- |
| **public_id** | **str**                                               | The public ID of the test to get details from. |
| **body**      | [**SyntheticsBrowserTest**](SyntheticsBrowserTest.md) | New test details to be saved.                  |

### Return type

[**SyntheticsBrowserTest**](SyntheticsBrowserTest.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                    | Response headers |
| ----------- | -------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | OK                                                                                                             | -                |
| **400**     | - JSON format is wrong - Updating sub-type is forbidden                                                        | -                |
| **403**     | Forbidden                                                                                                      | -                |
| **404**     | - Synthetic Monitoring is not activated for the user - Test is not owned by the user - Test can&#39;t be found | -                |
| **429**     | Too many requests                                                                                              | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_private_location**

> SyntheticsPrivateLocation update_private_location(location_id, body)

Edit a Synthetics private location.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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
        name="New private location",
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

| Name            | Type                                                          | Description                                    | Notes |
| --------------- | ------------------------------------------------------------- | ---------------------------------------------- | ----- |
| **location_id** | **str**                                                       | The ID of the private location.                |
| **body**        | [**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md) | Details of the private location to be updated. |

### Return type

[**SyntheticsPrivateLocation**](SyntheticsPrivateLocation.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                          | Response headers |
| ----------- | ------------------------------------------------------------------------------------ | ---------------- |
| **200**     | OK                                                                                   | -                |
| **404**     | - Private locations are not activated for the user - Private location does not exist | -                |
| **429**     | Too many requests                                                                    | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_test_pause_status**

> bool update_test_pause_status(public_id, body)

Pause or start a Synthetics test by changing the status.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

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

| Name          | Type                                                                                    | Description                                    | Notes |
| ------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------- | ----- |
| **public_id** | **str**                                                                                 | The public ID of the Synthetic test to update. |
| **body**      | [**SyntheticsUpdateTestPauseStatusPayload**](SyntheticsUpdateTestPauseStatusPayload.md) | Status to set the given Synthetic test to.     |

### Return type

**bool**

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                               | Response headers |
| ----------- | ------------------------------------------------------------------------- | ---------------- |
| **200**     | OK - Returns a boolean indicating if the update was successful.           | -                |
| **400**     | JSON format is wrong.                                                     | -                |
| **403**     | Forbidden                                                                 | -                |
| **404**     | - Synthetic is not activated for the user - Test is not owned by the user | -                |
| **429**     | Too many requests                                                         | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
