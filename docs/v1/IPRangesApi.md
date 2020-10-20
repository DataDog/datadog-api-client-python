# datadog_api_client.v1.IPRangesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_ranges**](IPRangesApi.md#get_ip_ranges) | **GET** / | List IP Ranges


# **get_ip_ranges**
> IPRanges get_ip_ranges()

List IP Ranges

Get information about Datadog IP ranges.

### Example

```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import ip_ranges_api
from datadog_api_client.v1.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com"
)


# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ip_ranges_api.IPRangesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List IP Ranges
        api_response = api_instance.get_ip_ranges()
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling IPRangesApi->get_ip_ranges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IPRanges**](IPRanges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

