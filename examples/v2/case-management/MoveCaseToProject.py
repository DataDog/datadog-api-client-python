"""
Update case project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.project_relationship import ProjectRelationship
from datadog_api_client.v2.model.project_relationship_data import ProjectRelationshipData
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType

body = ProjectRelationship(
    data=ProjectRelationshipData(
        id="e555e290-ed65-49bd-ae18-8acbfcf18db7",
        type=ProjectResourceType.PROJECT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["move_case_to_project"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.move_case_to_project(case_id="case_id", body=body)

    print(response)
