"""
Create postmortem for an incident returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_postmortem_create_attributes import IncidentPostmortemCreateAttributes
from datadog_api_client.v2.model.incident_postmortem_create_data import IncidentPostmortemCreateData
from datadog_api_client.v2.model.incident_postmortem_create_request import IncidentPostmortemCreateRequest
from datadog_api_client.v2.model.incident_postmortem_type import IncidentPostmortemType

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentPostmortemCreateRequest(
    data=IncidentPostmortemCreateData(
        attributes=IncidentPostmortemCreateAttributes(
            document_url="https://app.datadoghq.com/notebook/123",
            title="Postmortem for IR-123",
        ),
        type=IncidentPostmortemType.INCIDENT_POSTMORTEMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_postmortem"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_postmortem(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
