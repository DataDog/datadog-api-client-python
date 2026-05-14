"""
Update an incident communication returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_communication_content import IncidentCommunicationContent
from datadog_api_client.v2.model.incident_communication_content_handle import IncidentCommunicationContentHandle
from datadog_api_client.v2.model.incident_communication_data_attributes_request import (
    IncidentCommunicationDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_communication_data_request import IncidentCommunicationDataRequest
from datadog_api_client.v2.model.incident_communication_kind import IncidentCommunicationKind
from datadog_api_client.v2.model.incident_communication_request import IncidentCommunicationRequest
from datadog_api_client.v2.model.incident_communication_type import IncidentCommunicationType
from uuid import UUID

body = IncidentCommunicationRequest(
    data=IncidentCommunicationDataRequest(
        attributes=IncidentCommunicationDataAttributesRequest(
            communication_type=IncidentCommunicationKind.MANUAL,
            content=IncidentCommunicationContent(
                grouping_key="update-1",
                handles=[
                    IncidentCommunicationContentHandle(
                        created_at="2024-01-01T00:00:00.000Z",
                        display_name="#incidents-channel",
                        handle="@slack-incidents-channel",
                    ),
                ],
                message="Incident update for INC-123.",
                status=0,
                subject="Incident INC-123: Update",
            ),
        ),
        type=IncidentCommunicationType.COMMUNICATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_communication"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_communication(
        incident_id="incident_id", communication_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
