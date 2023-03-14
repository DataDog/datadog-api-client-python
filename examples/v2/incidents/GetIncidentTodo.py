"""
Get incident todo details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = environ["INCIDENT_TODO_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_todo(
        incident_id=INCIDENT_DATA_ID,
        todo_id=INCIDENT_TODO_DATA_ID,
    )

    print(response)
