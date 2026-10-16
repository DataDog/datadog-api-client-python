"""
Publish a batch migration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_attributes import (
    SecurityMonitoringBatchMigrationPublishAttributes,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_data import (
    SecurityMonitoringBatchMigrationPublishData,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_request import (
    SecurityMonitoringBatchMigrationPublishRequest,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_type import (
    SecurityMonitoringBatchMigrationPublishType,
)
from uuid import UUID

body = SecurityMonitoringBatchMigrationPublishRequest(
    data=SecurityMonitoringBatchMigrationPublishData(
        attributes=SecurityMonitoringBatchMigrationPublishAttributes(
            resource_ids=[
                UUID("c968cf83-56c2-4d54-a993-6c86dfb83527"),
            ],
        ),
        type=SecurityMonitoringBatchMigrationPublishType.BATCH_MIGRATION_PUBLISH,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["publish_security_monitoring_batch_migration"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.publish_security_monitoring_batch_migration(
        batch_id=UUID("7cdb3a75-64fb-46ce-9445-41969e78fe8e"), body=body
    )

    print(response)
