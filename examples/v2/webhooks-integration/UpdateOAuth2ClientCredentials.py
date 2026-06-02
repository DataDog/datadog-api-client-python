"""
Update an OAuth2 client credentials auth method returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import WebhooksOAuth2ClientCredentialsType
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_update_attributes import (
    WebhooksOAuth2ClientCredentialsUpdateAttributes,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_update_data import (
    WebhooksOAuth2ClientCredentialsUpdateData,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_update_request import (
    WebhooksOAuth2ClientCredentialsUpdateRequest,
)

body = WebhooksOAuth2ClientCredentialsUpdateRequest(
    data=WebhooksOAuth2ClientCredentialsUpdateData(
        attributes=WebhooksOAuth2ClientCredentialsUpdateAttributes(
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
    response = api_instance.update_o_auth2_client_credentials(auth_method_id="auth_method_id", body=body)

    print(response)
