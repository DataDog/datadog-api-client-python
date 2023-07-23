"""
Create a security filter returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_filter_create_request import SecurityFilterCreateRequestJSON
from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

body = SecurityFilterCreateRequestJSON(
    exclusion_filters=[
        SecurityFilterExclusionFilter(
            name="Exclude staging",
            query="source:staging",
        ),
    ],
    filtered_data_type=SecurityFilterFilteredDataType.LOGS,
    is_enabled=True,
    name="Example-Security-Monitoring",
    query="service:ExampleSecurityMonitoring",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_filter(body=body)

    print(response)
