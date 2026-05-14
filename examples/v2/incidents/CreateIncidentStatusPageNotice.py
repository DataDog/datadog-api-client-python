"""
Publish an incident status page notice returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_status_page_notice_create_data import IncidentStatusPageNoticeCreateData
from datadog_api_client.v2.model.incident_status_page_notice_create_data_attributes import (
    IncidentStatusPageNoticeCreateDataAttributes,
)
from datadog_api_client.v2.model.incident_status_page_notice_create_request import IncidentStatusPageNoticeCreateRequest
from datadog_api_client.v2.model.incident_status_page_notice_integration_type import (
    IncidentStatusPageNoticeIntegrationType,
)
from uuid import UUID

body = IncidentStatusPageNoticeCreateRequest(
    data=IncidentStatusPageNoticeCreateData(
        attributes=IncidentStatusPageNoticeCreateDataAttributes(
            components=dict(
                component_1="degraded_performance",
            ),
            message="We are investigating reports of elevated error rates.",
            status="investigating",
            title="Service degradation detected.",
        ),
        type=IncidentStatusPageNoticeIntegrationType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_status_page_notice"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_status_page_notice(
        incident_id="incident_id", statuspage_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
