"""
List Okta accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.list_okta_accounts()

    print(response)
