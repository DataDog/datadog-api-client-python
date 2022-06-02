"""
Get a list of all incident teams returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi

# there is a valid "team" in the system
TEAM_DATA_ATTRIBUTES_NAME = environ["TEAM_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
configuration.unstable_operations["list_incident_teams"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentTeamsApi(api_client)
    response = api_instance.list_incident_teams(
        filter=TEAM_DATA_ATTRIBUTES_NAME,
    )

    print(response)
