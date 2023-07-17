"""
Get all downtimes for a monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

configuration = Configuration()
configuration.unstable_operations["list_monitor_downtimes"] = True
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.list_monitor_downtimes(
        monitor_id=35534610,
    )

    print(response)
