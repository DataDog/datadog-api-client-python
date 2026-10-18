"""
Update a batch migration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_batch_migration_type import SecurityMonitoringBatchMigrationType
from datadog_api_client.v2.model.security_monitoring_batch_migration_update_attributes import (
    SecurityMonitoringBatchMigrationUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_update_data import (
    SecurityMonitoringBatchMigrationUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_batch_migration_update_request import (
    SecurityMonitoringBatchMigrationUpdateRequest,
)

# there is a valid "batch_migration" in the system
BATCH_MIGRATION_DATA_ID = environ["BATCH_MIGRATION_DATA_ID"]

body = SecurityMonitoringBatchMigrationUpdateRequest(
    data=SecurityMonitoringBatchMigrationUpdateData(
        type=SecurityMonitoringBatchMigrationType.BATCH_MIGRATION,
        attributes=SecurityMonitoringBatchMigrationUpdateAttributes(
            name="Example-Security-Monitoring-updated",
            tags=[
                "source:splunk",
                "team:secops",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_security_monitoring_batch_migration"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_batch_migration(batch_id=BATCH_MIGRATION_DATA_ID, body=body)

    print(response)
