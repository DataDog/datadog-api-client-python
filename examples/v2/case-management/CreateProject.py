"""
Create a project returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.project_create import ProjectCreate
from datadog_api_client.v2.model.project_create_attributes import ProjectCreateAttributes
from datadog_api_client.v2.model.project_create_request import ProjectCreateRequest
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType

body = ProjectCreateRequest(
    data=ProjectCreate(
        attributes=ProjectCreateAttributes(
            key="SEC",
            name="Security Investigation",
        ),
        type=ProjectResourceType.PROJECT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_project(body=body)

    print(response)
