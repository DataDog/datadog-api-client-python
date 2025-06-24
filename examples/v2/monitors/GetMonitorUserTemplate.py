"""
Get a monitor user template returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = environ["MONITOR_USER_TEMPLATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_user_template(
        template_id=MONITOR_USER_TEMPLATE_DATA_ID,
    )

    print(response)
