"""
Create a page from an incident returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_create_page_attributes import IncidentCreatePageAttributes
from datadog_api_client.v2.model.incident_create_page_from_incident_data import IncidentCreatePageFromIncidentData
from datadog_api_client.v2.model.incident_create_page_from_incident_request import IncidentCreatePageFromIncidentRequest
from datadog_api_client.v2.model.incident_page_target import IncidentPageTarget
from datadog_api_client.v2.model.incident_page_target_type import IncidentPageTargetType
from datadog_api_client.v2.model.incident_page_type import IncidentPageType

body = IncidentCreatePageFromIncidentRequest(
    data=IncidentCreatePageFromIncidentData(
        attributes=IncidentCreatePageAttributes(
            description="Page created for incident response",
            services=[
                "web-service",
                "api-service",
            ],
            tags=[
                "urgent",
                "production",
            ],
            target=IncidentPageTarget(
                identifier="team-handle",
                type=IncidentPageTargetType.TEAM_HANDLE,
            ),
            title="Incident Response Page",
        ),
        type=IncidentPageType.PAGE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_page_from_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_page_from_incident(incident_id="incident_id", body=body)

    print(response)
