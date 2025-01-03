"""
Search logs (GET) returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    items = api_instance.list_logs_get_with_pagination()
    for item in items:
        print(item)
