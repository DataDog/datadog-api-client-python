"""
Create an incident Microsoft Teams online meeting returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["create_incident_ms_teams_online_meeting"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_ms_teams_online_meeting(
        incident_id="incident_id",
    )

    print(response)
