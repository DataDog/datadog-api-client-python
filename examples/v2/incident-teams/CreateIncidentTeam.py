"""
Create a new incident team returns "CREATED" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi
from datadog_api_client.v2.model.incident_team_create_attributes import IncidentTeamCreateAttributes
from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData
from datadog_api_client.v2.model.incident_team_create_request import IncidentTeamCreateRequest
from datadog_api_client.v2.model.incident_team_type import IncidentTeamType

body = IncidentTeamCreateRequest(
    data=IncidentTeamCreateData(
        type=IncidentTeamType("teams"),
        attributes=IncidentTeamCreateAttributes(name="Example-Create_a_new_incident_team_returns_CREATED_response"),
    )
)

with ApiClient(Configuration()) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.create_incident_team(body=body)

    print(response)
