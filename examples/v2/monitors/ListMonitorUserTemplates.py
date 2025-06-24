"""
Get all monitor user templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
configuration.unstable_operations["list_monitor_user_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitor_user_templates()

    print(response)
