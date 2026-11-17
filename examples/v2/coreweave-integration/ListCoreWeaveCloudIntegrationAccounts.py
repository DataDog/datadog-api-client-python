"""
List CoreWeave integration accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.core_weave_integration_api import CoreWeaveIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_core_weave_cloud_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = CoreWeaveIntegrationApi(api_client)
    response = api_instance.list_core_weave_cloud_integration_accounts()

    print(response)
