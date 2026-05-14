"""
Update an incident status page notice returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_status_page_notice_integration_type import (
    IncidentStatusPageNoticeIntegrationType,
)
from datadog_api_client.v2.model.incident_status_page_notice_update_data import IncidentStatusPageNoticeUpdateData
from datadog_api_client.v2.model.incident_status_page_notice_update_data_attributes import (
    IncidentStatusPageNoticeUpdateDataAttributes,
)
from datadog_api_client.v2.model.incident_status_page_notice_update_request import IncidentStatusPageNoticeUpdateRequest
from uuid import UUID

body = IncidentStatusPageNoticeUpdateRequest(
    data=IncidentStatusPageNoticeUpdateData(
        attributes=IncidentStatusPageNoticeUpdateDataAttributes(
            message="The issue has been resolved.",
            status="resolved",
            title="Service degradation resolved.",
        ),
        type=IncidentStatusPageNoticeIntegrationType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_status_page_notice"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_status_page_notice(
        incident_id="incident_id",
        statuspage_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        notice_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        body=body,
    )

    print(response)
