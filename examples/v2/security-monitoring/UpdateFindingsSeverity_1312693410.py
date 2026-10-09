"""
Clear the severity override of security findings returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.severity_override_clear import SeverityOverrideClear
from datadog_api_client.v2.model.severity_override_clear_action_type import SeverityOverrideClearActionType
from datadog_api_client.v2.model.severity_override_data_type import SeverityOverrideDataType
from datadog_api_client.v2.model.severity_override_request import SeverityOverrideRequest
from datadog_api_client.v2.model.severity_override_request_data import SeverityOverrideRequestData
from datadog_api_client.v2.model.severity_override_request_data_attributes import SeverityOverrideRequestDataAttributes
from datadog_api_client.v2.model.severity_override_request_data_relationships import (
    SeverityOverrideRequestDataRelationships,
)

body = SeverityOverrideRequest(
    data=SeverityOverrideRequestData(
        attributes=SeverityOverrideRequestDataAttributes(
            severity=SeverityOverrideClear(
                action=SeverityOverrideClearActionType.CLEAR,
            ),
        ),
        relationships=SeverityOverrideRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="ZGVmLTAwMC0wYmd-MDE4NjcyMDJkMzE4MDE5ODY5MGE4ZmQ2MmFlMjg0Y2M=",
                        type=FindingDataType.FINDINGS,
                    ),
                ],
            ),
        ),
        type=SeverityOverrideDataType.SEVERITY_OVERRIDE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_findings_severity"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_findings_severity(body=body)

    print(response)
