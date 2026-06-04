"""
Get a SAML configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.get_saml_configuration(
        saml_config_uuid="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    )

    print(response)
