"""
Delete a webhook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

# there is a valid "webhook" in the system
WEBHOOK_NAME = environ["WEBHOOK_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    api_instance.delete_webhooks_integration(
        webhook_name=WEBHOOK_NAME,
    )
