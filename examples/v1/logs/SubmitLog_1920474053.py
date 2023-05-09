"""
Send gzip logs returns "Response from server (always 200 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.content_encoding import ContentEncoding
from datadog_api_client.v1.model.http_log_item import HTTPLogItem

body = [
    HTTPLogItem(
        message="Example-Log",
        ddtags="host:ExampleLog",
    ),
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding=ContentEncoding.GZIP, body=body)

    print(response)
