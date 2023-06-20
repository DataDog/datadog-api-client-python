"""
Change the triage state of a security signal returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import SecurityMonitoringSignalArchiveReason
from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState
from datadog_api_client.v2.model.security_monitoring_signal_state_update_request import (
    SecurityMonitoringSignalStateUpdateRequestJSON,
)

body = SecurityMonitoringSignalStateUpdateRequestJSON(
    archive_reason=SecurityMonitoringSignalArchiveReason.NONE,
    state=SecurityMonitoringSignalState.OPEN,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_signal_state(
        signal_id="AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE", body=body
    )

    print(response)
