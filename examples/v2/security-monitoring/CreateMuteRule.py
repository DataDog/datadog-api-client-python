"""
Create a new mute rule returns "Successfully created the mute rule" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.action_mute import ActionMute
from datadog_api_client.v2.model.automation_rule import AutomationRule
from datadog_api_client.v2.model.create_mute_rule_parameters import CreateMuteRuleParameters
from datadog_api_client.v2.model.create_mute_rule_parameters_data import CreateMuteRuleParametersData
from datadog_api_client.v2.model.create_mute_rule_parameters_data_attributes import (
    CreateMuteRuleParametersDataAttributes,
)
from datadog_api_client.v2.model.issue_type import IssueType
from datadog_api_client.v2.model.mute_reason import MuteReason
from datadog_api_client.v2.model.mute_rules_type import MuteRulesType
from datadog_api_client.v2.model.security_rule_severity import SecurityRuleSeverity
from datadog_api_client.v2.model.security_rule_types_items import SecurityRuleTypesItems

body = CreateMuteRuleParameters(
    data=CreateMuteRuleParametersData(
        attributes=CreateMuteRuleParametersDataAttributes(
            action=ActionMute(
                expire_at=1893452400000,
                reason=MuteReason.DUPLICATE,
                reason_description="Muting for a while",
            ),
            enabled=True,
            name="Rule 1",
            rule=AutomationRule(
                issue_type=IssueType.VULNERABILITY,
                query="key:val",
                rule_ids=[
                    "rule-id-1",
                ],
                rule_types=[
                    SecurityRuleTypesItems.APPLICATION_CODE_VULNERABILITY,
                ],
                severities=[
                    SecurityRuleSeverity.CRITICAL,
                ],
            ),
        ),
        type=MuteRulesType.MUTE_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_mute_rule(body=body)

    print(response)
