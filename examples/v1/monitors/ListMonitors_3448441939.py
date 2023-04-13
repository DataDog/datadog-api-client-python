"""
Get all monitor details with tags
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors(
        tags="test:examplemonitor",
        page_size=1,
    )

    print(response)
