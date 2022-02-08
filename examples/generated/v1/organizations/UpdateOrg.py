import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import organizations_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    public_id = "abc123"  # str | The `public_id` of the organization you are operating within.
    body = Organization(
        billing=OrganizationBilling(
            type="type_example",
        ),
        description="some description",
        name="New child org",
        public_id="abcdef12345",
        settings=OrganizationSettings(
            private_widget_share=False,
            saml=OrganizationSettingsSaml(
                enabled=False,
            ),
            saml_autocreate_access_role=AccessRole("st"),
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
            type="type_example",
        ),
    )  # Organization | 

    # example passing only required values which don't have defaults set
    try:
        # Update your organization
        api_response = api_instance.update_org(public_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationsApi->update_org: %s\n" % e)
