"""
Create, update, and delete incident attachments returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_attachment_link_attachment_type import IncidentAttachmentLinkAttachmentType
from datadog_api_client.v2.model.incident_attachment_link_attributes import IncidentAttachmentLinkAttributes
from datadog_api_client.v2.model.incident_attachment_link_attributes_attachment_object import (
    IncidentAttachmentLinkAttributesAttachmentObject,
)
from datadog_api_client.v2.model.incident_attachment_postmortem_attachment_type import (
    IncidentAttachmentPostmortemAttachmentType,
)
from datadog_api_client.v2.model.incident_attachment_postmortem_attributes import IncidentAttachmentPostmortemAttributes
from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType
from datadog_api_client.v2.model.incident_attachment_update_data import IncidentAttachmentUpdateData
from datadog_api_client.v2.model.incident_attachment_update_request import IncidentAttachmentUpdateRequest
from datadog_api_client.v2.model.incident_attachments_postmortem_attributes_attachment_object import (
    IncidentAttachmentsPostmortemAttributesAttachmentObject,
)

body = IncidentAttachmentUpdateRequest(
    data=[
        IncidentAttachmentUpdateData(
            attributes=IncidentAttachmentPostmortemAttributes(
                attachment=IncidentAttachmentsPostmortemAttributesAttachmentObject(
                    document_url="https://app.datadoghq.com/notebook/123",
                    title="Postmortem IR-123",
                ),
                attachment_type=IncidentAttachmentPostmortemAttachmentType.POSTMORTEM,
            ),
            id="00000000-abcd-0002-0000-000000000000",
            type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
        ),
        IncidentAttachmentUpdateData(
            attributes=IncidentAttachmentLinkAttributes(
                attachment=IncidentAttachmentLinkAttributesAttachmentObject(
                    document_url="https://www.example.com/webstore-failure-runbook",
                    title="Runbook for webstore service failures",
                ),
                attachment_type=IncidentAttachmentLinkAttachmentType.LINK,
            ),
            type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
        ),
        IncidentAttachmentUpdateData(
            id="00000000-abcd-0003-0000-000000000000",
            type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["update_incident_attachments"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_attachments(incident_id="incident_id", body=body)

    print(response)
