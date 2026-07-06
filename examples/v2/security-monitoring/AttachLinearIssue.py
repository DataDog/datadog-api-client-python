"""
Attach security findings to a Linear issue returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.attach_linear_issue_request import AttachLinearIssueRequest
from datadog_api_client.v2.model.attach_linear_issue_request_data import AttachLinearIssueRequestData
from datadog_api_client.v2.model.attach_linear_issue_request_data_attributes import (
    AttachLinearIssueRequestDataAttributes,
)
from datadog_api_client.v2.model.attach_linear_issue_request_data_relationships import (
    AttachLinearIssueRequestDataRelationships,
)
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.linear_issues_data_type import LinearIssuesDataType

body = AttachLinearIssueRequest(
    data=AttachLinearIssueRequestData(
        attributes=AttachLinearIssueRequestDataAttributes(
            linear_issue_url="https://linear.app/your-workspace/issue/ENG-123",
        ),
        relationships=AttachLinearIssueRequestDataRelationships(
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
)

configuration = Configuration()
configuration.unstable_operations["attach_linear_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.attach_linear_issue(body=body)

    print(response)
