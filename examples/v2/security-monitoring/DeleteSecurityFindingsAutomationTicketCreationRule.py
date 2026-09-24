"""
Delete a ticket creation rule returns "Successfully deleted the ticket creation rule" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_security_findings_automation_ticket_creation_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_findings_automation_ticket_creation_rule(
        rule_id=UUID("00000000-0000-0000-0000-000000000000"),
    )
