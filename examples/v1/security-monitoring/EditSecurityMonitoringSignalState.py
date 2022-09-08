"""
Change the triage state of a security signal returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v1.model.signal_archive_reason import SignalArchiveReason
from datadog_api_client.v1.model.signal_state_update_request import SignalStateUpdateRequest
from datadog_api_client.v1.model.signal_triage_state import SignalTriageState

body = SignalStateUpdateRequest(
    archive_reason=SignalArchiveReason.NONE,
    state=SignalTriageState.OPEN,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_signal_state(
        signal_id="AQAAAYDiB_Ol8PbzFAAAAABBWURpQl9PbEFBQU0yeXhGTG9ZV2JnQUE", body=body
    )

    print(response)
