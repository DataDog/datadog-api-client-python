"""
List batch migration resources returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "batch_migration" in the system
BATCH_MIGRATION_DATA_ID = environ["BATCH_MIGRATION_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_security_monitoring_batch_migration_resources"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_security_monitoring_batch_migration_resources(
        batch_id=BATCH_MIGRATION_DATA_ID,
    )

    print(response)
