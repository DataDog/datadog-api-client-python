"""
Get dataset dependencies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_attributes_request import (
    SecurityMonitoringDatasetDependenciesAttributesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_data_request import (
    SecurityMonitoringDatasetDependenciesDataRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_request import (
    SecurityMonitoringDatasetDependenciesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_type import (
    SecurityMonitoringDatasetDependenciesType,
)

body = SecurityMonitoringDatasetDependenciesRequest(
    data=SecurityMonitoringDatasetDependenciesDataRequest(
        attributes=SecurityMonitoringDatasetDependenciesAttributesRequest(
            dataset_ids=[
                "dataset-1",
            ],
        ),
        type=SecurityMonitoringDatasetDependenciesType.SECURITY_MONITORING_DATASET_DEPENDENCIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["batch_get_security_monitoring_dataset_dependencies"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.batch_get_security_monitoring_dataset_dependencies(body=body)

    print(response)
