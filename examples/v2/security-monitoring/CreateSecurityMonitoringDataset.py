"""
Create a dataset returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_dataset_attributes_request import (
    SecurityMonitoringDatasetAttributesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_column import SecurityMonitoringDatasetColumn
from datadog_api_client.v2.model.security_monitoring_dataset_create_data import SecurityMonitoringDatasetCreateData
from datadog_api_client.v2.model.security_monitoring_dataset_create_request import (
    SecurityMonitoringDatasetCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_create_type import SecurityMonitoringDatasetCreateType
from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition
from datadog_api_client.v2.model.security_monitoring_dataset_search import SecurityMonitoringDatasetSearch
from datadog_api_client.v2.model.security_monitoring_dataset_time_window import SecurityMonitoringDatasetTimeWindow

body = SecurityMonitoringDatasetCreateRequest(
    data=SecurityMonitoringDatasetCreateData(
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
        type=SecurityMonitoringDatasetCreateType.DATASET_CREATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_security_monitoring_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_dataset(body=body)

    print(response)
