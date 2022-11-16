"""
Edit an AuthN Mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_update_attributes import AuthNMappingUpdateAttributes
from datadog_api_client.v2.model.authn_mapping_update_data import AuthNMappingUpdateData
from datadog_api_client.v2.model.authn_mapping_update_relationships import AuthNMappingUpdateRelationships
from datadog_api_client.v2.model.authn_mapping_update_request import AuthNMappingUpdateRequest
from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingUpdateRequest(
    data=AuthNMappingUpdateData(
        attributes=AuthNMappingUpdateAttributes(
            attribute_key="member-of",
            attribute_value="Development",
        ),
        id=AUTHN_MAPPING_DATA_ID,
        relationships=AuthNMappingUpdateRelationships(
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
    response = api_instance.update_authn_mapping(authn_mapping_id=AUTHN_MAPPING_DATA_ID, body=body)

    print(response)
