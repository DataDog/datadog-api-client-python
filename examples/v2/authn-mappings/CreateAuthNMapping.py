"""
Create an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_create_attributes import AuthNMappingCreateAttributes
from datadog_api_client.v2.model.authn_mapping_create_data import AuthNMappingCreateData
from datadog_api_client.v2.model.authn_mapping_create_relationships import AuthNMappingCreateRelationships
from datadog_api_client.v2.model.authn_mapping_create_request import AuthNMappingCreateRequest
from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingCreateRequest(
    data=AuthNMappingCreateData(
        attributes=AuthNMappingCreateAttributes(
            attribute_key="examplecreateanauthnmappingreturnsokresponse",
            attribute_value="Example-Create_an_AuthN_Mapping_returns_OK_response",
        ),
        relationships=AuthNMappingCreateRelationships(
            role=RelationshipToRole(
                data=RelationshipToRoleData(
                    id=ROLE_DATA_ID,
                    type=RolesType.ROLES,
                ),
            ),
        ),
        type=AuthNMappingsType.AUTHN_MAPPINGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.create_authn_mapping(body=body)

    print(response)
