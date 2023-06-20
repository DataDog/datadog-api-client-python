"""
Modify the triage assignee of a security signal returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_assignee_update_request import (
    SecurityMonitoringSignalAssigneeUpdateRequestJSON,
)
from datadog_api_client.v2.model.security_monitoring_triage_user import SecurityMonitoringTriageUser

body = SecurityMonitoringSignalAssigneeUpdateRequestJSON(
    assignee=SecurityMonitoringTriageUser(
        uuid="",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_signal_assignee(
        signal_id="AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE", body=body
    )

    print(response)
