"""
Get all Opsgenie accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.list_opsgenie_accounts()

    print(response)
