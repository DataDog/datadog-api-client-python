"""
Update a dataset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_dataset_attributes_request import (
    SecurityMonitoringDatasetAttributesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_column import SecurityMonitoringDatasetColumn
from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition
from datadog_api_client.v2.model.security_monitoring_dataset_search import SecurityMonitoringDatasetSearch
from datadog_api_client.v2.model.security_monitoring_dataset_time_window import SecurityMonitoringDatasetTimeWindow
from datadog_api_client.v2.model.security_monitoring_dataset_update_data import SecurityMonitoringDatasetUpdateData
from datadog_api_client.v2.model.security_monitoring_dataset_update_request import (
    SecurityMonitoringDatasetUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_update_type import SecurityMonitoringDatasetUpdateType

body = SecurityMonitoringDatasetUpdateRequest(
    data=SecurityMonitoringDatasetUpdateData(
        attributes=SecurityMonitoringDatasetAttributesRequest(
            definition=SecurityMonitoringDatasetDefinition(
                columns=[
                    SecurityMonitoringDatasetColumn(
                        column="message",
                        type="string",
                    ),
                ],
                data_source="logs",
                indexes=[],
                name="sample_dataset",
                query_filter="status = 'active'",
                search=SecurityMonitoringDatasetSearch(
                    query="*",
                ),
                storage="hot",
                table_name="my_reference_table",
                time_window=SecurityMonitoringDatasetTimeWindow(
                    _from=1700000000000,
                    to=1700003600000,
                ),
            ),
            description="A sample dataset used for detection rules.",
            version=1,
        ),
        type=SecurityMonitoringDatasetUpdateType.DATASET_UPDATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_security_monitoring_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.update_security_monitoring_dataset(dataset_id="123e4567-e89b-12d3-a456-426614174000", body=body)
