"""
List indicators of compromise returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["list_indicators_of_compromise"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_indicators_of_compromise(
        limit=1,
    )

    print(response)
