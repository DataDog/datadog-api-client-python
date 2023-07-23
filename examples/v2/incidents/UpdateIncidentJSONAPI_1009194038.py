"""
Remove commander from an incident returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequestJSON

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentUpdateRequestJSON(
    id=INCIDENT_DATA_ID,
    commander_user=None,
)

configuration = Configuration()
configuration.unstable_operations["update_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
