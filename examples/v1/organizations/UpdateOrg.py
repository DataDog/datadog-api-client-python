"""
Update your organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi
from datadog_api_client.v1.model.access_role import AccessRole
from datadog_api_client.v1.model.organization import Organization
from datadog_api_client.v1.model.organization_billing import OrganizationBilling
from datadog_api_client.v1.model.organization_settings import OrganizationSettings
from datadog_api_client.v1.model.organization_settings_saml import OrganizationSettingsSaml
from datadog_api_client.v1.model.organization_settings_saml_autocreate_users_domains import (
    OrganizationSettingsSamlAutocreateUsersDomains,
)
from datadog_api_client.v1.model.organization_settings_saml_idp_initiated_login import (
    OrganizationSettingsSamlIdpInitiatedLogin,
)
from datadog_api_client.v1.model.organization_settings_saml_strict_mode import OrganizationSettingsSamlStrictMode
from datadog_api_client.v1.model.organization_subscription import OrganizationSubscription

body = Organization(
    billing=OrganizationBilling(
        type="parent_billing",
    ),
    description="some description",
    name="New child org",
    public_id="abcdef12345",
    settings=OrganizationSettings(
        private_widget_share=False,
        saml=OrganizationSettingsSaml(
            enabled=False,
        ),
        saml_autocreate_access_role=AccessRole.STANDARD,
        saml_autocreate_users_domains=OrganizationSettingsSamlAutocreateUsersDomains(
            domains=[
                "example.com",
            ],
            enabled=False,
        ),
        saml_can_be_enabled=False,
        saml_idp_endpoint="https://my.saml.endpoint",
        saml_idp_initiated_login=OrganizationSettingsSamlIdpInitiatedLogin(
            enabled=False,
        ),
        saml_idp_metadata_uploaded=False,
        saml_login_url="https://my.saml.login.url",
        saml_strict_mode=OrganizationSettingsSamlStrictMode(
            enabled=False,
        ),
    ),
    subscription=OrganizationSubscription(
        type="pro",
    ),
    trial=False,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.update_org(public_id="abc123", body=body)

    print(response)
