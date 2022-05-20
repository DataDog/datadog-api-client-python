"""
Create a webhooks integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration import WebhooksIntegration

body = WebhooksIntegration(
    name="Example-Create_a_webhooks_integration_returns_OK_response",
    url="https://example.com/webhook",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.create_webhooks_integration(body=body)

    print(response)
