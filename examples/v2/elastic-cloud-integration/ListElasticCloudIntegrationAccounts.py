"""
List Elastic Cloud integration accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_integration_api import ElasticCloudIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_elastic_cloud_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudIntegrationApi(api_client)
    response = api_instance.list_elastic_cloud_integration_accounts()

    print(response)
