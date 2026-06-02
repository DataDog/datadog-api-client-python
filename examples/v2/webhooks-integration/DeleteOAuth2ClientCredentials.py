"""
Delete an OAuth2 client credentials auth method returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.webhooks_integration_api import WebhooksIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    api_instance.delete_o_auth2_client_credentials(
        auth_method_id="auth_method_id",
    )
