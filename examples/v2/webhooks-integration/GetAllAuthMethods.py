"""
Get all auth methods returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.webhooks_integration_api import WebhooksIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.get_all_auth_methods()

    print(response)
