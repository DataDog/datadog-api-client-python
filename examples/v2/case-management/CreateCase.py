"""
Create a case returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_create import CaseCreate
from datadog_api_client.v2.model.case_create_attributes import CaseCreateAttributes
from datadog_api_client.v2.model.case_create_relationships import CaseCreateRelationships
from datadog_api_client.v2.model.case_create_request import CaseCreateRequest
from datadog_api_client.v2.model.case_priority import CasePriority
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_type import CaseType
from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship
from datadog_api_client.v2.model.nullable_user_relationship_data import NullableUserRelationshipData
from datadog_api_client.v2.model.project_relationship import ProjectRelationship
from datadog_api_client.v2.model.project_relationship_data import ProjectRelationshipData
from datadog_api_client.v2.model.project_resource_type import ProjectResourceType
from datadog_api_client.v2.model.user_resource_type import UserResourceType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CaseCreateRequest(
    data=CaseCreate(
        attributes=CaseCreateAttributes(
            priority=CasePriority.NOT_DEFINED,
            title="Security breach investigation in 0cfbc5cbc676ee71",
            type=CaseType.STANDARD,
        ),
        relationships=CaseCreateRelationships(
            assignee=NullableUserRelationship(
                data=NullableUserRelationshipData(
                    id=USER_DATA_ID,
                    type=UserResourceType.USER,
                ),
            ),
            project=ProjectRelationship(
                data=ProjectRelationshipData(
                    id="d4bbe1af-f36e-42f1-87c1-493ca35c320e",
                    type=ProjectResourceType.PROJECT,
                ),
            ),
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_case(body=body)

    print(response)
