"""
Unmute security findings returns "Accepted" response
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
                description="Resolved.",
                is_muted=False,
                reason=MuteFindingsReason.NO_PENDING_FIX,
            ),
        ),
        relationships=MuteFindingsRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="ZGVmLTAwMC0wYmd-MDE4NjcyMDJkMzE4MDE5ODY5MGE4ZmQ2MmFlMjg0Y2M=",
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
