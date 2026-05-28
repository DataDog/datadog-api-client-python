"""
Get all device issue definitions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.end_user_device_monitoring_api import EndUserDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EndUserDeviceMonitoringApi(api_client)
    response = api_instance.get_eudm_issues()

    print(response)
