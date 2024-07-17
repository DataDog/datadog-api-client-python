"""
Get the list of devices returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.list_devices(
        page_number=0,
        page_size=1,
        filter_tag="device_namespace:default",
    )

    print(response)
