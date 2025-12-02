"""
Attach security finding to a case returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.attach_case_request import AttachCaseRequest
from datadog_api_client.v2.model.attach_case_request_data import AttachCaseRequestData
from datadog_api_client.v2.model.attach_case_request_data_relationships import AttachCaseRequestDataRelationships
from datadog_api_client.v2.model.case_data_type import CaseDataType
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings

body = AttachCaseRequest(
    data=AttachCaseRequestData(
        id="7d16945b-baf8-411e-ab2a-20fe43af1ea3",
        relationships=AttachCaseRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y=",
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
    response = api_instance.attach_case(case_id="7d16945b-baf8-411e-ab2a-20fe43af1ea3", body=body)

    print(response)
