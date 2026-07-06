"""
List users with an identity provider override returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.identity_providers_api import IdentityProvidersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IdentityProvidersApi(api_client)
    response = api_instance.list_identity_provider_users(
        idp_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
