# datadog_api_client.v1.LogsApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                  | HTTP request                       | Description |
| --------------------------------------- | ---------------------------------- | ----------- |
| [**list_logs**](LogsApi.md#list_logs)   | **POST** /api/v1/logs-queries/list | Search logs |
| [**submit_log**](LogsApi.md#submit_log) | **POST** /v1/input                 | Send logs   |

# **list_logs**

> LogsListResponse list_logs(body)

List endpoint returns logs that match a log search query.
[Results are paginated][1].

**If you are considering archiving logs for your organization,
consider use of the Datadog archive capabilities instead of the log list API.
See [Datadog Logs Archive documentation][2].**

[1]: /logs/guide/collect-multiple-logs-with-pagination
[2]: https://docs.datadoghq.com/logs/archives

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    body = LogsListRequest(
        index="retention-3,retention-15",
        limit=1,
        query="service:web* AND @http.status_code:[200 TO 299]",
        sort=LogsSort("asc"),
        start_at="start_at_example",
        time=LogsListRequestTime(
            _from=dateutil_parser('2020-02-02T02:02:02Z'),
            timezone="timezone_example",
            to=dateutil_parser('2020-02-02T20:20:20Z'),
        ),
    )  # LogsListRequest | Logs filter

    # example passing only required values which don't have defaults set
    try:
        # Search logs
        api_response = api_instance.list_logs(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)
```

### Parameters

| Name     | Type                                      | Description | Notes |
| -------- | ----------------------------------------- | ----------- | ----- |
| **body** | [**LogsListRequest**](LogsListRequest.md) | Logs filter |

### Return type

[**LogsListResponse**](LogsListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description          | Response headers |
| ----------- | -------------------- | ---------------- |
| **200**     | OK                   | -                |
| **400**     | Bad Request          | -                |
| **403**     | Authentication error | -                |
| **429**     | Too many requests    | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **submit_log**

> dict submit_log(body)

Send your logs to your Datadog platform over HTTP. Limits per HTTP request are:

- Maximum content size per payload (uncompressed): 5MB
- Maximum size for a single log: 1MB
- Maximum array size if sending multiple logs in an array: 1000 entries

Any log exceeding 1MB is accepted and truncated by Datadog:

- For a single log request, the API truncates the log at 1MB and returns a 2xx.
- For a multi-logs request, the API processes all logs, truncates only logs larger than 1MB, and returns a 2xx.

Datadog recommends sending your logs compressed.
Add the `Content-Encoding: gzip` header to the request when sending compressed logs.

The status codes answered by the HTTP API are:

- 200: OK
- 400: Bad request (likely an issue in the payload formatting)
- 403: Permission issue (likely using an invalid API Key)
- 413: Payload too large (batch is above 5MB uncompressed)
- 5xx: Internal error, request should be retried after some time

### Example

- Api Key Authentication (apiKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    body = HTTPLog([
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
            service="payment",
        ),
    ])  # HTTPLog | Log to send (JSON format).
    content_encoding = ContentEncoding("gzip")  # ContentEncoding | HTTP header used to compress the media-type. (optional)
    ddtags = "env:prod,user:my-user"  # str | Log tags can be passed as query parameters with `text/plain` content type. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send logs
        api_response = api_instance.submit_log(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->submit_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send logs
        api_response = api_instance.submit_log(body, content_encoding=content_encoding, ddtags=ddtags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->submit_log: %s\n" % e)
```

### Parameters

| Name                 | Type                      | Description                                                                          | Notes      |
| -------------------- | ------------------------- | ------------------------------------------------------------------------------------ | ---------- |
| **body**             | [**HTTPLog**](HTTPLog.md) | Log to send (JSON format).                                                           |
| **content_encoding** | **ContentEncoding**       | HTTP header used to compress the media-type.                                         | [optional] |
| **ddtags**           | **str**                   | Log tags can be passed as query parameters with &#x60;text/plain&#x60; content type. | [optional] |

### Return type

**dict**

### Authorization

[apiKeyAuth](README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/logplex-1, text/plain
- **Accept**: application/json

### HTTP response details

| Status code | Description                                   | Response headers |
| ----------- | --------------------------------------------- | ---------------- |
| **200**     | Response from server (always 200 empty JSON). | -                |
| **400**     | unexpected error                              | -                |
| **429**     | Too many requests                             | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
