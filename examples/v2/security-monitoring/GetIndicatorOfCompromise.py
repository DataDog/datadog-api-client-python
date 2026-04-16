"""
Get an indicator of compromise returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_indicator_of_compromise"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_indicator_of_compromise(
        indicator="masscan/1.3 (https://github.com/robertdavidgraham/masscan)",
    )

    print(response)
