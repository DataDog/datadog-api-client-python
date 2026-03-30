"""
Create an incident user-defined field returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.incident_user_defined_field_attributes_create_request import (
    IncidentUserDefinedFieldAttributesCreateRequest,
)
from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
from datadog_api_client.v2.model.incident_user_defined_field_create_data import IncidentUserDefinedFieldCreateData
from datadog_api_client.v2.model.incident_user_defined_field_create_relationships import (
    IncidentUserDefinedFieldCreateRelationships,
)
from datadog_api_client.v2.model.incident_user_defined_field_create_request import IncidentUserDefinedFieldCreateRequest
from datadog_api_client.v2.model.incident_user_defined_field_field_type import IncidentUserDefinedFieldFieldType
from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType
from datadog_api_client.v2.model.incident_user_defined_field_valid_value import IncidentUserDefinedFieldValidValue
from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
from datadog_api_client.v2.model.relationship_to_incident_type_data import RelationshipToIncidentTypeData

body = IncidentUserDefinedFieldCreateRequest(
    data=IncidentUserDefinedFieldCreateData(
        attributes=IncidentUserDefinedFieldAttributesCreateRequest(
            category=IncidentUserDefinedFieldCategory.WHAT_HAPPENED,
            collected=IncidentUserDefinedFieldCollected.ACTIVE,
            default_value="critical",
            display_name="Root Cause",
            name="root_cause",
            ordinal="1.5",
            required=False,
            tag_key="datacenter",
            type=IncidentUserDefinedFieldFieldType.TEXTBOX,
            valid_values=[
                IncidentUserDefinedFieldValidValue(
                    description="A critical severity incident.",
                    display_name="Critical",
                    short_description="Critical",
                    value="critical",
                ),
            ],
        ),
        relationships=IncidentUserDefinedFieldCreateRelationships(
            incident_type=RelationshipToIncidentType(
                data=RelationshipToIncidentTypeData(
                    id="00000000-0000-0000-0000-000000000000",
                    type=IncidentTypeType.INCIDENT_TYPES,
                ),
            ),
        ),
        type=IncidentUserDefinedFieldType.USER_DEFINED_FIELD,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_user_defined_field"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_user_defined_field(body=body)

    print(response)
