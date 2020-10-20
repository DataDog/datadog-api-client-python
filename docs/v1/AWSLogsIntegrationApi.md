# datadog_api_client.v1.AWSLogsIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_aws_logs_lambda_async**](AWSLogsIntegrationApi.md#check_aws_logs_lambda_async) | **POST** /api/v1/integration/aws/logs/check_async | Check that an AWS Lambda Function exists
[**check_aws_logs_services_async**](AWSLogsIntegrationApi.md#check_aws_logs_services_async) | **POST** /api/v1/integration/aws/logs/services_async | Check permissions for log services
[**create_aws_lambda_arn**](AWSLogsIntegrationApi.md#create_aws_lambda_arn) | **POST** /api/v1/integration/aws/logs | Add AWS Log Lambda ARN
[**delete_aws_lambda_arn**](AWSLogsIntegrationApi.md#delete_aws_lambda_arn) | **DELETE** /api/v1/integration/aws/logs | Delete an AWS Logs integration
[**enable_aws_log_services**](AWSLogsIntegrationApi.md#enable_aws_log_services) | **POST** /api/v1/integration/aws/logs/services | Enable an AWS Logs integration
[**list_aws_logs_integrations**](AWSLogsIntegrationApi.md#list_aws_logs_integrations) | **GET** /api/v1/integration/aws/logs | List all AWS Logs integrations
[**list_aws_logs_services**](AWSLogsIntegrationApi.md#list_aws_logs_services) | **GET** /api/v1/integration/aws/logs/services | Get list of AWS log ready services


# **check_aws_logs_lambda_async**
> AWSLogsAsyncResponse check_aws_logs_lambda_async(body)

Check that an AWS Lambda Function exists

Test if permissions are present to add a log-forwarding triggers for the given services and AWS account. The input is the same as for Enable an AWS service log collection. Subsequent requests will always repeat the above, so this endpoint can be polled intermittently instead of blocking.  - Returns a status of 'created' when it's checking if the Lambda exists in the account. - Returns a status of 'waiting' while checking. - Returns a status of 'checked and ok' if the Lambda exists. - Returns a status of 'error' if the Lambda does not exist.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)
    body = AWSAccountAndLambdaRequest(
        account_id="1234567",
        lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    ) # AWSAccountAndLambdaRequest | Check AWS Log Lambda Async request body.

    # example passing only required values which don't have defaults set
    try:
        # Check that an AWS Lambda Function exists
        api_response = api_instance.check_aws_logs_lambda_async(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->check_aws_logs_lambda_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccountAndLambdaRequest**](AWSAccountAndLambdaRequest.md)| Check AWS Log Lambda Async request body. |

### Return type

[**AWSLogsAsyncResponse**](AWSLogsAsyncResponse.md)

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

# **check_aws_logs_services_async**
> AWSLogsAsyncResponse check_aws_logs_services_async(body)

Check permissions for log services

Test if permissions are present to add log-forwarding triggers for the given services and AWS account. Input is the same as for `EnableAWSLogServices`. Done async, so can be repeatedly polled in a non-blocking fashion until the async request completes.  - Returns a status of `created` when it's checking if the permissions exists   in the AWS account. - Returns a status of `waiting` while checking. - Returns a status of `checked and ok` if the Lambda exists. - Returns a status of `error` if the Lambda does not exist.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)
    body = AWSLogsServicesRequest(
        account_id="1234567",
        services=[
            "["s3","elb","elbv2","cloudfront","redshift","lambda"]",
        ],
    ) # AWSLogsServicesRequest | Check AWS Logs Async Services request body.

    # example passing only required values which don't have defaults set
    try:
        # Check permissions for log services
        api_response = api_instance.check_aws_logs_services_async(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->check_aws_logs_services_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSLogsServicesRequest**](AWSLogsServicesRequest.md)| Check AWS Logs Async Services request body. |

### Return type

[**AWSLogsAsyncResponse**](AWSLogsAsyncResponse.md)

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

# **create_aws_lambda_arn**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_aws_lambda_arn(body)

Add AWS Log Lambda ARN

Attach the Lambda ARN of the Lambda created for the Datadog-AWS log collection to your AWS account ID to enable log collection.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)
    body = AWSAccountAndLambdaRequest(
        account_id="1234567",
        lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    ) # AWSAccountAndLambdaRequest | AWS Log Lambda Async request body.

    # example passing only required values which don't have defaults set
    try:
        # Add AWS Log Lambda ARN
        api_response = api_instance.create_aws_lambda_arn(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->create_aws_lambda_arn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccountAndLambdaRequest**](AWSAccountAndLambdaRequest.md)| AWS Log Lambda Async request body. |

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

# **delete_aws_lambda_arn**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_aws_lambda_arn(body)

Delete an AWS Logs integration

Delete a Datadog-AWS logs configuration by removing the specific Lambda ARN associated with a given AWS account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)
    body = AWSAccountAndLambdaRequest(
        account_id="1234567",
        lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    ) # AWSAccountAndLambdaRequest | Delete AWS Lambda ARN request body.

    # example passing only required values which don't have defaults set
    try:
        # Delete an AWS Logs integration
        api_response = api_instance.delete_aws_lambda_arn(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->delete_aws_lambda_arn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSAccountAndLambdaRequest**](AWSAccountAndLambdaRequest.md)| Delete AWS Lambda ARN request body. |

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

# **enable_aws_log_services**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enable_aws_log_services(body)

Enable an AWS Logs integration

Enable automatic log collection for a list of services. This should be run after running `CreateAWSLambdaARN` to save the configuration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)
    body = AWSLogsServicesRequest(
        account_id="1234567",
        services=[
            "["s3","elb","elbv2","cloudfront","redshift","lambda"]",
        ],
    ) # AWSLogsServicesRequest | Enable AWS Log Services request body.

    # example passing only required values which don't have defaults set
    try:
        # Enable an AWS Logs integration
        api_response = api_instance.enable_aws_log_services(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->enable_aws_log_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AWSLogsServicesRequest**](AWSLogsServicesRequest.md)| Enable AWS Log Services request body. |

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

# **list_aws_logs_integrations**
> [AWSLogsListResponse] list_aws_logs_integrations()

List all AWS Logs integrations

List all Datadog-AWS Logs integrations configured in your Datadog account.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all AWS Logs integrations
        api_response = api_instance.list_aws_logs_integrations()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->list_aws_logs_integrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[AWSLogsListResponse]**](AWSLogsListResponse.md)

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

# **list_aws_logs_services**
> [AWSLogsListServicesResponse] list_aws_logs_services()

Get list of AWS log ready services

Get the list of current AWS services that Datadog offers automatic log collection. Use returned service IDs with the services parameter for the Enable an AWS service log collection API endpoint.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_logs_integration_api
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
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of AWS log ready services
        api_response = api_instance.list_aws_logs_services()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->list_aws_logs_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[AWSLogsListServicesResponse]**](AWSLogsListServicesResponse.md)

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

