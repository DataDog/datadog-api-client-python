"""
Delete an existing rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "security_rule" in the system
SECURITY_RULE_ID = environ["SECURITY_RULE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_monitoring_rule(
        rule_id=SECURITY_RULE_ID,
    )
