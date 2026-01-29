"""
Get dataset history returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_security_monitoring_dataset_history"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_monitoring_dataset_history(
        dataset_id=UUID("123e4567-e89b-12d3-a456-426614174000"),
    )

    print(response)
