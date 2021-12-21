"""
Get a quick list of logs returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs_get(
        filter_query="datadog-agent",
        filter_index="main",
        filter_from="2020-09-17T11:48:36+01:00",
        filter_to="2020-09-17T12:48:36+01:00",
        page_limit=5,
    )

    print(response)
