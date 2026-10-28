"""
Create an incident responder returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_responder_data_request import IncidentResponderDataRequest
from datadog_api_client.v2.model.incident_responder_relationships_request import IncidentResponderRelationshipsRequest
from datadog_api_client.v2.model.incident_responder_request import IncidentResponderRequest
from datadog_api_client.v2.model.incident_responder_type import IncidentResponderType
from datadog_api_client.v2.model.incident_responder_user_relationship import IncidentResponderUserRelationship
from datadog_api_client.v2.model.incident_responder_user_relationship_data import IncidentResponderUserRelationshipData
from uuid import UUID

body = IncidentResponderRequest(
    data=IncidentResponderDataRequest(
        relationships=IncidentResponderRelationshipsRequest(
            user=IncidentResponderUserRelationship(
                data=IncidentResponderUserRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000000"),
                    type="users",
                ),
            ),
        ),
        type=IncidentResponderType.INCIDENT_RESPONDERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_incident_responder"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_responder(incident_id="incident_id", body=body)

    print(response)
