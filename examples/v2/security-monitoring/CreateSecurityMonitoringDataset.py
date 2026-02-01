"""
Create a dataset returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_dataset_create_attributes_request import (
    SecurityMonitoringDatasetCreateAttributesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_create_data_request import (
    SecurityMonitoringDatasetCreateDataRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_create_request import (
    SecurityMonitoringDatasetCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition
from datadog_api_client.v2.model.security_monitoring_dataset_definition_column import (
    SecurityMonitoringDatasetDefinitionColumn,
)
from datadog_api_client.v2.model.security_monitoring_dataset_definition_column_type import (
    SecurityMonitoringDatasetDefinitionColumnType,
)
from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType

body = SecurityMonitoringDatasetCreateRequest(
    data=SecurityMonitoringDatasetCreateDataRequest(
        attributes=SecurityMonitoringDatasetCreateAttributesRequest(
            definition=SecurityMonitoringDatasetDefinition(
                columns=[
                    SecurityMonitoringDatasetDefinitionColumn(
                        column="message",
                        type=SecurityMonitoringDatasetDefinitionColumnType.STRING,
                    ),
                ],
                data_source="logs",
                indexes=[
                    "k9",
                ],
                name="my_dataset",
            ),
            description="A dataset for monitoring authentication events",
        ),
        type=SecurityMonitoringDatasetType.SECURITY_MONITORING_DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_security_monitoring_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_dataset(body=body)

    print(response)
