"""
Update a SAML configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles
from datadog_api_client.v2.model.roles_type import RolesType
from datadog_api_client.v2.model.saml_configuration_relationships import SAMLConfigurationRelationships
from datadog_api_client.v2.model.saml_configuration_update_attributes import SAMLConfigurationUpdateAttributes
from datadog_api_client.v2.model.saml_configuration_update_data import SAMLConfigurationUpdateData
from datadog_api_client.v2.model.saml_configuration_update_request import SAMLConfigurationUpdateRequest
from datadog_api_client.v2.model.saml_configurations_type import SAMLConfigurationsType

body = SAMLConfigurationUpdateRequest(
    data=SAMLConfigurationUpdateData(
        attributes=SAMLConfigurationUpdateAttributes(
            idp_initiated=True,
            jit_domains=[
                "example.com",
            ],
        ),
        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
        relationships=SAMLConfigurationRelationships(
            default_roles=RelationshipToRoles(
                data=[
                    RelationshipToRoleData(
                        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
                        type=RolesType.ROLES,
                    ),
                ],
            ),
        ),
        type=SAMLConfigurationsType.SAML_CONFIGURATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.update_saml_configuration(
        saml_config_uuid="3653d3c6-0c75-11ea-ad28-fb5701eabc7d", body=body
    )

    print(response)
