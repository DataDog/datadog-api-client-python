"""
Delete a custom framework returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.delete_custom_framework(
        org_id="org_id",
        handle="handle",
        version="version",
    )

    print(response)
