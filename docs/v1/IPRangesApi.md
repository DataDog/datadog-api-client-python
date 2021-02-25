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
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import ip_ranges_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ip_ranges_api.IPRangesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List IP Ranges
        api_response = api_instance.get_ip_ranges()
        pprint(api_response)
    except ApiException as e:
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

