"""
Search logs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.logs_list_request import LogsListRequest
from datadog_api_client.v1.model.logs_list_request_time import LogsListRequestTime
from datadog_api_client.v1.model.logs_sort import LogsSort
from datetime import datetime
from dateutil.tz import tzutc

body = LogsListRequest(
    index="retention-3,retention-15",
    query="service:web* AND @http.status_code:[200 TO 299]",
    sort=LogsSort.TIME_ASCENDING,
    time=LogsListRequestTime(
        _from=datetime(2020, 2, 2, 2, 2, 2, 202000, tzinfo=tzutc()),
        to=datetime(2020, 2, 20, 2, 2, 2, 202000, tzinfo=tzutc()),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs(body=body)

    print(response)
