"""
Create a security signal investigation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_investigation_request import (
    SecurityMonitoringSignalInvestigationRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_request_attributes import (
    SecurityMonitoringSignalInvestigationRequestAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_request_data import (
    SecurityMonitoringSignalInvestigationRequestData,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_type import (
    SecurityMonitoringSignalInvestigationType,
)

body = SecurityMonitoringSignalInvestigationRequest(
    data=SecurityMonitoringSignalInvestigationRequestData(
        attributes=SecurityMonitoringSignalInvestigationRequestAttributes(
            deployment="live",
            signal_id="AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
        ),
        type=SecurityMonitoringSignalInvestigationType.INVESTIGATION_SIGNAL,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_signal_investigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_signal_investigation(body=body)

    print(response)
