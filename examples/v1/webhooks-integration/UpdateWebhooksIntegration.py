"""
Update a webhook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration_update_request import WebhooksIntegrationUpdateRequest

# there is a valid "webhook" in the system
WEBHOOK_NAME = environ["WEBHOOK_NAME"]

body = WebhooksIntegrationUpdateRequest(
    url="https://example.com/webhook-updated",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.update_webhooks_integration(webhook_name=WEBHOOK_NAME, body=body)

    print(response)
