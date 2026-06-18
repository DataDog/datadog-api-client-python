"""
Get all ticket creation rules returns "Successfully retrieved the list of ticket creation rules" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["list_security_findings_automation_ticket_creation_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_security_findings_automation_ticket_creation_rules()

    print(response)
