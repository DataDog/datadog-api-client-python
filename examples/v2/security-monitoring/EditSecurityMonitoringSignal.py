"""
Update security signal triage state or assignee returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import SecurityMonitoringSignalArchiveReason
from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import SecurityMonitoringSignalMetadataType
from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState
from datadog_api_client.v2.model.security_monitoring_signal_update_attributes import (
    SecurityMonitoringSignalUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signal_update_data import SecurityMonitoringSignalUpdateData
from datadog_api_client.v2.model.security_monitoring_signal_update_request import SecurityMonitoringSignalUpdateRequest
from datadog_api_client.v2.model.security_monitoring_triage_user import SecurityMonitoringTriageUser

body = SecurityMonitoringSignalUpdateRequest(
    data=SecurityMonitoringSignalUpdateData(
        attributes=SecurityMonitoringSignalUpdateAttributes(
            archive_reason=SecurityMonitoringSignalArchiveReason.NONE,
            assignee=SecurityMonitoringTriageUser(
                uuid="773b045d-ccf8-4808-bd3b-955ef6a8c940",
            ),
            state=SecurityMonitoringSignalState.OPEN,
        ),
        type=SecurityMonitoringSignalMetadataType.SIGNAL_METADATA,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_signal(signal_id="signal_id", body=body)

    print(response)
