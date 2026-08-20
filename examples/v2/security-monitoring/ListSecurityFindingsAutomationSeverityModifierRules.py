"""
Get all severity modifier rules returns "Successfully retrieved the list of severity modifier rules" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["list_security_findings_automation_severity_modifier_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_security_findings_automation_severity_modifier_rules()

    print(response)
