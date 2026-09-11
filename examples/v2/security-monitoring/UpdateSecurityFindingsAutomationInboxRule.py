"""
Update an inbox rule returns "Successfully updated the inbox rule" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
from datadog_api_client.v2.model.inbox_rule_action import InboxRuleAction
from datadog_api_client.v2.model.inbox_rule_attributes_create import InboxRuleAttributesCreate
from datadog_api_client.v2.model.inbox_rule_data_update import InboxRuleDataUpdate
from datadog_api_client.v2.model.inbox_rule_type import InboxRuleType
from datadog_api_client.v2.model.inbox_rule_update_request import InboxRuleUpdateRequest
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType

# there is a valid "valid_inbox_rule" in the system
VALID_INBOX_RULE_DATA_ID = environ["VALID_INBOX_RULE_DATA_ID"]

body = InboxRuleUpdateRequest(
    data=InboxRuleDataUpdate(
        attributes=InboxRuleAttributesCreate(
            action=InboxRuleAction(
                description="Needs triage",
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
        id=VALID_INBOX_RULE_DATA_ID,
        type=InboxRuleType.INBOX_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_security_findings_automation_inbox_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_findings_automation_inbox_rule(rule_id=VALID_INBOX_RULE_DATA_ID, body=body)

    print(response)
