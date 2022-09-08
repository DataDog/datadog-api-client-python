"""
Update a security filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_type import SecurityFilterType
from datadog_api_client.v2.model.security_filter_update_attributes import SecurityFilterUpdateAttributes
from datadog_api_client.v2.model.security_filter_update_data import SecurityFilterUpdateData
from datadog_api_client.v2.model.security_filter_update_request import SecurityFilterUpdateRequest

# there is a valid "security_filter" in the system
SECURITY_FILTER_DATA_ID = environ["SECURITY_FILTER_DATA_ID"]

body = SecurityFilterUpdateRequest(
    data=SecurityFilterUpdateData(
        attributes=SecurityFilterUpdateAttributes(
            exclusion_filters=[],
            filtered_data_type=SecurityFilterFilteredDataType.LOGS,
            is_enabled=True,
            name="Example-Update_a_security_filter_returns_OK_response",
            query="service:ExampleUpdateasecurityfilterreturnsOKresponse",
            version=1,
        ),
        type=SecurityFilterType.SECURITY_FILTERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_filter(security_filter_id=SECURITY_FILTER_DATA_ID, body=body)

    print(response)
