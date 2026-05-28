"""
Register an OAuth2 client returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.o_auth2_client_public_api import OAuth2ClientPublicApi
from datadog_api_client.v2.model.o_auth_client_registration_grant_type import OAuthClientRegistrationGrantType
from datadog_api_client.v2.model.o_auth_client_registration_request import OAuthClientRegistrationRequest
from datadog_api_client.v2.model.o_auth_client_registration_response_type import OAuthClientRegistrationResponseType

body = OAuthClientRegistrationRequest(
    client_name="Example MCP Client",
    client_uri="https://example.com",
    grant_types=[
        OAuthClientRegistrationGrantType.AUTHORIZATION_CODE,
        OAuthClientRegistrationGrantType.REFRESH_TOKEN,
    ],
    jwks_uri="https://example.com/.well-known/jwks.json",
    logo_uri="https://example.com/logo.png",
    policy_uri="https://example.com/privacy",
    redirect_uris=[
        "https://example.com/oauth/callback",
    ],
    response_types=[
        OAuthClientRegistrationResponseType.CODE,
    ],
    scope="openid profile",
    token_endpoint_auth_method="none",
    tos_uri="https://example.com/tos",
)

configuration = Configuration()
configuration.unstable_operations["register_o_auth_client"] = True
with ApiClient(configuration) as api_client:
    api_instance = OAuth2ClientPublicApi(api_client)
    response = api_instance.register_o_auth_client(body=body)

    print(response)
