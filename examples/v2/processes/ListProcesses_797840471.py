"""
Get all processes returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.processes_api import ProcessesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProcessesApi(api_client)
    items = api_instance.list_processes_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
