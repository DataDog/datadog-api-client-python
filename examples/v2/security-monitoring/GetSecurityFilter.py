"""
Get a security filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "security_filter" in the system
SECURITY_FILTER_DATA_ID = environ["SECURITY_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_filter(
        security_filter_id=SECURITY_FILTER_DATA_ID,
    )

    print(response)
