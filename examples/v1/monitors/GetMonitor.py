"""
Get a monitor's details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor(
        monitor_id=int(MONITOR_ID),
    )

    print(response)
