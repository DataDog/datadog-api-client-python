"""
Create an incident attachment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_attachment_link_attachment_type import IncidentAttachmentLinkAttachmentType
from datadog_api_client.v2.model.incident_attachment_link_attributes import IncidentAttachmentLinkAttributes
from datadog_api_client.v2.model.incident_attachment_link_attributes_attachment_object import (
    IncidentAttachmentLinkAttributesAttachmentObject,
)
from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType
from datadog_api_client.v2.model.incident_attachment_update_data import IncidentAttachmentUpdateData
from datadog_api_client.v2.model.incident_attachment_update_request import IncidentAttachmentUpdateRequest

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentAttachmentUpdateRequest(
    data=[
        IncidentAttachmentUpdateData(
            type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
            attributes=IncidentAttachmentLinkAttributes(
                attachment_type=IncidentAttachmentLinkAttachmentType.LINK,
                attachment=IncidentAttachmentLinkAttributesAttachmentObject(
                    document_url="https://www.example.com/doc",
                    title="Example-Create_an_incident_attachment_returns_OK_response",
                ),
            ),
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["update_incident_attachments"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_attachments(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
