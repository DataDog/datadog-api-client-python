"""
Send deflate logs returns "Response from server (always 200 empty JSON)." response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.http_log import HTTPLog
from datadog_api_client.v1.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            message="Test-Example-Send_deflate_logs_returns_Response_from_server_always_200_empty_JSON_response",
            ddtags="host:TestExampleSenddeflatelogsreturnsResponsefromserveralways200emptyJSONresponse",
        )
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding="deflate", body=body)

    print(response)
