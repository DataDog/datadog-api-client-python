"""
Enable Storage Management for a bucket returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_inventory_sync_configs_api import CloudInventorySyncConfigsApi
from datadog_api_client.v2.model.cloud_inventory_cloud_provider_id import CloudInventoryCloudProviderId
from datadog_api_client.v2.model.cloud_inventory_cloud_provider_request_type import (
    CloudInventoryCloudProviderRequestType,
)
from datadog_api_client.v2.model.cloud_inventory_sync_config_aws_request_attributes import (
    CloudInventorySyncConfigAWSRequestAttributes,
)
from datadog_api_client.v2.model.cloud_inventory_sync_config_azure_request_attributes import (
    CloudInventorySyncConfigAzureRequestAttributes,
)
from datadog_api_client.v2.model.cloud_inventory_sync_config_gcp_request_attributes import (
    CloudInventorySyncConfigGCPRequestAttributes,
)
from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request import UpsertCloudInventorySyncConfigRequest
from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request_attributes import (
    UpsertCloudInventorySyncConfigRequestAttributes,
)
from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request_data import (
    UpsertCloudInventorySyncConfigRequestData,
)

body = UpsertCloudInventorySyncConfigRequest(
    data=UpsertCloudInventorySyncConfigRequestData(
        attributes=UpsertCloudInventorySyncConfigRequestAttributes(
            aws=CloudInventorySyncConfigAWSRequestAttributes(
                aws_account_id="123456789012",
                destination_bucket_name="my-inventory-bucket",
                destination_bucket_region="us-east-1",
                destination_prefix="logs/",
            ),
            azure=CloudInventorySyncConfigAzureRequestAttributes(
                client_id="11111111-1111-1111-1111-111111111111",
                container="inventory-container",
                resource_group="my-resource-group",
                storage_account="mystorageaccount",
                subscription_id="33333333-3333-3333-3333-333333333333",
                tenant_id="22222222-2222-2222-2222-222222222222",
            ),
            gcp=CloudInventorySyncConfigGCPRequestAttributes(
                destination_bucket_name="my-inventory-reports",
                project_id="my-gcp-project",
                service_account_email="reader@my-gcp-project.iam.gserviceaccount.com",
                source_bucket_name="my-monitored-bucket",
            ),
        ),
        id=CloudInventoryCloudProviderId.AWS,
        type=CloudInventoryCloudProviderRequestType.CLOUD_PROVIDER,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_sync_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudInventorySyncConfigsApi(api_client)
    response = api_instance.upsert_sync_config(body=body)

    print(response)
