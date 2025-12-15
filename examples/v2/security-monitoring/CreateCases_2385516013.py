"""
Create case for security finding returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.case_data_type import CaseDataType
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.create_case_request_array import CreateCaseRequestArray
from datadog_api_client.v2.model.create_case_request_data import CreateCaseRequestData
from datadog_api_client.v2.model.create_case_request_data_attributes import CreateCaseRequestDataAttributes
from datadog_api_client.v2.model.create_case_request_data_relationships import CreateCaseRequestDataRelationships
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings

body = CreateCaseRequestArray(
    data=[
        CreateCaseRequestData(
            attributes=CreateCaseRequestDataAttributes(
                title="A title",
                description="A description",
            ),
            relationships=CreateCaseRequestDataRelationships(
                findings=Findings(
                    data=[
                        FindingData(
                            id="YjdhNDM3N2QyNTFjYmUwYTY3NDdhMTg0YTk2Yjg5MDl-ZjNmMzAwOTFkZDNhNGQzYzI0MzgxNTk4MjRjZmE2NzE=",
                            type=FindingDataType.FINDINGS,
                        ),
                    ],
                ),
                project=CaseManagementProject(
                    data=CaseManagementProjectData(
                        id="959a6f71-bac8-4027-b1d3-2264f569296f",
                        type=CaseManagementProjectDataType.PROJECTS,
                    ),
                ),
            ),
            type=CaseDataType.CASES,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_cases(body=body)

    print(response)
