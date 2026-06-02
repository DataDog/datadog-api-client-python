"""
Create an OAuth2 client credentials auth method returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_create_attributes import (
    WebhooksOAuth2ClientCredentialsCreateAttributes,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_create_data import (
    WebhooksOAuth2ClientCredentialsCreateData,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_create_request import (
    WebhooksOAuth2ClientCredentialsCreateRequest,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import WebhooksOAuth2ClientCredentialsType

body = WebhooksOAuth2ClientCredentialsCreateRequest(
    data=WebhooksOAuth2ClientCredentialsCreateData(
        attributes=WebhooksOAuth2ClientCredentialsCreateAttributes(
            access_token_url="https://example.com/oauth/token",
            audience="https://api.example.com",
            client_id="my-client-id",
            client_secret="my-client-secret",
            name="my-oauth2-auth",
            scope="read:webhooks write:webhooks",
        ),
        type=WebhooksOAuth2ClientCredentialsType.WEBHOOKS_AUTH_METHOD_OAUTH2_CLIENT_CREDENTIALS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.create_o_auth2_client_credentials(body=body)

    print(response)
