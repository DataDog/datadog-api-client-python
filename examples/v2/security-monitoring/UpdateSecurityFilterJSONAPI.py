"""
Update a security filter returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_update_request import SecurityFilterUpdateRequestJSON

# there is a valid "security_filter" in the system
SECURITY_FILTER_DATA_ID = environ["SECURITY_FILTER_DATA_ID"]

body = SecurityFilterUpdateRequestJSON(
    exclusion_filters=[],
    filtered_data_type=SecurityFilterFilteredDataType.LOGS,
    is_enabled=True,
    name="Example-Security-Monitoring",
    query="service:ExampleSecurityMonitoring",
    version=1,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_filter(security_filter_id=SECURITY_FILTER_DATA_ID, body=body)

    print(response)
