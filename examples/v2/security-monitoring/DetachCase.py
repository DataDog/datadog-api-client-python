"""
Detach security findings from their case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.case_data_type import CaseDataType
from datadog_api_client.v2.model.detach_case_request import DetachCaseRequest
from datadog_api_client.v2.model.detach_case_request_data import DetachCaseRequestData
from datadog_api_client.v2.model.detach_case_request_data_relationships import DetachCaseRequestDataRelationships
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings

body = DetachCaseRequest(
    data=DetachCaseRequestData(
        relationships=DetachCaseRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="YzM2MTFjYzcyNmY0Zjg4MTAxZmRlNjQ1MWU1ZGQwYzR-YzI5NzE5Y2Y4MzU4ZjliNzhkNjYxNTY0ODIzZDQ2YTM=",
                        type=FindingDataType.FINDINGS,
                    ),
                ],
            ),
        ),
        type=CaseDataType.CASES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.detach_case(body=body)
