"""
Get all monitor details returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    items = api_instance.list_monitors_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
