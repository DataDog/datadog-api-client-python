"""
Update an incident Jira template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_jira_template_data_attributes_request import (
    IncidentJiraTemplateDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_jira_template_data_request import IncidentJiraTemplateDataRequest
from datadog_api_client.v2.model.incident_jira_template_field_configuration import (
    IncidentJiraTemplateFieldConfiguration,
)
from datadog_api_client.v2.model.incident_jira_template_incident_type_relationship import (
    IncidentJiraTemplateIncidentTypeRelationship,
)
from datadog_api_client.v2.model.incident_jira_template_incident_type_relationship_data import (
    IncidentJiraTemplateIncidentTypeRelationshipData,
)
from datadog_api_client.v2.model.incident_jira_template_relationships import IncidentJiraTemplateRelationships
from datadog_api_client.v2.model.incident_jira_template_request import IncidentJiraTemplateRequest
from datadog_api_client.v2.model.incident_jira_template_type import IncidentJiraTemplateType
from uuid import UUID

body = IncidentJiraTemplateRequest(
    data=IncidentJiraTemplateDataRequest(
        attributes=IncidentJiraTemplateDataAttributesRequest(
            account_id="123456",
            field_configurations=[
                IncidentJiraTemplateFieldConfiguration(
                    incident_field="title",
                    jira_field_key="summary",
                    jira_field_type="string",
                    sync_direction="bidirectional",
                ),
            ],
            is_default=False,
            issue_id="10001",
            name="Default Jira Template",
            project_id="10000",
            project_key="INC",
            sync_enabled=True,
            type="jira",
        ),
        relationships=IncidentJiraTemplateRelationships(
            incident_type=IncidentJiraTemplateIncidentTypeRelationship(
                data=IncidentJiraTemplateIncidentTypeRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000000"),
                    type="incident_types",
                ),
            ),
        ),
        type=IncidentJiraTemplateType.INCIDENTS_JIRA_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_jira_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_jira_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
