"""
Create a case view returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_view_create import CaseViewCreate
from datadog_api_client.v2.model.case_view_create_attributes import CaseViewCreateAttributes
from datadog_api_client.v2.model.case_view_create_request import CaseViewCreateRequest
from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType

body = CaseViewCreateRequest(
    data=CaseViewCreate(
        attributes=CaseViewCreateAttributes(
            name="Open bugs",
            project_id="e555e290-ed65-49bd-ae18-8acbfcf18db7",
            query="status:open type:bug",
        ),
        type=CaseViewResourceType.VIEW,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_view"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_case_view(body=body)

    print(response)
