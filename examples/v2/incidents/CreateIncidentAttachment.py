"""
Create incident attachment returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.attachment_data_attributes_attachment_type import (
    AttachmentDataAttributesAttachmentType,
)
from datadog_api_client.v2.model.create_attachment_request import CreateAttachmentRequest
from datadog_api_client.v2.model.create_attachment_request_data import CreateAttachmentRequestData
from datadog_api_client.v2.model.create_attachment_request_data_attributes import CreateAttachmentRequestDataAttributes
from datadog_api_client.v2.model.create_attachment_request_data_attributes_attachment import (
    CreateAttachmentRequestDataAttributesAttachment,
)
from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType

body = CreateAttachmentRequest(
    data=CreateAttachmentRequestData(
        attributes=CreateAttachmentRequestDataAttributes(
            attachment=CreateAttachmentRequestDataAttributesAttachment(
                document_url="https://app.datadoghq.com/notebook/123/Postmortem-IR-123",
                title="Postmortem-IR-123",
            ),
            attachment_type=AttachmentDataAttributesAttachmentType.POSTMORTEM,
        ),
        id="00000000-0000-0000-0000-000000000000",
        type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_attachment(incident_id="incident_id", body=body)

    print(response)
