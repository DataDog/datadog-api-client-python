"""
Get an inbox rule returns "Successfully retrieved the inbox rule" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "valid_inbox_rule" in the system
VALID_INBOX_RULE_DATA_ID = environ["VALID_INBOX_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_security_findings_automation_inbox_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_findings_automation_inbox_rule(
        rule_id=VALID_INBOX_RULE_DATA_ID,
    )

    print(response)
