import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["update_incident_team"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    team_id = "team_id_example"  # str | The ID of the incident team.
    body = IncidentTeamUpdateRequest(
        data=IncidentTeamUpdateData(
            attributes=IncidentTeamUpdateAttributes(
                name="team name",
            ),
            id="00000000-0000-0000-0000-000000000000",
            type=IncidentTeamType("teams"),
        ),
    )  # IncidentTeamUpdateRequest | Incident Team Payload.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing incident team
        api_response = api_instance.update_incident_team(team_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->update_incident_team: %s\n" % e)
