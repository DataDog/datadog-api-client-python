"""
Create an Elastic Cloud integration account returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_integration_accounts_api import ElasticCloudIntegrationAccountsApi
from datadog_api_client.v2.model.elastic_cloud_detailed_index_stats_integration_dataflow_request import (
    ElasticCloudDetailedIndexStatsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.elastic_cloud_index_stats_integration_dataflow_request import (
    ElasticCloudIndexStatsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_create_attributes import (
    ElasticCloudIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_create_data import (
    ElasticCloudIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_create_request import (
    ElasticCloudIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_request import (
    ElasticCloudIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_request import (
    ElasticCloudIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.elastic_cloud_pending_task_stats_integration_dataflow_request import (
    ElasticCloudPendingTaskStatsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.elastic_cloud_primary_shard_graceful_timeout_integration_dataflow_request import (
    ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.elastic_cloud_primary_shard_stats_integration_dataflow_request import (
    ElasticCloudPrimaryShardStatsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.elastic_cloud_shard_allocation_stats_integration_dataflow_request import (
    ElasticCloudShardAllocationStatsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.elastic_cloud_slm_stats_integration_dataflow_request import (
    ElasticCloudSlmStatsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.integration_account_basic_auth_request import IntegrationAccountBasicAuthRequest
from datadog_api_client.v2.model.integration_account_basic_auth_type import IntegrationAccountBasicAuthType
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ElasticCloudIntegrationAccountCreateRequest(
    data=ElasticCloudIntegrationAccountCreateData(
        attributes=ElasticCloudIntegrationAccountCreateAttributes(
            authentication=IntegrationAccountBasicAuthRequest(
                auth_type=IntegrationAccountBasicAuthType.BASIC,
                password="your-password",
                username="datadog",
            ),
            dataflows=ElasticCloudIntegrationDataflowsRequest(
                elastic_cloud_detailed_index_stats=ElasticCloudDetailedIndexStatsIntegrationDataflowRequest(
                    enabled=True,
                ),
                elastic_cloud_index_stats=ElasticCloudIndexStatsIntegrationDataflowRequest(
                    enabled=True,
                ),
                elastic_cloud_pending_task_stats=ElasticCloudPendingTaskStatsIntegrationDataflowRequest(
                    enabled=True,
                ),
                elastic_cloud_primary_shard_graceful_timeout=ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest(
                    enabled=True,
                ),
                elastic_cloud_primary_shard_stats=ElasticCloudPrimaryShardStatsIntegrationDataflowRequest(
                    enabled=True,
                ),
                elastic_cloud_shard_allocation_stats=ElasticCloudShardAllocationStatsIntegrationDataflowRequest(
                    enabled=True,
                ),
                elastic_cloud_slm_stats=ElasticCloudSlmStatsIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="elastic-cloud-prod",
            settings=ElasticCloudIntegrationAccountSettingsRequest(
                tags="env:prod,team:saasint",
                url="https://example.es.us-central1.gcp.cloud.es.io:9243",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_elastic_cloud_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudIntegrationAccountsApi(api_client)
    response = api_instance.create_elastic_cloud_integration_account(body=body)

    print(response)
