"""
Delete a dataset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_security_monitoring_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_monitoring_dataset(
        dataset_id=UUID("123e4567-e89b-12d3-a456-426614174000"),
    )
