"""
Create an inbox rule returns "Successfully created the inbox rule" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
from datadog_api_client.v2.model.inbox_rule_action import InboxRuleAction
from datadog_api_client.v2.model.inbox_rule_attributes_create import InboxRuleAttributesCreate
from datadog_api_client.v2.model.inbox_rule_create_request import InboxRuleCreateRequest
from datadog_api_client.v2.model.inbox_rule_data_create import InboxRuleDataCreate
from datadog_api_client.v2.model.inbox_rule_type import InboxRuleType
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType

body = InboxRuleCreateRequest(
    data=InboxRuleDataCreate(
        attributes=InboxRuleAttributesCreate(
            action=InboxRuleAction(
                description="Needs triage",
            ),
            enabled=True,
            name="Example-Security-Monitoring",
            rule=AutomationRuleScope(
                finding_types=[
                    SecurityFindingType.MISCONFIGURATION,
                ],
                query="env:staging",
            ),
        ),
        type=InboxRuleType.INBOX_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_security_findings_automation_inbox_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_findings_automation_inbox_rule(body=body)

    print(response)
