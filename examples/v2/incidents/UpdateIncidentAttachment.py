"""
Update incident attachment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType
from datadog_api_client.v2.model.patch_attachment_request import PatchAttachmentRequest
from datadog_api_client.v2.model.patch_attachment_request_data import PatchAttachmentRequestData
from datadog_api_client.v2.model.patch_attachment_request_data_attributes import PatchAttachmentRequestDataAttributes
from datadog_api_client.v2.model.patch_attachment_request_data_attributes_attachment import (
    PatchAttachmentRequestDataAttributesAttachment,
)

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# there is a valid "incident_attachment" in the system
INCIDENT_ATTACHMENT_DATA_ID = environ["INCIDENT_ATTACHMENT_DATA_ID"]

body = PatchAttachmentRequest(
    data=PatchAttachmentRequestData(
        attributes=PatchAttachmentRequestDataAttributes(
            attachment=PatchAttachmentRequestDataAttributesAttachment(
                document_url="https://app.datadoghq.com/notebook/124/Example-Incident",
                title="Example-Incident",
            ),
        ),
        id=INCIDENT_ATTACHMENT_DATA_ID,
        type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_attachment(
        incident_id=INCIDENT_DATA_ID, attachment_id=INCIDENT_ATTACHMENT_DATA_ID, body=body
    )

    print(response)
