"""
Create an incident Statuspage incident returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_statuspage_incident_data_attributes_request import (
    IncidentStatuspageIncidentDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_statuspage_incident_data_request import IncidentStatuspageIncidentDataRequest
from datadog_api_client.v2.model.incident_statuspage_incident_request import IncidentStatuspageIncidentRequest
from datadog_api_client.v2.model.incident_statuspage_incident_type import IncidentStatuspageIncidentType

body = IncidentStatuspageIncidentRequest(
    data=IncidentStatuspageIncidentDataRequest(
        attributes=IncidentStatuspageIncidentDataAttributesRequest(
            body="We are investigating the issue.",
            deliver_notifications=True,
            impact="major",
            name="Service Outage",
            page_id="abc123",
            status="investigating",
        ),
        type=IncidentStatuspageIncidentType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_statuspage_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_statuspage_incident(incident_id="incident_id", body=body)

    print(response)
