import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_api
from datadog_api_client.v2.models import *
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
