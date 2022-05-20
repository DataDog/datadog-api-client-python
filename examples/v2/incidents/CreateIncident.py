"""
Create an incident returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_create_attributes import IncidentCreateAttributes
from datadog_api_client.v2.model.incident_create_data import IncidentCreateData
from datadog_api_client.v2.model.incident_create_relationships import IncidentCreateRelationships
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequest
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_single_value_type import (
    IncidentFieldAttributesSingleValueType,
)
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser
from datadog_api_client.v2.model.nullable_relationship_to_user_data import NullableRelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = IncidentCreateRequest(
    data=IncidentCreateData(
        type=IncidentType("incidents"),
        attributes=IncidentCreateAttributes(
            title="Example-Create_an_incident_returns_CREATED_response",
            customer_impacted=False,
            fields=dict(
                state=IncidentFieldAttributesSingleValue(
                    type=IncidentFieldAttributesSingleValueType("dropdown"),
                    value="resolved",
                ),
            ),
        ),
        relationships=IncidentCreateRelationships(
            commander_user=NullableRelationshipToUser(
                data=NullableRelationshipToUserData(
                    type=UsersType("users"),
                    id=USER_DATA_ID,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident(body=body)

    print(response)
