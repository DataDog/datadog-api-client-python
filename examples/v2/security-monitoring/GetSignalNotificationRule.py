"""
Get details of a signal-based notification rule returns "Notification rule details." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "valid_signal_notification_rule" in the system
VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID = environ["VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_signal_notification_rule(
        id=VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID,
    )

    print(response)
