"""
Delete a Custom OIDC provider returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi

# there is a valid "oidc_cloud_auth_provider" in the system
OIDC_CLOUD_AUTH_PROVIDER_DATA_ID = environ["OIDC_CLOUD_AUTH_PROVIDER_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_oidc_cloud_auth_provider"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    api_instance.delete_oidc_cloud_auth_provider(
        provider_id=OIDC_CLOUD_AUTH_PROVIDER_DATA_ID,
    )
