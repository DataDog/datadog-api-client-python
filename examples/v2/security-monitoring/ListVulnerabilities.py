"""
List vulnerabilities returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.tool import Tool
from datadog_api_client.v2.model.vulnerability_type import VulnerabilityType

configuration = Configuration()
configuration.unstable_operations["list_vulnerabilities"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_vulnerabilities(
        filter_type=VulnerabilityType.COMMANDINJECTION,
        filter_tool=Tool.IAST,
        filter_asset_repository_url="github.com/datadog/dd-go",
    )

    print(response)
