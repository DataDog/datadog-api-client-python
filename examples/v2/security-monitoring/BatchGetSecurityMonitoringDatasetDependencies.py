"""
Get dataset dependencies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_request import (
    SecurityMonitoringDatasetDependenciesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_request_attributes import (
    SecurityMonitoringDatasetDependenciesRequestAttributes,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_request_data import (
    SecurityMonitoringDatasetDependenciesRequestData,
)

body = SecurityMonitoringDatasetDependenciesRequest(
    data=SecurityMonitoringDatasetDependenciesRequestData(
        attributes=SecurityMonitoringDatasetDependenciesRequestAttributes(
            dataset_ids=[
                "123e4567-e89b-12d3-a456-426614174000",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["batch_get_security_monitoring_dataset_dependencies"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.batch_get_security_monitoring_dataset_dependencies(body=body)

    print(response)
