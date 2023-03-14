"""
Update an incident todo returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray
from datadog_api_client.v2.model.incident_todo_attributes import IncidentTodoAttributes
from datadog_api_client.v2.model.incident_todo_patch_data import IncidentTodoPatchData
from datadog_api_client.v2.model.incident_todo_patch_request import IncidentTodoPatchRequest
from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_todo"
INCIDENT_TODO_DATA_ID = environ["INCIDENT_TODO_DATA_ID"]

body = IncidentTodoPatchRequest(
    data=IncidentTodoPatchData(
        attributes=IncidentTodoAttributes(
            assignees=IncidentTodoAssigneeArray(
                [
                    "@test.user@test.com",
                ]
            ),
            content="Restore lost data.",
            completed="2023-03-06T22:00:00.000000+00:00",
            due_date="2023-07-10T05:00:00.000000+00:00",
        ),
        type=IncidentTodoType.INCIDENT_TODOS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_todo"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_todo(incident_id=INCIDENT_DATA_ID, todo_id=INCIDENT_TODO_DATA_ID, body=body)

    print(response)
