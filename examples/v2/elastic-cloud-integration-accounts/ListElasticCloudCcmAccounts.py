"""
List Elastic Cloud CCM accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_integration_accounts_api import ElasticCloudIntegrationAccountsApi

configuration = Configuration()
configuration.unstable_operations["list_elastic_cloud_ccm_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudIntegrationAccountsApi(api_client)
    response = api_instance.list_elastic_cloud_ccm_accounts()

    print(response)
