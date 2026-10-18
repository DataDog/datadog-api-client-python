"""
Cancel a batch migration returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["cancel_security_monitoring_batch_migration"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.cancel_security_monitoring_batch_migration(
        batch_id=UUID("7cdb3a75-64fb-46ce-9445-41969e78fe8e"),
    )
