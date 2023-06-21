from datadog_api_client.model_utils import to_json_api
from datadog_api_client.v2.model.incidents_response import IncidentsResponse, IncidentsResponseJSON
from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
from datadog_api_client.v2.model.incident_response_attributes import IncidentResponseAttributes
from datadog_api_client.v2.model.incident_response_relationships import IncidentResponseRelationships
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType


def test_to_json_api():
    response = IncidentsResponse(
        data=[
            IncidentResponseData(
                id="incident-id",
                type=IncidentType.INCIDENTS,
                attributes=IncidentResponseAttributes(title="incident title"),
                relationships=IncidentResponseRelationships(
                    created_by_user=RelationshipToUser(data=RelationshipToUserData(id="user-id", type=UsersType.USERS))
                ),
            )
        ]
    )
    [json_api_response] = to_json_api(response)

    assert isinstance(json_api_response, IncidentsResponseJSON)
    assert json_api_response.id == "incident-id"
    assert json_api_response.title == "incident title"
    assert json_api_response.created_by_user == "user-id"
