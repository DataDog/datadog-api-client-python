"""
Update a dataset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition
from datadog_api_client.v2.model.security_monitoring_dataset_definition_column import (
    SecurityMonitoringDatasetDefinitionColumn,
)
from datadog_api_client.v2.model.security_monitoring_dataset_definition_column_type import (
    SecurityMonitoringDatasetDefinitionColumnType,
)
from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType
from datadog_api_client.v2.model.security_monitoring_dataset_update_attributes_request import (
    SecurityMonitoringDatasetUpdateAttributesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_update_data_request import (
    SecurityMonitoringDatasetUpdateDataRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_update_request import (
    SecurityMonitoringDatasetUpdateRequest,
)
from uuid import UUID

body = SecurityMonitoringDatasetUpdateRequest(
    data=SecurityMonitoringDatasetUpdateDataRequest(
        attributes=SecurityMonitoringDatasetUpdateAttributesRequest(
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
            description="Updated dataset description",
            version=1,
        ),
        type=SecurityMonitoringDatasetType.SECURITY_MONITORING_DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_security_monitoring_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.update_security_monitoring_dataset(dataset_id=UUID("123e4567-e89b-12d3-a456-426614174000"), body=body)
