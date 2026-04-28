"""
Mute or unmute security findings returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.mute_data_type import MuteDataType
from datadog_api_client.v2.model.mute_findings_mute_attributes import MuteFindingsMuteAttributes
from datadog_api_client.v2.model.mute_findings_reason import MuteFindingsReason
from datadog_api_client.v2.model.mute_findings_request import MuteFindingsRequest
from datadog_api_client.v2.model.mute_findings_request_data import MuteFindingsRequestData
from datadog_api_client.v2.model.mute_findings_request_data_attributes import MuteFindingsRequestDataAttributes
from datadog_api_client.v2.model.mute_findings_request_data_relationships import MuteFindingsRequestDataRelationships

body = MuteFindingsRequest(
    data=MuteFindingsRequestData(
        attributes=MuteFindingsRequestDataAttributes(
            mute=MuteFindingsMuteAttributes(
                description="To be resolved later.",
                expire_at=1778721573794,
                is_muted=True,
                reason=MuteFindingsReason.PENDING_FIX,
            ),
        ),
        id="93bfeb70-af47-424d-908a-948d3f08e37f",
        relationships=MuteFindingsRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==",
                        type=FindingDataType.FINDINGS,
                    ),
                ],
            ),
        ),
        type=MuteDataType.MUTE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["mute_security_findings"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.mute_security_findings(body=body)

    print(response)
