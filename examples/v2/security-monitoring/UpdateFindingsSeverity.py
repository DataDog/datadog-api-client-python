"""
Override the severity of security findings returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.severity_override_data_type import SeverityOverrideDataType
from datadog_api_client.v2.model.severity_override_request import SeverityOverrideRequest
from datadog_api_client.v2.model.severity_override_request_data import SeverityOverrideRequestData
from datadog_api_client.v2.model.severity_override_request_data_attributes import SeverityOverrideRequestDataAttributes
from datadog_api_client.v2.model.severity_override_request_data_relationships import (
    SeverityOverrideRequestDataRelationships,
)
from datadog_api_client.v2.model.severity_override_set import SeverityOverrideSet
from datadog_api_client.v2.model.severity_override_set_action_type import SeverityOverrideSetActionType
from datadog_api_client.v2.model.severity_override_value import SeverityOverrideValue

body = SeverityOverrideRequest(
    data=SeverityOverrideRequestData(
        attributes=SeverityOverrideRequestDataAttributes(
            severity=SeverityOverrideSet(
                action=SeverityOverrideSetActionType.SET,
                description="Database contains sensitive data.",
                value=SeverityOverrideValue.HIGH,
            ),
        ),
        id="00000000-0000-0000-0000-000000000001",
        relationships=SeverityOverrideRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==",
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
