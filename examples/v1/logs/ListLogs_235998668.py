"""
Search test logs returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_api import LogsApi
from datadog_api_client.v1.model.logs_list_request import LogsListRequest
from datadog_api_client.v1.model.logs_list_request_time import LogsListRequestTime
from datadog_api_client.v1.model.logs_sort import LogsSort

body = LogsListRequest(
    index="main",
    query="host:Test*",
    sort=LogsSort.TIME_ASCENDING,
    time=LogsListRequestTime(
        _from=(datetime.now() + relativedelta(hours=-1)),
        timezone="Europe/Paris",
        to=datetime.now(),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs(body=body)

    print(response)
