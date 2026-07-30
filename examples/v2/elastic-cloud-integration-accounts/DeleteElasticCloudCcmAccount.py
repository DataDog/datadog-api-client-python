"""
Delete an Elastic Cloud CCM account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_integration_accounts_api import ElasticCloudIntegrationAccountsApi

configuration = Configuration()
configuration.unstable_operations["delete_elastic_cloud_ccm_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudIntegrationAccountsApi(api_client)
    api_instance.delete_elastic_cloud_ccm_account(
        account_id="account_id",
    )
