"""
Delete resources from a batch migration returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_delete_attributes import (
    SecurityMonitoringBatchMigrationResourcesDeleteAttributes,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_delete_data import (
    SecurityMonitoringBatchMigrationResourcesDeleteData,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_delete_request import (
    SecurityMonitoringBatchMigrationResourcesDeleteRequest,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_type import (
    SecurityMonitoringBatchMigrationResourcesType,
)

# there is a valid "batch_migration" in the system
BATCH_MIGRATION_DATA_ID = environ["BATCH_MIGRATION_DATA_ID"]

# there is a valid "batch_migration_resource" in the system
BATCH_MIGRATION_RESOURCE_ID = environ["BATCH_MIGRATION_RESOURCE_ID"]

body = SecurityMonitoringBatchMigrationResourcesDeleteRequest(
    data=SecurityMonitoringBatchMigrationResourcesDeleteData(
        type=SecurityMonitoringBatchMigrationResourcesType.BATCH_MIGRATION_RESOURCES,
        attributes=SecurityMonitoringBatchMigrationResourcesDeleteAttributes(
            resource_ids=[
                BATCH_MIGRATION_RESOURCE_ID,
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_security_monitoring_batch_migration_resources"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_monitoring_batch_migration_resources(batch_id=BATCH_MIGRATION_DATA_ID, body=body)
