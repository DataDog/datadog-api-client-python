"""
Create ServiceNow ticket for case returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.service_now_ticket_create_attributes import ServiceNowTicketCreateAttributes
from datadog_api_client.v2.model.service_now_ticket_create_data import ServiceNowTicketCreateData
from datadog_api_client.v2.model.service_now_ticket_create_request import ServiceNowTicketCreateRequest
from datadog_api_client.v2.model.service_now_ticket_resource_type import ServiceNowTicketResourceType

body = ServiceNowTicketCreateRequest(
    data=ServiceNowTicketCreateData(
        attributes=ServiceNowTicketCreateAttributes(
            assignment_group="IT Support",
            instance_name="my-instance",
        ),
        type=ServiceNowTicketResourceType.TICKETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_service_now_ticket"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_service_now_ticket(case_id="case_id", body=body)
