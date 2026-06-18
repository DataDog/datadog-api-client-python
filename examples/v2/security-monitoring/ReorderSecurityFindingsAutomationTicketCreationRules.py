"""
Reorder ticket creation rules returns "Successfully reordered the ticket creation rules" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.ticket_creation_rule_reorder_item import TicketCreationRuleReorderItem
from datadog_api_client.v2.model.ticket_creation_rule_reorder_request import TicketCreationRuleReorderRequest
from datadog_api_client.v2.model.ticket_creation_rule_type import TicketCreationRuleType

# there is a valid "valid_ticket_creation_rule" in the system
VALID_TICKET_CREATION_RULE_DATA_ID = environ["VALID_TICKET_CREATION_RULE_DATA_ID"]

body = TicketCreationRuleReorderRequest(
    data=[
        TicketCreationRuleReorderItem(
            id=VALID_TICKET_CREATION_RULE_DATA_ID,
            type=TicketCreationRuleType.TICKET_CREATION_RULES,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["reorder_security_findings_automation_ticket_creation_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_security_findings_automation_ticket_creation_rules(body=body)

    print(response)
