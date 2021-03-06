# datadog_api_client.v1.AWSIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_account**](AWSIntegrationApi.md#create_aws_account) | **POST** /api/v1/integration/aws | Create an AWS integration
[**create_aws_tag_filter**](AWSIntegrationApi.md#create_aws_tag_filter) | **POST** /api/v1/integration/aws/filtering | Set an AWS tag filter
[**create_new_aws_external_id**](AWSIntegrationApi.md#create_new_aws_external_id) | **PUT** /api/v1/integration/aws/generate_new_external_id | Generate a new external ID
[**delete_aws_account**](AWSIntegrationApi.md#delete_aws_account) | **DELETE** /api/v1/integration/aws | Delete an AWS integration
[**delete_aws_tag_filter**](AWSIntegrationApi.md#delete_aws_tag_filter) | **DELETE** /api/v1/integration/aws/filtering | Delete a tag filtering entry
[**list_available_aws_namespaces**](AWSIntegrationApi.md#list_available_aws_namespaces) | **GET** /api/v1/integration/aws/available_namespace_rules | List namespace rules
[**list_aws_accounts**](AWSIntegrationApi.md#list_aws_accounts) | **GET** /api/v1/integration/aws | List all AWS integrations
[**list_aws_tag_filters**](AWSIntegrationApi.md#list_aws_tag_filters) | **GET** /api/v1/integration/aws/filtering | Get all AWS tag filters
[**update_aws_account**](AWSIntegrationApi.md#update_aws_account) | **PUT** /api/v1/integration/aws | Update an AWS integration


# **create_aws_account**
> AWSAccountCreateResponse create_aws_account(body)

Create an AWS integration

Create a Datadog-Amazon Web Services integration. Using the `POST` method updates your integration configuration by adding your new configuration to the existing one in your Datadog organization. A unique AWS Account ID for role based authentication.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSAccount(
        access_key_id="access_key_id_example",
        account_id="1234567",
        account_specific_namespace_rules={
            "key": True,
        },
        excluded_regions=["us-east-1","us-west-2"],
        filter_tags=["<KEY>:<VALUE>"],
        host_tags=["<KEY>:<VALUE>"],
        role_name="DatadogAWSIntegrationRole",
        secret_access_key="secret_access_key_example",
    )  # AWSAccount | AWS Request Object

    # example passing only required values which don't have defaults set
    try:
        # Create an AWS integration
        api_response = api_instance.create_aws_account(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->create_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccount**](AWSAccount.md)| AWS Request Object |

### Return type

[**AWSAccountCreateResponse**](AWSAccountCreateResponse.md)

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
**409** | Conflict Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_aws_tag_filter**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_aws_tag_filter(body)

Set an AWS tag filter

Set an AWS tag filter.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSTagFilterCreateRequest(
        account_id="1234567",
        namespace=AWSNamespace("elb"),
        tag_filter_str="prod*",
    )  # AWSTagFilterCreateRequest | Set an AWS tag filter using an `aws_account_identifier`, `namespace`, and filtering string. Namespace options are `application_elb`, `elb`, `lambda`, `network_elb`, `rds`, `sqs`, and `custom`.

    # example passing only required values which don't have defaults set
    try:
        # Set an AWS tag filter
        api_response = api_instance.create_aws_tag_filter(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->create_aws_tag_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSTagFilterCreateRequest**](AWSTagFilterCreateRequest.md)| Set an AWS tag filter using an &#x60;aws_account_identifier&#x60;, &#x60;namespace&#x60;, and filtering string. Namespace options are &#x60;application_elb&#x60;, &#x60;elb&#x60;, &#x60;lambda&#x60;, &#x60;network_elb&#x60;, &#x60;rds&#x60;, &#x60;sqs&#x60;, and &#x60;custom&#x60;. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **create_new_aws_external_id**
> AWSAccountCreateResponse create_new_aws_external_id(body)

Generate a new external ID

Generate a new AWS external ID for a given AWS account ID and role name pair.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSAccount(
        access_key_id="access_key_id_example",
        account_id="1234567",
        account_specific_namespace_rules={
            "key": True,
        },
        excluded_regions=["us-east-1","us-west-2"],
        filter_tags=["<KEY>:<VALUE>"],
        host_tags=["<KEY>:<VALUE>"],
        role_name="DatadogAWSIntegrationRole",
        secret_access_key="secret_access_key_example",
    )  # AWSAccount | Your Datadog role delegation name. For more information about your AWS account Role name, see the [Datadog AWS integration configuration info](https://github.com/DataDog/documentation/blob/master/integrations/amazon_web_services/#installation).

    # example passing only required values which don't have defaults set
    try:
        # Generate a new external ID
        api_response = api_instance.create_new_aws_external_id(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->create_new_aws_external_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccount**](AWSAccount.md)| Your Datadog role delegation name. For more information about your AWS account Role name, see the [Datadog AWS integration configuration info](https://github.com/DataDog/documentation/blob/master/integrations/amazon_web_services/#installation). |

### Return type

[**AWSAccountCreateResponse**](AWSAccountCreateResponse.md)

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

# **delete_aws_account**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_aws_account(body)

Delete an AWS integration

Delete a Datadog-AWS integration matching the specified `account_id` and `role_name parameters`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSAccount(
        access_key_id="access_key_id_example",
        account_id="1234567",
        account_specific_namespace_rules={
            "key": True,
        },
        excluded_regions=["us-east-1","us-west-2"],
        filter_tags=["<KEY>:<VALUE>"],
        host_tags=["<KEY>:<VALUE>"],
        role_name="DatadogAWSIntegrationRole",
        secret_access_key="secret_access_key_example",
    )  # AWSAccount | AWS request object

    # example passing only required values which don't have defaults set
    try:
        # Delete an AWS integration
        api_response = api_instance.delete_aws_account(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->delete_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccount**](AWSAccount.md)| AWS request object |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
**409** | Conflict Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_aws_tag_filter**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_aws_tag_filter(body)

Delete a tag filtering entry

Delete a tag filtering entry.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSTagFilterDeleteRequest(
        account_id="FAKEAC0FAKEAC2FAKEAC",
        namespace=AWSNamespace("elb"),
    )  # AWSTagFilterDeleteRequest | Delete a tag filtering entry for a given AWS account and `dd-aws` namespace.

    # example passing only required values which don't have defaults set
    try:
        # Delete a tag filtering entry
        api_response = api_instance.delete_aws_tag_filter(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->delete_aws_tag_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSTagFilterDeleteRequest**](AWSTagFilterDeleteRequest.md)| Delete a tag filtering entry for a given AWS account and &#x60;dd-aws&#x60; namespace. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **list_available_aws_namespaces**
> [str] list_available_aws_namespaces()

List namespace rules

List all namespace rules for a given Datadog-AWS integration. This endpoint takes no arguments.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List namespace rules
        api_response = api_instance.list_available_aws_namespaces()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->list_available_aws_namespaces: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_aws_accounts**
> AWSAccountListResponse list_aws_accounts()

List all AWS integrations

List all Datadog-AWS integrations available in your Datadog organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    account_id = "account_id_example"  # str | Only return AWS accounts that matches this `account_id`. (optional)
    role_name = "role_name_example"  # str | Only return AWS accounts that matches this role_name. (optional)
    access_key_id = "access_key_id_example"  # str | Only return AWS accounts that matches this `access_key_id`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all AWS integrations
        api_response = api_instance.list_aws_accounts(account_id=account_id, role_name=role_name, access_key_id=access_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->list_aws_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Only return AWS accounts that matches this &#x60;account_id&#x60;. | [optional]
 **role_name** | **str**| Only return AWS accounts that matches this role_name. | [optional]
 **access_key_id** | **str**| Only return AWS accounts that matches this &#x60;access_key_id&#x60;. | [optional]

### Return type

[**AWSAccountListResponse**](AWSAccountListResponse.md)

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

# **list_aws_tag_filters**
> AWSTagFilterListResponse list_aws_tag_filters(account_id)

Get all AWS tag filters

Get all AWS tag filters.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    account_id = "account_id_example"  # str | Only return AWS filters that matches this `account_id`.

    # example passing only required values which don't have defaults set
    try:
        # Get all AWS tag filters
        api_response = api_instance.list_aws_tag_filters(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->list_aws_tag_filters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Only return AWS filters that matches this &#x60;account_id&#x60;. |

### Return type

[**AWSTagFilterListResponse**](AWSTagFilterListResponse.md)

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

# **update_aws_account**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_aws_account(body)

Update an AWS integration

Update a Datadog-Amazon Web Services integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSAccount(
        access_key_id="access_key_id_example",
        account_id="1234567",
        account_specific_namespace_rules={
            "key": True,
        },
        excluded_regions=["us-east-1","us-west-2"],
        filter_tags=["<KEY>:<VALUE>"],
        host_tags=["<KEY>:<VALUE>"],
        role_name="DatadogAWSIntegrationRole",
        secret_access_key="secret_access_key_example",
    )  # AWSAccount | AWS request object
    account_id = "account_id_example"  # str | Only return AWS accounts that matches this `account_id`. (optional)
    role_name = "role_name_example"  # str | Only return AWS accounts that match this `role_name`. Required if `account_id` is specified. (optional)
    access_key_id = "access_key_id_example"  # str | Only return AWS accounts that matches this `access_key_id`. Required if none of the other two options are specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an AWS integration
        api_response = api_instance.update_aws_account(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->update_aws_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an AWS integration
        api_response = api_instance.update_aws_account(body, account_id=account_id, role_name=role_name, access_key_id=access_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->update_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccount**](AWSAccount.md)| AWS request object |
 **account_id** | **str**| Only return AWS accounts that matches this &#x60;account_id&#x60;. | [optional]
 **role_name** | **str**| Only return AWS accounts that match this &#x60;role_name&#x60;. Required if &#x60;account_id&#x60; is specified. | [optional]
 **access_key_id** | **str**| Only return AWS accounts that matches this &#x60;access_key_id&#x60;. Required if none of the other two options are specified. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
**409** | Conflict Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

