"""
Attach security findings to a ServiceNow ticket returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.attach_service_now_ticket_request import AttachServiceNowTicketRequest
from datadog_api_client.v2.model.attach_service_now_ticket_request_data import AttachServiceNowTicketRequestData
from datadog_api_client.v2.model.attach_service_now_ticket_request_data_attributes import (
    AttachServiceNowTicketRequestDataAttributes,
)
from datadog_api_client.v2.model.attach_service_now_ticket_request_data_relationships import (
    AttachServiceNowTicketRequestDataRelationships,
)
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.service_now_tickets_data_type import ServiceNowTicketsDataType

body = AttachServiceNowTicketRequest(
    data=AttachServiceNowTicketRequestData(
        attributes=AttachServiceNowTicketRequestDataAttributes(
            servicenow_ticket_url="https://example.service-now.com/now/nav/ui/classic/params/target/incident.do?sys_id=abcdef0123456789abcdef0123456789",
        ),
        relationships=AttachServiceNowTicketRequestDataRelationships(
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
        type=ServiceNowTicketsDataType.SERVICENOW_TICKETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["attach_service_now_ticket"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.attach_service_now_ticket(body=body)

    print(response)
