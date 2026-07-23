"""
Update postmortem template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.confluence_postmortem_settings import ConfluencePostmortemSettings
from datadog_api_client.v2.model.google_docs_postmortem_settings import GoogleDocsPostmortemSettings
from datadog_api_client.v2.model.postmortem_template_attributes_request import PostmortemTemplateAttributesRequest
from datadog_api_client.v2.model.postmortem_template_create_relationships import PostmortemTemplateCreateRelationships
from datadog_api_client.v2.model.postmortem_template_data_request import PostmortemTemplateDataRequest
from datadog_api_client.v2.model.postmortem_template_incident_type_relationship import (
    PostmortemTemplateIncidentTypeRelationship,
)
from datadog_api_client.v2.model.postmortem_template_incident_type_relationship_data import (
    PostmortemTemplateIncidentTypeRelationshipData,
)
from datadog_api_client.v2.model.postmortem_template_location import PostmortemTemplateLocation
from datadog_api_client.v2.model.postmortem_template_request import PostmortemTemplateRequest
from datadog_api_client.v2.model.postmortem_template_type import PostmortemTemplateType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = PostmortemTemplateRequest(
    data=PostmortemTemplateDataRequest(
        attributes=PostmortemTemplateAttributesRequest(
            confluence_postmortem_settings=ConfluencePostmortemSettings(
                account_id="123456",
                parent_id="345678",
                space_id="789012",
            ),
            content="# Overview\n\n# What Happened\n\n# Timeline\n\n# Action Items",
            google_docs_postmortem_settings=GoogleDocsPostmortemSettings(
                account_id="123456",
                parent_folder_id="789012",
            ),
            is_default=datetime(2024, 1, 1, 0, 0, tzinfo=tzutc()),
            location=PostmortemTemplateLocation.DATADOG_NOTEBOOKS,
            name="Standard Postmortem Template",
        ),
        id="00000000-0000-0000-0000-000000000000",
        relationships=PostmortemTemplateCreateRelationships(
            incident_type=PostmortemTemplateIncidentTypeRelationship(
                data=PostmortemTemplateIncidentTypeRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000009"),
                    type="incident_types",
                ),
            ),
        ),
        type=PostmortemTemplateType.POSTMORTEM_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_postmortem_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_postmortem_template(template_id="template_id", body=body)

    print(response)
