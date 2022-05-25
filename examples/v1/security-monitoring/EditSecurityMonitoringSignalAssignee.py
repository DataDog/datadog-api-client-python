"""
Modify the triage assignee of a security signal returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v1.model.signal_assignee_update_request import SignalAssigneeUpdateRequest

body = SignalAssigneeUpdateRequest(
    assignee="773b045d-ccf8-4808-bd3b-955ef6a8c940",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_signal_assignee(
        signal_id="AQAAAYDiB_Ol8PbzFAAAAABBWURpQl9PbEFBQU0yeXhGTG9ZV2JnQUE", body=body
    )

    print(response)
