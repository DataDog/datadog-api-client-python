"""
Get all monitor notification rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_notification_rules()

    print(response)
