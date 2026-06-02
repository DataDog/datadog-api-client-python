"""
Assign or unassign security findings returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.assignee_data_type import AssigneeDataType
from datadog_api_client.v2.model.assignee_request import AssigneeRequest
from datadog_api_client.v2.model.assignee_request_data import AssigneeRequestData
from datadog_api_client.v2.model.assignee_request_data_attributes import AssigneeRequestDataAttributes
from datadog_api_client.v2.model.assignee_request_data_relationships import AssigneeRequestDataRelationships
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings

body = AssigneeRequest(
    data=AssigneeRequestData(
        attributes=AssigneeRequestDataAttributes(
            assignee_id="f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0",
        ),
        id="00000000-0000-0000-0000-000000000001",
        relationships=AssigneeRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==",
                        type=FindingDataType.FINDINGS,
                    ),
                ],
            ),
        ),
        type=AssigneeDataType.ASSIGNEE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_findings_assignee"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_findings_assignee(body=body)

    print(response)
