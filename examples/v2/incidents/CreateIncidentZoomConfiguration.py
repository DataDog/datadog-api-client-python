"""
Create an incident Zoom configuration returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_zoom_configuration_data_attributes_request import (
    IncidentZoomConfigurationDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_zoom_configuration_data_request import IncidentZoomConfigurationDataRequest
from datadog_api_client.v2.model.incident_zoom_configuration_request import IncidentZoomConfigurationRequest
from datadog_api_client.v2.model.incident_zoom_configuration_type import IncidentZoomConfigurationType

body = IncidentZoomConfigurationRequest(
    data=IncidentZoomConfigurationDataRequest(
        attributes=IncidentZoomConfigurationDataAttributesRequest(
            manual_meeting_creation=False,
            meeting_chat_timeline_sync=False,
            post_meeting_summary=True,
        ),
        type=IncidentZoomConfigurationType.ZOOM_CONFIGURATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_zoom_configuration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_zoom_configuration(body=body)

    print(response)
