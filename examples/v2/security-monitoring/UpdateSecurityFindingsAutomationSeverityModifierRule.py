"""
Update a severity modifier rule returns "Successfully updated the severity modifier rule" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType
from datadog_api_client.v2.model.severity_modifier_rule_attributes_create import SeverityModifierRuleAttributesCreate
from datadog_api_client.v2.model.severity_modifier_rule_data_create import SeverityModifierRuleDataCreate
from datadog_api_client.v2.model.severity_modifier_rule_set_action import SeverityModifierRuleSetAction
from datadog_api_client.v2.model.severity_modifier_rule_set_action_type import SeverityModifierRuleSetActionType
from datadog_api_client.v2.model.severity_modifier_rule_type import SeverityModifierRuleType
from datadog_api_client.v2.model.severity_modifier_rule_update_request import SeverityModifierRuleUpdateRequest
from datadog_api_client.v2.model.severity_modifier_severity import SeverityModifierSeverity

# there is a valid "valid_severity_modifier_rule" in the system
VALID_SEVERITY_MODIFIER_RULE_DATA_ID = environ["VALID_SEVERITY_MODIFIER_RULE_DATA_ID"]

body = SeverityModifierRuleUpdateRequest(
    data=SeverityModifierRuleDataCreate(
        attributes=SeverityModifierRuleAttributesCreate(
            action=SeverityModifierRuleSetAction(
                description="Lower severity for dev environment noise",
                severity=SeverityModifierSeverity.LOW,
                type=SeverityModifierRuleSetActionType.SET,
            ),
            enabled=True,
            name="Downgrade misconfigurations in dev",
            rule=AutomationRuleScope(
                finding_types=[
                    SecurityFindingType.MISCONFIGURATION,
                ],
                query="env:prod team:platform",
            ),
        ),
        type=SeverityModifierRuleType.SEVERITY_MODIFIER_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_security_findings_automation_severity_modifier_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_findings_automation_severity_modifier_rule(
        rule_id=VALID_SEVERITY_MODIFIER_RULE_DATA_ID, body=body
    )

    print(response)
