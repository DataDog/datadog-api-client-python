"""
Upload IdP metadata returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.upload_idp_metadata(
        idp_file=open("fixtures/organizations/saml_configurations/valid_idp_metadata.xml", "rb"),
    )
