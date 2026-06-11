"""
List identity providers returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.identity_providers_api import IdentityProvidersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IdentityProvidersApi(api_client)
    response = api_instance.list_identity_providers()

    print(response)
