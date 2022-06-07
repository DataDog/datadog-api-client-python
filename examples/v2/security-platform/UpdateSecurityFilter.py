"""
Update a security filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_platform_api import SecurityPlatformApi
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_type import SecurityFilterType
from datadog_api_client.v2.model.security_filter_update_attributes import SecurityFilterUpdateAttributes
from datadog_api_client.v2.model.security_filter_update_data import SecurityFilterUpdateData
from datadog_api_client.v2.model.security_filter_update_request import SecurityFilterUpdateRequest

body = SecurityFilterUpdateRequest(
    data=SecurityFilterUpdateData(
        attributes=SecurityFilterUpdateAttributes(
            exclusion_filters=[],
            filtered_data_type=SecurityFilterFilteredDataType("logs"),
            is_enabled=True,
            name="Custom security filter",
            query="service:api",
            version=1,
        ),
        type=SecurityFilterType("security_filters"),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityPlatformApi(api_client)
    response = api_instance.update_security_filter(security_filter_id="security_filter_id", body=body)

    print(response)
