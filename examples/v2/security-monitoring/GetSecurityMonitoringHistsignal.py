"""
Get a hist signal's details returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_security_monitoring_histsignal"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_monitoring_histsignal(
        histsignal_id="histsignal_id",
    )

    print(response)
