"""
Update incident notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
    IncidentNotificationRuleConditionsItems,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes import (
    IncidentNotificationRuleCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_rule_create_attributes_visibility import (
    IncidentNotificationRuleCreateAttributesVisibility,
)
from datadog_api_client.v2.model.incident_notification_rule_create_data_relationships import (
    IncidentNotificationRuleCreateDataRelationships,
)
from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType
from datadog_api_client.v2.model.incident_notification_rule_update_data import IncidentNotificationRuleUpdateData
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.put_incident_notification_rule_request import PutIncidentNotificationRuleRequest
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData

# there is a valid "notification_rule" in the system
NOTIFICATION_RULE_DATA_ID = environ["NOTIFICATION_RULE_DATA_ID"]

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = PutIncidentNotificationRuleRequest(
    data=IncidentNotificationRuleUpdateData(
        attributes=IncidentNotificationRuleCreateAttributes(
            enabled=False,
            conditions=[
                IncidentNotificationRuleConditionsItems(
                    field="severity",
                    values=[
                        "SEV-1",
                    ],
                ),
            ],
            handles=[
                "@updated-team-email@company.com",
            ],
            visibility=IncidentNotificationRuleCreateAttributesVisibility.PRIVATE,
            trigger="incident_modified_trigger",
        ),
        relationships=IncidentNotificationRuleCreateDataRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id=INCIDENT_TYPE_DATA_ID,
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
        ),
        id=NOTIFICATION_RULE_DATA_ID,
        type=IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_notification_rule(id=NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)
