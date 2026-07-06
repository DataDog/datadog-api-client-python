"""
List users with an identity provider override returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.identity_providers_api import IdentityProvidersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IdentityProvidersApi(api_client)
    items = api_instance.list_identity_provider_users_with_pagination(
        idp_id="00000000-0000-0000-0000-000000000001",
    )
    for item in items:
        print(item)
