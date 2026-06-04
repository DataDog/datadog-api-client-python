"""
Update organization SAML preferences returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.org_saml_preferences_attributes import OrgSAMLPreferencesAttributes
from datadog_api_client.v2.model.org_saml_preferences_data import OrgSAMLPreferencesData
from datadog_api_client.v2.model.org_saml_preferences_type import OrgSAMLPreferencesType
from datadog_api_client.v2.model.org_saml_preferences_update_request import OrgSAMLPreferencesUpdateRequest
from uuid import UUID

body = OrgSAMLPreferencesUpdateRequest(
    data=OrgSAMLPreferencesData(
        attributes=OrgSAMLPreferencesAttributes(
            default_role_uuids=[
                UUID("8dd1cf3c-0c75-11ea-ad28-fb5701eabc7d"),
            ],
            jit_domains=[
                "example.com",
            ],
        ),
        id="00000000-0000-0000-0000-000000000000",
        type=OrgSAMLPreferencesType.SAML_PREFERENCES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_org_saml_configurations"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.update_org_saml_configurations(body=body)
