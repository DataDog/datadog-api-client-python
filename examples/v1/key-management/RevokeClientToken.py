"""
Revoke client token returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.client_token_revoke_request import ClientTokenRevokeRequest

body = ClientTokenRevokeRequest(
    hash="1234567890abcdef1234567890abcdef123",
)

configuration = Configuration()
configuration.unstable_operations["revoke_client_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.revoke_client_token(body=body)
