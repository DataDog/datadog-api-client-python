"""
Delete the Statuspage account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.statuspage_integration_api import StatuspageIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = StatuspageIntegrationApi(api_client)
    api_instance.delete_statuspage_account()
