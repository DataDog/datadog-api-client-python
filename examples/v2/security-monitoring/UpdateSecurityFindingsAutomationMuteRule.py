"""
Update a mute rule returns "Successfully updated the mute rule" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
from datadog_api_client.v2.model.mute_reason import MuteReason
from datadog_api_client.v2.model.mute_rule_action import MuteRuleAction
from datadog_api_client.v2.model.mute_rule_attributes_create import MuteRuleAttributesCreate
from datadog_api_client.v2.model.mute_rule_data_create import MuteRuleDataCreate
from datadog_api_client.v2.model.mute_rule_type import MuteRuleType
from datadog_api_client.v2.model.mute_rule_update_request import MuteRuleUpdateRequest
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType

# there is a valid "valid_mute_rule" in the system
VALID_MUTE_RULE_DATA_ID = environ["VALID_MUTE_RULE_DATA_ID"]

body = MuteRuleUpdateRequest(
    data=MuteRuleDataCreate(
        attributes=MuteRuleAttributesCreate(
            action=MuteRuleAction(
                reason=MuteReason.FALSE_POSITIVE,
            ),
            enabled=False,
            name="Example-Security-Monitoring",
            rule=AutomationRuleScope(
                finding_types=[
                    SecurityFindingType.MISCONFIGURATION,
                ],
                query="env:staging",
            ),
        ),
        type=MuteRuleType.MUTE_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_security_findings_automation_mute_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_findings_automation_mute_rule(rule_id=VALID_MUTE_RULE_DATA_ID, body=body)

    print(response)
