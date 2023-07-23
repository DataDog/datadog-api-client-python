"""
Create a new incident team returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi
from datadog_api_client.v2.model.incident_team_create_request import IncidentTeamCreateRequestJSON

body = IncidentTeamCreateRequestJSON(
    name="Example-Incident-Team",
)

configuration = Configuration()
configuration.unstable_operations["create_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.create_incident_team(body=body)

    print(response)
