"""
Create a security filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_filter_create_attributes import SecurityFilterCreateAttributes
from datadog_api_client.v2.model.security_filter_create_data import SecurityFilterCreateData
from datadog_api_client.v2.model.security_filter_create_request import SecurityFilterCreateRequest
from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_type import SecurityFilterType

body = SecurityFilterCreateRequest(
    data=SecurityFilterCreateData(
        attributes=SecurityFilterCreateAttributes(
            exclusion_filters=[
                SecurityFilterExclusionFilter(
                    name="Exclude staging",
                    query="source:staging",
                ),
            ],
            filtered_data_type=SecurityFilterFilteredDataType.LOGS,
            is_enabled=True,
            name="Example-Create_a_security_filter_returns_OK_response",
            query="service:ExampleCreateasecurityfilterreturnsOKresponse",
        ),
        type=SecurityFilterType.SECURITY_FILTERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_filter(body=body)

    print(response)
