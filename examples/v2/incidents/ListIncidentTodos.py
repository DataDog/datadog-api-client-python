"""
Get a list of an incident's todos returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_incident_todos"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_todos(
        incident_id=INCIDENT_DATA_ID,
    )

    print(response)
