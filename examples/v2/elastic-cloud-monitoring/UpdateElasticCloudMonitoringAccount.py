"""
Update an Elastic Cloud monitoring account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_monitoring_api import ElasticCloudMonitoringApi
from datadog_api_client.v2.model.elastic_cloud_basic_auth import ElasticCloudBasicAuth
from datadog_api_client.v2.model.elastic_cloud_basic_auth_type import ElasticCloudBasicAuthType
from datadog_api_client.v2.model.elastic_cloud_dataflow import ElasticCloudDataflow
from datadog_api_client.v2.model.elastic_cloud_dataflow_id import ElasticCloudDataflowId
from datadog_api_client.v2.model.elastic_cloud_monitoring_account_update_attributes import (
    ElasticCloudMonitoringAccountUpdateAttributes,
)
from datadog_api_client.v2.model.elastic_cloud_monitoring_account_update_data import (
    ElasticCloudMonitoringAccountUpdateData,
)
from datadog_api_client.v2.model.elastic_cloud_monitoring_account_update_request import (
    ElasticCloudMonitoringAccountUpdateRequest,
)
from datadog_api_client.v2.model.elastic_cloud_settings_update import ElasticCloudSettingsUpdate
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ElasticCloudMonitoringAccountUpdateRequest(
    data=ElasticCloudMonitoringAccountUpdateData(
        attributes=ElasticCloudMonitoringAccountUpdateAttributes(
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
            settings=ElasticCloudSettingsUpdate(
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
configuration.unstable_operations["update_elastic_cloud_monitoring_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudMonitoringApi(api_client)
    response = api_instance.update_elastic_cloud_monitoring_account(account_id="account_id", body=body)

    print(response)
