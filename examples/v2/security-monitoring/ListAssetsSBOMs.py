"""
List assets SBOMs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.asset_type import AssetType

configuration = Configuration()
configuration.unstable_operations["list_assets_sbo_ms"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_assets_sbo_ms(
        filter_asset_type=AssetType.SERVICE,
        filter_package_name="pandas",
    )

    print(response)
