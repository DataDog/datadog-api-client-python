"""
Create a team returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.relationship_to_users import RelationshipToUsers
from datadog_api_client.v2.model.team_create import TeamCreate
from datadog_api_client.v2.model.team_create_attributes import TeamCreateAttributes
from datadog_api_client.v2.model.team_create_relationships import TeamCreateRelationships
from datadog_api_client.v2.model.team_create_request import TeamCreateRequest
from datadog_api_client.v2.model.team_type import TeamType

body = TeamCreateRequest(
    data=TeamCreate(
        attributes=TeamCreateAttributes(
            handle="test-handle-a0fc0297eb519635",
            name="test-name-a0fc0297eb519635",
        ),
        relationships=TeamCreateRelationships(
            users=RelationshipToUsers(
                data=[],
            ),
        ),
        type=TeamType.TEAM,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team(body=body)

    print(response)
