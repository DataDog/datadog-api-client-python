"""
Update a critical asset returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_critical_asset_severity import (
    SecurityMonitoringCriticalAssetSeverity,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_type import SecurityMonitoringCriticalAssetType
from datadog_api_client.v2.model.security_monitoring_critical_asset_update_attributes import (
    SecurityMonitoringCriticalAssetUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_update_data import (
    SecurityMonitoringCriticalAssetUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_update_request import (
    SecurityMonitoringCriticalAssetUpdateRequest,
)

# there is a valid "critical_asset" in the system
CRITICAL_ASSET_DATA_ID = environ["CRITICAL_ASSET_DATA_ID"]

body = SecurityMonitoringCriticalAssetUpdateRequest(
    data=SecurityMonitoringCriticalAssetUpdateData(
        type=SecurityMonitoringCriticalAssetType.CRITICAL_ASSETS,
        attributes=SecurityMonitoringCriticalAssetUpdateAttributes(
            enabled=False,
            query="no:alert",
            rule_query="type:(log_detection OR signal_correlation OR workload_security OR application_security) ruleId:djg-ktx-ipq",
            severity=SecurityMonitoringCriticalAssetSeverity.DECREASE,
            tags=[
                "env:production",
            ],
            version=1,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_critical_asset(
        critical_asset_id=CRITICAL_ASSET_DATA_ID, body=body
    )

    print(response)
