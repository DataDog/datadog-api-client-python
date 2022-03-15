"""
Search logs returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.logs_list_request import LogsListRequest
from datadog_api_client.v1.model.logs_list_request_time import LogsListRequestTime
from datadog_api_client.v1.model.logs_sort import LogsSort

body = LogsListRequest(
    index="main",
    limit=5,
    query="service:web* AND @http.status_code:[200 TO 299]",
    sort=LogsSort("asc"),
    time=LogsListRequestTime(
        _from=(datetime.now() + relativedelta(days=-1)).timestamp(),
        timezone="Europe/Paris",
        to=datetime.now().timestamp(),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs(body=body)

    print(response)
