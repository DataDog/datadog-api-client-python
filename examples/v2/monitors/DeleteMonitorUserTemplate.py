"""
Delete a monitor user template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
configuration.unstable_operations["delete_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.delete_monitor_user_template(
        template_id="template_id",
    )
