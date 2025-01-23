"""
Patch an inbox rule returns "Inbox rule successfully patched" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.action_inbox import ActionInbox
from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType
from datadog_api_client.v2.model.issue_type import IssueType
from datadog_api_client.v2.model.patch_inbox_rules_parameters import PatchInboxRulesParameters
from datadog_api_client.v2.model.patch_inbox_rules_parameters_data import PatchInboxRulesParametersData
from datadog_api_client.v2.model.patch_inbox_rules_parameters_data_attributes import (
    PatchInboxRulesParametersDataAttributes,
)
from datadog_api_client.v2.model.rule import Rule
from datadog_api_client.v2.model.rule_severity import RuleSeverity
from datadog_api_client.v2.model.rule_types_items import RuleTypesItems

# there is a valid "valid_inbox_rule" in the system
VALID_INBOX_RULE_DATA_ID = environ["VALID_INBOX_RULE_DATA_ID"]

body = PatchInboxRulesParameters(
    data=PatchInboxRulesParametersData(
        attributes=PatchInboxRulesParametersDataAttributes(
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
        id=VALID_INBOX_RULE_DATA_ID,
        type=InboxRulesType.INBOX_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.patch_inbox_rule(inbox_rule_id=VALID_INBOX_RULE_DATA_ID, body=body)

    print(response)
