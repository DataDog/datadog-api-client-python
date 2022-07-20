"""
Get a synthetics monitor's details
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

# there is a valid "synthetics_api_test" in the system
SYNTHETICS_API_TEST_MONITOR_ID = environ["SYNTHETICS_API_TEST_MONITOR_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor(
        monitor_id=int(SYNTHETICS_API_TEST_MONITOR_ID),
    )

    print(response)
