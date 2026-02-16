"""
Create security finding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType

configuration = Configuration()
configuration.unstable_operations["create_security_finding"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.create_security_finding(
        vendor="vendor",
        finding_type=SecurityFindingType.VULNERABILITY,
    )
