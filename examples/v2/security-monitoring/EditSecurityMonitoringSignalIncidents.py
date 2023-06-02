"""
Change the related incidents of a security signal returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_incident_ids import SecurityMonitoringSignalIncidentIds
from datadog_api_client.v2.model.security_monitoring_signal_incidents_update_attributes import (
    SecurityMonitoringSignalIncidentsUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signal_incidents_update_data import (
    SecurityMonitoringSignalIncidentsUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_signal_incidents_update_request import (
    SecurityMonitoringSignalIncidentsUpdateRequest,
)

body = SecurityMonitoringSignalIncidentsUpdateRequest(
    data=SecurityMonitoringSignalIncidentsUpdateData(
        attributes=SecurityMonitoringSignalIncidentsUpdateAttributes(
            incident_ids=SecurityMonitoringSignalIncidentIds(
                [
                    2066,
                ]
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_signal_incidents(
        signal_id="AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE", body=body
    )

    print(response)
