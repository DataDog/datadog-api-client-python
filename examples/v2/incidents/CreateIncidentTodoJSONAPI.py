"""
Create an incident todo returns "CREATED" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray
from datadog_api_client.v2.model.incident_todo_create_request import IncidentTodoCreateRequestJSON

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentTodoCreateRequestJSON(
    assignees=IncidentTodoAssigneeArray(
        [
            "@test.user@test.com",
        ]
    ),
    content="Restore lost data.",
)

configuration = Configuration()
configuration.unstable_operations["create_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_todo(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
