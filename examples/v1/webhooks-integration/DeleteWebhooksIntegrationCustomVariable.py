"""
Delete a custom variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = environ["WEBHOOK_CUSTOM_VARIABLE_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    api_instance.delete_webhooks_integration_custom_variable(
        custom_variable_name=WEBHOOK_CUSTOM_VARIABLE_NAME,
    )
