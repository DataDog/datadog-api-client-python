"""
Create an incident notification rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.create_incident_notification_rule_request import CreateIncidentNotificationRuleRequest
from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
    IncidentNotificationRuleConditionsItems,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes import (
    IncidentNotificationRuleCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes_visibility import (
    IncidentNotificationRuleCreateAttributesVisibility,
)
from datadog_api_client.v2.model.incident_notification_rule_create_data import IncidentNotificationRuleCreateData
from datadog_api_client.v2.model.incident_notification_rule_create_data_relationships import (
    IncidentNotificationRuleCreateDataRelationships,
)
from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType
from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.relationship_to_incident_notification_template import (
    RelationshipToIncidentNotificationTemplate,
)
from datadog_api_client.v2.model.relationship_to_incident_notification_template_data import (
    RelationshipToIncidentNotificationTemplateData,
)
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData
from uuid import UUID

body = CreateIncidentNotificationRuleRequest(
    data=IncidentNotificationRuleCreateData(
        attributes=IncidentNotificationRuleCreateAttributes(
            conditions=[
                IncidentNotificationRuleConditionsItems(
                    field="severity",
                    values=[
                        "SEV-1",
                        "SEV-2",
                    ],
                ),
            ],
            enabled=True,
            handles=[
                "@team-email@company.com",
                "@slack-channel",
            ],
            renotify_on=[
                "status",
                "severity",
            ],
            trigger="incident_created_trigger",
            visibility=IncidentNotificationRuleCreateAttributesVisibility.ORGANIZATION,
        ),
        relationships=IncidentNotificationRuleCreateDataRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id="00000000-0000-0000-0000-000000000000",
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
            notification_template=RelationshipToIncidentNotificationTemplate(
                data=RelationshipToIncidentNotificationTemplateData(
                    id=UUID("00000000-0000-0000-0000-000000000001"),
                    type=IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES,
                ),
            ),
        ),
        type=IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_notification_rule(body=body)

    print(response)
