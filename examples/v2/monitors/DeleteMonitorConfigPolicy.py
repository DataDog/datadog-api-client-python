"""
Delete a monitor configuration policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = environ["MONITOR_CONFIGURATION_POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.delete_monitor_config_policy(
        policy_id=MONITOR_CONFIGURATION_POLICY_DATA_ID,
    )
