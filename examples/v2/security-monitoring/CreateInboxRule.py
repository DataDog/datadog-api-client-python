"""
Create a new inbox rule returns "Successfully created the inbox rule" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.action_inbox import ActionInbox
from datadog_api_client.v2.model.create_inbox_rule_parameters import CreateInboxRuleParameters
from datadog_api_client.v2.model.create_inbox_rule_parameters_data import CreateInboxRuleParametersData
from datadog_api_client.v2.model.create_inbox_rule_parameters_data_attributes import (
    CreateInboxRuleParametersDataAttributes,
)
from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType
from datadog_api_client.v2.model.issue_type import IssueType
from datadog_api_client.v2.model.rule import Rule
from datadog_api_client.v2.model.rule_severity import RuleSeverity
from datadog_api_client.v2.model.rule_types_items import RuleTypesItems

body = CreateInboxRuleParameters(
    data=CreateInboxRuleParametersData(
        attributes=CreateInboxRuleParametersDataAttributes(
            action=ActionInbox(
                reason_description="We want to focus on these items.",
            ),
            enabled=True,
            name="Rule 1",
            rule=Rule(
                issue_type=IssueType.VULNERABILITY,
                query="key:val",
                rule_ids=[
                    "rule-id-1",
                ],
                rule_types=[
                    RuleTypesItems.APPLICATION_CODE_VULNERABILITY,
                ],
                severities=[
                    RuleSeverity.CRITICAL,
                ],
            ),
        ),
        type=InboxRulesType.INBOX_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_inbox_rule(body=body)

    print(response)
