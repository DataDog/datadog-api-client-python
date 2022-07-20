"""
Send logs returns "Request accepted for processing (always 202 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
            service="payment",
            status="error",
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(body=body)

    print(response)
