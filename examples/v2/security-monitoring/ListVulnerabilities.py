"""
List vulnerabilities returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.asset_type import AssetType
from datadog_api_client.v2.model.vulnerability_severity import VulnerabilitySeverity
from datadog_api_client.v2.model.vulnerability_tool import VulnerabilityTool

configuration = Configuration()
configuration.unstable_operations["list_vulnerabilities"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_vulnerabilities(
        filter_cvss_base_severity=VulnerabilitySeverity.HIGH,
        filter_tool=VulnerabilityTool.INFRA,
        filter_asset_type=AssetType.SERVICE,
    )

    print(response)
