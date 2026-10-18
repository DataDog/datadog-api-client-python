"""
Add resources to a batch migration returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_create_item import (
    SecurityMonitoringBatchMigrationResourceCreateItem,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_input_type import (
    SecurityMonitoringBatchMigrationResourceInputType,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_create_attributes import (
    SecurityMonitoringBatchMigrationResourcesCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_create_data import (
    SecurityMonitoringBatchMigrationResourcesCreateData,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_create_request import (
    SecurityMonitoringBatchMigrationResourcesCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_type import (
    SecurityMonitoringBatchMigrationResourcesType,
)

# there is a valid "batch_migration" in the system
BATCH_MIGRATION_DATA_ID = environ["BATCH_MIGRATION_DATA_ID"]

body = SecurityMonitoringBatchMigrationResourcesCreateRequest(
    data=SecurityMonitoringBatchMigrationResourcesCreateData(
        type=SecurityMonitoringBatchMigrationResourcesType.BATCH_MIGRATION_RESOURCES,
        attributes=SecurityMonitoringBatchMigrationResourcesCreateAttributes(
            resources=[
                SecurityMonitoringBatchMigrationResourceCreateItem(
                    name="Linux sudo abuse",
                    input_type=SecurityMonitoringBatchMigrationResourceInputType.SPL,
                    input='index=linux process=sudo "authentication failure" | stats count by user, host',
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_security_monitoring_batch_migration_resources"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_batch_migration_resources(
        batch_id=BATCH_MIGRATION_DATA_ID, body=body
    )

    print(response)
