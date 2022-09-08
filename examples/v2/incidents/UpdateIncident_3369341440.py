"""
Add commander to an incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData
from datadog_api_client.v2.model.incident_update_relationships import IncidentUpdateRelationships
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
from datadog_api_client.v2.model.nullable_relationship_to_user_data import NullableRelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = IncidentUpdateRequest(
    data=IncidentUpdateData(
        id=INCIDENT_DATA_ID,
        type=IncidentType.INCIDENTS,
        relationships=IncidentUpdateRelationships(
            commander_user=NullableRelationshipToUser(
                data=NullableRelationshipToUserData(
                    id=USER_DATA_ID,
                    type=UsersType.USERS,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
