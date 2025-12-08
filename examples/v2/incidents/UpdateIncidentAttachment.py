"""
Update incident attachment returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType
from datadog_api_client.v2.model.patch_attachment_request import PatchAttachmentRequest
from datadog_api_client.v2.model.patch_attachment_request_data import PatchAttachmentRequestData
from datadog_api_client.v2.model.patch_attachment_request_data_attributes import PatchAttachmentRequestDataAttributes
from datadog_api_client.v2.model.patch_attachment_request_data_attributes_attachment import (
    PatchAttachmentRequestDataAttributesAttachment,
)

body = PatchAttachmentRequest(
    data=PatchAttachmentRequestData(
        attributes=PatchAttachmentRequestDataAttributes(
            attachment=PatchAttachmentRequestDataAttributesAttachment(
                document_url="https://app.datadoghq.com/notebook/124/Postmortem-IR-124",
                title="Postmortem-IR-124",
            ),
        ),
        type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_attachment(
        incident_id="incident_id", attachment_id="00000000-0000-0000-0000-000000000002", body=body
    )

    print(response)
