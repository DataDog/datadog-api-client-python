"""
Bulk update triage assignee of security signals returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_type import SecurityMonitoringSignalType
from datadog_api_client.v2.model.security_monitoring_signals_bulk_assignee_update_attributes import (
    SecurityMonitoringSignalsBulkAssigneeUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_assignee_update_data import (
    SecurityMonitoringSignalsBulkAssigneeUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_assignee_update_request import (
    SecurityMonitoringSignalsBulkAssigneeUpdateRequest,
)

body = SecurityMonitoringSignalsBulkAssigneeUpdateRequest(
    data=[
        SecurityMonitoringSignalsBulkAssigneeUpdateData(
            attributes=SecurityMonitoringSignalsBulkAssigneeUpdateAttributes(
                assignee="773b045d-ccf8-4808-bd3b-955ef6a8c940",
            ),
            id="AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
            type=SecurityMonitoringSignalType.SIGNAL,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_edit_security_monitoring_signals_assignee(body=body)

    print(response)
