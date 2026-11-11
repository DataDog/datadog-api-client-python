"""
Create a Nebius Cloud integration account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.nebius_cloud_integration_api import NebiusCloudIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_request import (
    NebiusCloudCostCollectionIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_settings_request import (
    NebiusCloudCostCollectionIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.nebius_cloud_integration_account_create_attributes import (
    NebiusCloudIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.nebius_cloud_integration_account_create_data import (
    NebiusCloudIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.nebius_cloud_integration_account_create_request import (
    NebiusCloudIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_request import (
    NebiusCloudIntegrationAccountServiceAccountAuthRequest,
)
from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_type import (
    NebiusCloudIntegrationAccountServiceAccountAuthType,
)
from datadog_api_client.v2.model.nebius_cloud_integration_account_settings_request import (
    NebiusCloudIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.nebius_cloud_integration_dataflows_request import (
    NebiusCloudIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_request import (
    NebiusCloudLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_settings_request import (
    NebiusCloudLogsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.nebius_cloud_resources_integration_dataflow_request import (
    NebiusCloudResourcesIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.nebius_cloud_service_quota_collection_integration_dataflow_request import (
    NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest,
)

body = NebiusCloudIntegrationAccountCreateRequest(
    data=NebiusCloudIntegrationAccountCreateData(
        attributes=NebiusCloudIntegrationAccountCreateAttributes(
            authentication=NebiusCloudIntegrationAccountServiceAccountAuthRequest(
                auth_type=NebiusCloudIntegrationAccountServiceAccountAuthType.NEBIUS_SERVICE_ACCOUNT,
                private_key="-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----",
                public_key_id="publickey-yyyyyyyy",
                service_account_id="serviceaccount-xxxxxxxx",
                static_api_key="eyJhbGciOi...static-api-key",
            ),
            dataflows=NebiusCloudIntegrationDataflowsRequest(
                nebius_cloud_cost_collection=NebiusCloudCostCollectionIntegrationDataflowRequest(
                    enabled=True,
                    settings=NebiusCloudCostCollectionIntegrationDataflowSettingsRequest(
                        access_key_id="AKID0123456789ABCDEF",
                        access_key_secret="wJalrXUtnFEMIstaticaccesskey",
                        bucket_name="nebius-cost-exports",
                        bucket_prefix_path="cost-export/2026/",
                        bucket_region="eu-north1",
                    ),
                ),
                nebius_cloud_logs=NebiusCloudLogsIntegrationDataflowRequest(
                    enabled=True,
                    settings=NebiusCloudLogsIntegrationDataflowSettingsRequest(
                        enabled_services=[
                            "nebius-cloud-compute",
                            "nebius-cloud-kubernetes",
                            "default",
                        ],
                    ),
                ),
                nebius_cloud_resources=NebiusCloudResourcesIntegrationDataflowRequest(
                    enabled=True,
                ),
                nebius_cloud_service_quota_collection=NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="nebius-prod",
            settings=NebiusCloudIntegrationAccountSettingsRequest(
                account_tags=[
                    "env:prod",
                    "team:ai",
                ],
                tenant_id="tenant-12345678",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_nebius_cloud_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = NebiusCloudIntegrationApi(api_client)
    response = api_instance.create_nebius_cloud_integration_account(body=body)

    print(response)
