"""
Create a case link returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_link_attributes import CaseLinkAttributes
from datadog_api_client.v2.model.case_link_create import CaseLinkCreate
from datadog_api_client.v2.model.case_link_create_request import CaseLinkCreateRequest
from datadog_api_client.v2.model.case_link_resource_type import CaseLinkResourceType

body = CaseLinkCreateRequest(
    data=CaseLinkCreate(
        attributes=CaseLinkAttributes(
            child_entity_id="4417921d-0866-4a38-822c-6f2a0f65f77d",
            child_entity_type="CASE",
            parent_entity_id="bf0cbac6-4c16-4cfb-b6bf-ca5e0ec37a4f",
            parent_entity_type="CASE",
            relationship="BLOCKS",
        ),
        type=CaseLinkResourceType.LINK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_link"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_case_link(body=body)

    print(response)
