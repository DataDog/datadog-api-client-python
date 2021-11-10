"""
Get all monitor details returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

with ApiClient(Configuration()) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors()

    print(response)
