"""
Update a batch migration resource returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_type import (
    SecurityMonitoringBatchMigrationResourceType,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_update_attributes import (
    SecurityMonitoringBatchMigrationResourceUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_update_data import (
    SecurityMonitoringBatchMigrationResourceUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_update_request import (
    SecurityMonitoringBatchMigrationResourceUpdateRequest,
)

# there is a valid "batch_migration" in the system
BATCH_MIGRATION_DATA_ID = environ["BATCH_MIGRATION_DATA_ID"]

# there is a valid "batch_migration_resource" in the system
BATCH_MIGRATION_RESOURCE_ID = environ["BATCH_MIGRATION_RESOURCE_ID"]

body = SecurityMonitoringBatchMigrationResourceUpdateRequest(
    data=SecurityMonitoringBatchMigrationResourceUpdateData(
        type=SecurityMonitoringBatchMigrationResourceType.BATCH_MIGRATION_RESOURCE,
        attributes=SecurityMonitoringBatchMigrationResourceUpdateAttributes(
            input="index=wineventlog EventCode=4625 | stats count by user",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_security_monitoring_batch_migration_resource"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_batch_migration_resource(
        batch_id=BATCH_MIGRATION_DATA_ID, resource_id=BATCH_MIGRATION_RESOURCE_ID, body=body
    )

    print(response)
