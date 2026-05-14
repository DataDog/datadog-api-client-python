"""
Create an incident Zoom meeting returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_create_zoom_meeting_data import IncidentCreateZoomMeetingData
from datadog_api_client.v2.model.incident_create_zoom_meeting_data_attributes import (
    IncidentCreateZoomMeetingDataAttributes,
)
from datadog_api_client.v2.model.incident_create_zoom_meeting_request import IncidentCreateZoomMeetingRequest
from datadog_api_client.v2.model.incident_zoom_integration_type import IncidentZoomIntegrationType

body = IncidentCreateZoomMeetingRequest(
    data=IncidentCreateZoomMeetingData(
        attributes=IncidentCreateZoomMeetingDataAttributes(
            topic="Incident INC-123 War Room",
        ),
        type=IncidentZoomIntegrationType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_zoom_meeting"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_zoom_meeting(incident_id="incident_id", body=body)

    print(response)
