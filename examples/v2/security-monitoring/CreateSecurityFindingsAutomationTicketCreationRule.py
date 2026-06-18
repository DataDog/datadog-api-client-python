"""
Create a ticket creation rule returns "Successfully created the ticket creation rule" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType
from datadog_api_client.v2.model.ticket_creation_rule_action import TicketCreationRuleAction
from datadog_api_client.v2.model.ticket_creation_rule_attributes_create import TicketCreationRuleAttributesCreate
from datadog_api_client.v2.model.ticket_creation_rule_create_request import TicketCreationRuleCreateRequest
from datadog_api_client.v2.model.ticket_creation_rule_data_create import TicketCreationRuleDataCreate
from datadog_api_client.v2.model.ticket_creation_rule_type import TicketCreationRuleType
from datadog_api_client.v2.model.ticket_creation_target import TicketCreationTarget
from uuid import UUID

body = TicketCreationRuleCreateRequest(
    data=TicketCreationRuleDataCreate(
        attributes=TicketCreationRuleAttributesCreate(
            action=TicketCreationRuleAction(
                max_tickets_per_day=10,
                project_id=UUID("11111111-1111-1111-1111-111111111111"),
                target=TicketCreationTarget.JIRA,
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
        type=TicketCreationRuleType.TICKET_CREATION_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_security_findings_automation_ticket_creation_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_findings_automation_ticket_creation_rule(body=body)

    print(response)
