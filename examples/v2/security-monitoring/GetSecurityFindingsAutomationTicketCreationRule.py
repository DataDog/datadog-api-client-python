"""
Get a ticket creation rule returns "Successfully retrieved the ticket creation rule" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "valid_ticket_creation_rule" in the system
VALID_TICKET_CREATION_RULE_DATA_ID = environ["VALID_TICKET_CREATION_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_security_findings_automation_ticket_creation_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_findings_automation_ticket_creation_rule(
        rule_id=VALID_TICKET_CREATION_RULE_DATA_ID,
    )

    print(response)
