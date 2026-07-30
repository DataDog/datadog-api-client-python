"""
Update an Elastic Cloud CCM account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_cloud_cost_management_api import ElasticCloudCloudCostManagementApi
from datadog_api_client.v2.model.elastic_cloud_ccm_account_update_attributes import (
    ElasticCloudCcmAccountUpdateAttributes,
)
from datadog_api_client.v2.model.elastic_cloud_ccm_account_update_data import ElasticCloudCcmAccountUpdateData
from datadog_api_client.v2.model.elastic_cloud_ccm_account_update_request import ElasticCloudCcmAccountUpdateRequest
from datadog_api_client.v2.model.elastic_cloud_ccm_dataflow import ElasticCloudCcmDataflow
from datadog_api_client.v2.model.elastic_cloud_ccm_dataflow_id import ElasticCloudCcmDataflowId
from datadog_api_client.v2.model.elastic_cloud_ccm_settings_update import ElasticCloudCcmSettingsUpdate
from datadog_api_client.v2.model.elastic_cloud_ccm_token_auth import ElasticCloudCcmTokenAuth
from datadog_api_client.v2.model.elastic_cloud_ccm_token_auth_type import ElasticCloudCcmTokenAuthType
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ElasticCloudCcmAccountUpdateRequest(
    data=ElasticCloudCcmAccountUpdateData(
        attributes=ElasticCloudCcmAccountUpdateAttributes(
            authentication=ElasticCloudCcmTokenAuth(
                api_key="your-billing-api-key",
                type=ElasticCloudCcmTokenAuthType.BEARER_TOKEN,
            ),
            dataflows=[
                ElasticCloudCcmDataflow(
                    enabled=True,
                    id=ElasticCloudCcmDataflowId.COST_DATA,
                ),
            ],
            name="elastic-cloud-ccm-prod",
            settings=ElasticCloudCcmSettingsUpdate(
                elastic_org_id="2079364244",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_elastic_cloud_ccm_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudCloudCostManagementApi(api_client)
    response = api_instance.update_elastic_cloud_ccm_account(account_id="account_id", body=body)

    print(response)
