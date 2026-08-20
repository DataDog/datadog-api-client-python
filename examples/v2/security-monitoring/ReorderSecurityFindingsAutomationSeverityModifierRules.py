"""
Reorder severity modifier rules returns "Successfully reordered the severity modifier rules" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.severity_modifier_rule_reorder_item import SeverityModifierRuleReorderItem
from datadog_api_client.v2.model.severity_modifier_rule_reorder_request import SeverityModifierRuleReorderRequest
from datadog_api_client.v2.model.severity_modifier_rule_type import SeverityModifierRuleType

# there is a valid "valid_severity_modifier_rule" in the system
VALID_SEVERITY_MODIFIER_RULE_DATA_ID = environ["VALID_SEVERITY_MODIFIER_RULE_DATA_ID"]

body = SeverityModifierRuleReorderRequest(
    data=[
        SeverityModifierRuleReorderItem(
            id=VALID_SEVERITY_MODIFIER_RULE_DATA_ID,
            type=SeverityModifierRuleType.SEVERITY_MODIFIER_RULES,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["reorder_security_findings_automation_severity_modifier_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_security_findings_automation_severity_modifier_rules(body=body)

    print(response)
