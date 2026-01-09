"""
Create a critical asset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_critical_asset_create_attributes import (
    SecurityMonitoringCriticalAssetCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_create_data import (
    SecurityMonitoringCriticalAssetCreateData,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_create_request import (
    SecurityMonitoringCriticalAssetCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_severity import (
    SecurityMonitoringCriticalAssetSeverity,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_type import SecurityMonitoringCriticalAssetType

body = SecurityMonitoringCriticalAssetCreateRequest(
    data=SecurityMonitoringCriticalAssetCreateData(
        type=SecurityMonitoringCriticalAssetType.CRITICAL_ASSETS,
        attributes=SecurityMonitoringCriticalAssetCreateAttributes(
            query="host:examplesecuritymonitoring",
            rule_query="type:(log_detection OR signal_correlation OR workload_security OR application_security) source:cloudtrail",
            severity=SecurityMonitoringCriticalAssetSeverity.DECREASE,
            tags=[
                "team:security",
                "env:test",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_critical_asset(body=body)

    print(response)
