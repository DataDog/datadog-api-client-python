"""
Delete an Elastic Cloud integration account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_integration_accounts_api import ElasticCloudIntegrationAccountsApi
from datadog_api_client.v2.model.elastic_cloud_interface_id import ElasticCloudInterfaceId

configuration = Configuration()
configuration.unstable_operations["delete_elastic_cloud_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudIntegrationAccountsApi(api_client)
    api_instance.delete_elastic_cloud_integration_account(
        interface_id=ElasticCloudInterfaceId.ELASTIC_CLOUD,
        account_id="account_id",
    )
