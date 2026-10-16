"""
Create a batch migration returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_batch_migration_create_attributes import (
    SecurityMonitoringBatchMigrationCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_create_data import (
    SecurityMonitoringBatchMigrationCreateData,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_create_request import (
    SecurityMonitoringBatchMigrationCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_create_item import (
    SecurityMonitoringBatchMigrationResourceCreateItem,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_input_type import (
    SecurityMonitoringBatchMigrationResourceInputType,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_type import SecurityMonitoringBatchMigrationType

body = SecurityMonitoringBatchMigrationCreateRequest(
    data=SecurityMonitoringBatchMigrationCreateData(
        type=SecurityMonitoringBatchMigrationType.BATCH_MIGRATION,
        attributes=SecurityMonitoringBatchMigrationCreateAttributes(
            name="Example-Security-Monitoring",
            description="Rules imported from Splunk",
            tags=[
                "source:splunk",
            ],
            resources=[
                SecurityMonitoringBatchMigrationResourceCreateItem(
                    name="Repeated Windows login failures",
                    description="Detects repeated failed Windows authentication attempts.",
                    input_type=SecurityMonitoringBatchMigrationResourceInputType.SPL,
                    input="index=wineventlog EventCode=4625",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_security_monitoring_batch_migration"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_batch_migration(body=body)

    print(response)
