"""
Create incident notification template returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.create_incident_notification_template_request import (
    CreateIncidentNotificationTemplateRequest,
)
from datadog_api_client.v2.model.incident_notification_template_create_attributes import (
    IncidentNotificationTemplateCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_template_create_data import (
    IncidentNotificationTemplateCreateData,
)
from datadog_api_client.v2.model.incident_notification_template_create_data_relationships import (
    IncidentNotificationTemplateCreateDataRelationships,
)
from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = CreateIncidentNotificationTemplateRequest(
    data=IncidentNotificationTemplateCreateData(
        attributes=IncidentNotificationTemplateCreateAttributes(
            category="alert",
            content="An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.",
            name="Example-Incident",
            subject="SEV-2 Incident: Sample Incident Title",
        ),
        relationships=IncidentNotificationTemplateCreateDataRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id=INCIDENT_TYPE_DATA_ID,
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
        ),
        type=IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_notification_template(body=body)

    print(response)
