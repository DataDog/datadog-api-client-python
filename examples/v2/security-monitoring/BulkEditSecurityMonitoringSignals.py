"""
Bulk update security signals returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import SecurityMonitoringSignalArchiveReason
from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState
from datadog_api_client.v2.model.security_monitoring_signal_type import SecurityMonitoringSignalType
from datadog_api_client.v2.model.security_monitoring_signal_update_attributes import (
    SecurityMonitoringSignalUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_update_data import (
    SecurityMonitoringSignalsBulkUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_update_request import (
    SecurityMonitoringSignalsBulkUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_triage_user import SecurityMonitoringTriageUser

body = SecurityMonitoringSignalsBulkUpdateRequest(
    data=[
        SecurityMonitoringSignalsBulkUpdateData(
            attributes=SecurityMonitoringSignalUpdateAttributes(
                archive_reason=SecurityMonitoringSignalArchiveReason.NONE,
                assignee=SecurityMonitoringTriageUser(
                    uuid="773b045d-ccf8-4808-bd3b-955ef6a8c940",
                ),
                state=SecurityMonitoringSignalState.OPEN,
            ),
            id="AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
            type=SecurityMonitoringSignalType.SIGNAL,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_edit_security_monitoring_signals(body=body)

    print(response)
