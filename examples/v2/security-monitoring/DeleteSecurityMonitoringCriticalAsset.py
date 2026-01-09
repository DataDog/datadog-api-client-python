"""
Delete a critical asset returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "critical_asset" in the system
CRITICAL_ASSET_DATA_ID = environ["CRITICAL_ASSET_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_security_monitoring_critical_asset(
        critical_asset_id=CRITICAL_ASSET_DATA_ID,
    )
