"""
Create a Custom OIDC provider returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi
from datadog_api_client.v2.model.oidc_cloud_auth_discovery_type import OIDCCloudAuthDiscoveryType
from datadog_api_client.v2.model.oidc_cloud_auth_provider_create_attributes import OIDCCloudAuthProviderCreateAttributes
from datadog_api_client.v2.model.oidc_cloud_auth_provider_create_data import OIDCCloudAuthProviderCreateData
from datadog_api_client.v2.model.oidc_cloud_auth_provider_create_request import OIDCCloudAuthProviderCreateRequest
from datadog_api_client.v2.model.oidc_cloud_auth_provider_type import OIDCCloudAuthProviderType

body = OIDCCloudAuthProviderCreateRequest(
    data=OIDCCloudAuthProviderCreateData(
        type=OIDCCloudAuthProviderType.CUSTOM_OIDC_PROVIDER_CONFIG,
        attributes=OIDCCloudAuthProviderCreateAttributes(
            provider_name="oidc-de20b7e944abfac3",
            issuer_url="https://oidc-de20b7e944abfac3.example.com",
            discovery_type=OIDCCloudAuthDiscoveryType.OIDC_DISCOVERY,
            audiences=[
                "sdk-test",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_oidc_cloud_auth_provider"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.create_oidc_cloud_auth_provider(body=body)

    print(response)
