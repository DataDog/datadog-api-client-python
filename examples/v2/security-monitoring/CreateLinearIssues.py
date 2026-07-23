"""
Create Linear issues for security findings returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.case_priority import CasePriority
from datadog_api_client.v2.model.create_linear_issue_request_array import CreateLinearIssueRequestArray
from datadog_api_client.v2.model.create_linear_issue_request_data import CreateLinearIssueRequestData
from datadog_api_client.v2.model.create_linear_issue_request_data_attributes import (
    CreateLinearIssueRequestDataAttributes,
)
from datadog_api_client.v2.model.create_linear_issue_request_data_relationships import (
    CreateLinearIssueRequestDataRelationships,
)
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.linear_issues_data_type import LinearIssuesDataType

body = CreateLinearIssueRequestArray(
    data=[
        CreateLinearIssueRequestData(
            attributes=CreateLinearIssueRequestDataAttributes(
                assignee_id="f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0",
                description="A description of the Linear issue.",
                label_ids=[
                    "a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                ],
                linear_project_id="d4c3b2a1-6f5e-8b7a-0d9c-2f1e4a3b6c5d",
                priority=CasePriority.NOT_DEFINED,
                title="A title for the Linear issue.",
            ),
            relationships=CreateLinearIssueRequestDataRelationships(
                findings=Findings(
                    data=[
                        FindingData(
                            id="ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==",
                            type=FindingDataType.FINDINGS,
                        ),
                    ],
                ),
                project=CaseManagementProject(
                    data=CaseManagementProjectData(
                        id="aeadc05e-98a8-11ec-ac2c-da7ad0900001",
                        type=CaseManagementProjectDataType.PROJECTS,
                    ),
                ),
            ),
            type=LinearIssuesDataType.LINEAR_ISSUES,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_linear_issues(body=body)

    print(response)
