"""
Bulk update triage state of security signals returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import SecurityMonitoringSignalArchiveReason
from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState
from datadog_api_client.v2.model.security_monitoring_signal_state_update_attributes import (
    SecurityMonitoringSignalStateUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signal_type import SecurityMonitoringSignalType
from datadog_api_client.v2.model.security_monitoring_signals_bulk_state_update_data import (
    SecurityMonitoringSignalsBulkStateUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_state_update_request import (
    SecurityMonitoringSignalsBulkStateUpdateRequest,
)

body = SecurityMonitoringSignalsBulkStateUpdateRequest(
    data=[
        SecurityMonitoringSignalsBulkStateUpdateData(
            attributes=SecurityMonitoringSignalStateUpdateAttributes(
                archive_reason=SecurityMonitoringSignalArchiveReason.NONE,
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
    response = api_instance.bulk_edit_security_monitoring_signals_state(body=body)

    print(response)
