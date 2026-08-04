"""
Delete a severity modifier rule returns "Rule successfully deleted." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "valid_severity_modifier_rule" in the system
VALID_SEVERITY_MODIFIER_RULE_DATA_ID = environ["VALID_SEVERITY_MODIFIER_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_security_findings_automation_severity_modifier_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_findings_automation_severity_modifier_rule(
        rule_id=VALID_SEVERITY_MODIFIER_RULE_DATA_ID,
    )
