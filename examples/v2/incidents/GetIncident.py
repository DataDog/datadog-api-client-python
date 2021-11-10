"""
Get the details of an incident returns "OK" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

with ApiClient(Configuration()) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident(incident_id=INCIDENT_DATA_ID)

    print(response)
