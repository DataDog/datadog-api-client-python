"""
Enable a default inbox rule returns "Successfully enabled the default inbox rule" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["enable_security_findings_automation_default_inbox_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.enable_security_findings_automation_default_inbox_rule(
        rule_id="secret_default_rule",
    )

    print(response)
