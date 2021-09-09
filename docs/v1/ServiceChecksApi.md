# datadog_api_client.v1.ServiceChecksApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_service_check**](ServiceChecksApi.md#submit_service_check) | **POST** /api/v1/check_run | Submit a Service Check


# **submit_service_check**
> IntakePayloadAccepted submit_service_check(body)

Submit a list of Service Checks.

**Note**: A valid API key is required.

### Example

* Api Key Authentication (apiKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_checks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_checks_api.ServiceChecksApi(api_client)
    body = ServiceChecks([
        ServiceCheck(
            check="app.ok",
            host_name="app.host1",
            message="app is running",
            status=ServiceCheckStatus(0),
            tags=["environment:test"],
            timestamp=1,
        ),
    ])  # ServiceChecks | Service Check request body.

    # example passing only required values which don't have defaults set
    try:
        # Submit a Service Check
        api_response = api_instance.submit_service_check(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceChecksApi->submit_service_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceChecks**](ServiceChecks.md)| Service Check request body. |

### Return type

[**IntakePayloadAccepted**](IntakePayloadAccepted.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Payload accepted |  -  |
**400** | Bad Request |  -  |
**403** | Authentication Error |  -  |
**408** | Request timeout |  -  |
**413** | Payload too large |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

