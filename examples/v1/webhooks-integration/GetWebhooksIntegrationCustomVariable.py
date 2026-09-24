"""
Get a custom variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.get_webhooks_integration_custom_variable(
        custom_variable_name="custom_variable_name",
    )

    print(response)
