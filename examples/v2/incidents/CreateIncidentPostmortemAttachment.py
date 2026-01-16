"""
Create postmortem attachment returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType
from datadog_api_client.v2.model.postmortem_attachment_request import PostmortemAttachmentRequest
from datadog_api_client.v2.model.postmortem_attachment_request_attributes import PostmortemAttachmentRequestAttributes
from datadog_api_client.v2.model.postmortem_attachment_request_data import PostmortemAttachmentRequestData
from datadog_api_client.v2.model.postmortem_cell import PostmortemCell
from datadog_api_client.v2.model.postmortem_cell_attributes import PostmortemCellAttributes
from datadog_api_client.v2.model.postmortem_cell_definition import PostmortemCellDefinition
from datadog_api_client.v2.model.postmortem_cell_type import PostmortemCellType

body = PostmortemAttachmentRequest(
    data=PostmortemAttachmentRequestData(
        attributes=PostmortemAttachmentRequestAttributes(
            cells=[
                PostmortemCell(
                    attributes=PostmortemCellAttributes(
                        definition=PostmortemCellDefinition(
                            content="## Incident Summary\nThis incident was caused by...",
                        ),
                    ),
                    id="cell-1",
                    type=PostmortemCellType.MARKDOWN,
                ),
            ],
            content="# Incident Report - IR-123\n[...]",
            postmortem_template_id="93645509-874e-45c4-adfa-623bfeaead89-123",
            title="Postmortem-IR-123",
        ),
        type=IncidentAttachmentType.INCIDENT_ATTACHMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_postmortem_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_postmortem_attachment(
        incident_id="00000000-0000-0000-0000-000000000000", body=body
    )

    print(response)
