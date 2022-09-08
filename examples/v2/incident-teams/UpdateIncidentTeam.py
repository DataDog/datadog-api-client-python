"""
Update an existing incident team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi
from datadog_api_client.v2.model.incident_team_type import IncidentTeamType
from datadog_api_client.v2.model.incident_team_update_attributes import IncidentTeamUpdateAttributes
from datadog_api_client.v2.model.incident_team_update_data import IncidentTeamUpdateData
from datadog_api_client.v2.model.incident_team_update_request import IncidentTeamUpdateRequest

# there is a valid "team" in the system
TEAM_DATA_ATTRIBUTES_NAME = environ["TEAM_DATA_ATTRIBUTES_NAME"]
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

body = IncidentTeamUpdateRequest(
    data=IncidentTeamUpdateData(
        type=IncidentTeamType.TEAMS,
        attributes=IncidentTeamUpdateAttributes(
            name="team name-updated",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.update_incident_team(team_id=TEAM_DATA_ID, body=body)

    print(response)
