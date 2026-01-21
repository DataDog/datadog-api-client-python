"""
Create incident attachment returns "Created" response
"""

from os import environ
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

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = CreateAttachmentRequest(
    data=CreateAttachmentRequestData(
        attributes=CreateAttachmentRequestDataAttributes(
            attachment=CreateAttachmentRequestDataAttributesAttachment(
                document_url="https://app.datadoghq.com/notebook/ExampleIncident/Example-Incident",
                title="Example-Incident",
            ),
            attachment_type=AttachmentDataAttributesAttachmentType.POSTMORTEM,
        ),
        type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_attachment(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
