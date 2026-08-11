"""
Create an Elastic Cloud monitoring account returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_integration_accounts_api import ElasticCloudIntegrationAccountsApi
from datadog_api_client.v2.model.elastic_cloud_basic_auth import ElasticCloudBasicAuth
from datadog_api_client.v2.model.elastic_cloud_basic_auth_type import ElasticCloudBasicAuthType
from datadog_api_client.v2.model.elastic_cloud_dataflow import ElasticCloudDataflow
from datadog_api_client.v2.model.elastic_cloud_dataflow_id import ElasticCloudDataflowId
from datadog_api_client.v2.model.elastic_cloud_monitoring_account_attributes import (
    ElasticCloudMonitoringAccountAttributes,
)
from datadog_api_client.v2.model.elastic_cloud_monitoring_account_create_data import (
    ElasticCloudMonitoringAccountCreateData,
)
from datadog_api_client.v2.model.elastic_cloud_monitoring_account_request import ElasticCloudMonitoringAccountRequest
from datadog_api_client.v2.model.elastic_cloud_settings import ElasticCloudSettings
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ElasticCloudMonitoringAccountRequest(
    data=ElasticCloudMonitoringAccountCreateData(
        attributes=ElasticCloudMonitoringAccountAttributes(
            authentication=ElasticCloudBasicAuth(
                password="your-password",
                type=ElasticCloudBasicAuthType.BASIC,
                username="datadog",
            ),
            dataflows=[
                ElasticCloudDataflow(
                    enabled=True,
                    id=ElasticCloudDataflowId.METRICS,
                ),
            ],
            name="elastic-cloud-prod",
            settings=ElasticCloudSettings(
                cat_allocation_stats_enabled=False,
                detailed_index_stats_enabled=False,
                index_stats_enabled=False,
                pending_task_stats_enabled=False,
                pshard_graceful_to_enabled=False,
                pshard_stats_enabled=False,
                slm_stats_enabled=False,
                tags=[
                    "env:prod",
                ],
                url="https://example.es.us-central1.gcp.cloud.es.io:9243",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_elastic_cloud_monitoring_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudIntegrationAccountsApi(api_client)
    response = api_instance.create_elastic_cloud_monitoring_account(body=body)

    print(response)
