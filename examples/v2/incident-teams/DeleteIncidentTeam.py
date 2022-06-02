"""
Delete an existing incident team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi

# there is a valid "team" in the system
TEAM_DATA_ID = environ["TEAM_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    api_instance.delete_incident_team(
        team_id=TEAM_DATA_ID,
    )
