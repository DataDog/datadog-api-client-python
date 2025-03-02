"""
Get rule version history returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "security_rule" in the system
SECURITY_RULE_ID = environ["SECURITY_RULE_ID"]

configuration = Configuration()
configuration.unstable_operations["get_rule_version_history"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_rule_version_history(
        rule_id=SECURITY_RULE_ID,
    )

    print(response)
