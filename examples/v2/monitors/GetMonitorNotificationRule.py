"""
Get a monitor notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_notification_rule(
        rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID,
    )

    print(response)
