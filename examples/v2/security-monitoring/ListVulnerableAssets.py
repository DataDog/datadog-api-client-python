"""
List vulnerable assets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.asset_type import AssetType

configuration = Configuration()
configuration.unstable_operations["list_vulnerable_assets"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_vulnerable_assets(
        filter_type=AssetType.HOST,
        filter_repository_url="github.com/datadog/dd-go",
        filter_risks_in_production=True,
    )

    print(response)
