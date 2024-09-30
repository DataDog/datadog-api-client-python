"""
Get the list of tags for a device returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.list_device_user_tags(
        device_id="default_device",
    )

    print(response)
