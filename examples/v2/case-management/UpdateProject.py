"""
Update a project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType
from datadog_api_client.v2.model.project_update import ProjectUpdate
from datadog_api_client.v2.model.project_update_attributes import ProjectUpdateAttributes
from datadog_api_client.v2.model.project_update_request import ProjectUpdateRequest

body = ProjectUpdateRequest(
    data=ProjectUpdate(
        type=ProjectResourceType.PROJECT,
        attributes=ProjectUpdateAttributes(
            name="Updated Project Name Example-Case-Management",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_project(project_id="d4bbe1af-f36e-42f1-87c1-493ca35c320e", body=body)

    print(response)
