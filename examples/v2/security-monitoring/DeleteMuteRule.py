"""
Delete a mute rule returns "Rule successfully deleted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "valid_mute_rule" in the system
VALID_MUTE_RULE_DATA_ID = environ["VALID_MUTE_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_mute_rule(
        mute_rule_id=VALID_MUTE_RULE_DATA_ID,
    )
