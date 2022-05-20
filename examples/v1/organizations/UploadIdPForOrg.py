"""
Upload IdP metadata returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.upload_idp_for_org(
        public_id="abc123",
        idp_file=open("./idp_metadata.xml", "rb"),
    )

    print(response)
