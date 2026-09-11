"""
Delete a due date rule returns "Rule successfully deleted." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "valid_due_date_rule" in the system
VALID_DUE_DATE_RULE_DATA_ID = environ["VALID_DUE_DATE_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_security_findings_automation_due_date_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_findings_automation_due_date_rule(
        rule_id=VALID_DUE_DATE_RULE_DATA_ID,
    )
