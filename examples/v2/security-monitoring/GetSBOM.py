"""
Get SBOM returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.asset_type import AssetType

configuration = Configuration()
configuration.unstable_operations["get_sbom"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_sbom(
        asset_type=AssetType.REPOSITORY,
        filter_asset_name="github.com/datadog/datadog-agent",
    )

    print(response)
